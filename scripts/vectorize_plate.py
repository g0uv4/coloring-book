#!/usr/bin/env python3
"""Trace a binary Open-Line Plate to SVG, then a true vector A4 PDF.

ibon does not accept SVG. The deliverable is the PDF (optional JPEG).
Uses potrace when installed; otherwise marching-squares + RDP (Pillow+numpy).
"""
from __future__ import annotations

import argparse
import math
import shutil
import subprocess
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

import numpy as np
from PIL import Image

A4_PT = (595.275590551, 841.88976378)  # 210mm x 297mm
MM = 72.0 / 25.4

# A=1 B=2 D=4 C=8 ; midpoints in (row, col) of the 2x2 cell
T, R, Bo, L = (0.0, 0.5), (0.5, 1.0), (1.0, 0.5), (0.5, 0.0)
MS_CASES = {
    1: [(T, L)],
    2: [(T, R)],
    3: [(L, R)],
    4: [(R, Bo)],
    5: [(T, R), (L, Bo)],
    6: [(T, Bo)],
    7: [(L, Bo)],
    8: [(L, Bo)],
    9: [(T, Bo)],
    10: [(T, L), (R, Bo)],
    11: [(R, Bo)],
    12: [(L, R)],
    13: [(T, R)],
    14: [(T, L)],
}


def load_ink(path: Path) -> np.ndarray:
    gray = np.asarray(Image.open(path).convert("L"))
    return gray < 128


def quant(p: tuple[float, float]) -> tuple[float, float]:
    return (round(p[0] * 2) / 2.0, round(p[1] * 2) / 2.0)


def marching_squares(ink: np.ndarray) -> dict:
    a, b, d, c = ink[:-1, :-1], ink[:-1, 1:], ink[1:, 1:], ink[1:, :-1]
    code = (
        a.astype(np.uint8)
        + (b.astype(np.uint8) << 1)
        + (d.astype(np.uint8) << 2)
        + (c.astype(np.uint8) << 3)
    )
    ys, xs = np.nonzero((code > 0) & (code < 15))
    adj: dict[tuple[float, float], list] = defaultdict(list)
    for y, x, k in zip(ys.tolist(), xs.tolist(), code[ys, xs].tolist()):
        for p0, p1 in MS_CASES[int(k)]:
            u = quant((y + p0[0], x + p0[1]))
            v = quant((y + p1[0], x + p1[1]))
            adj[u].append(v)
            adj[v].append(u)
    return adj


def stitch_loops(adj: dict) -> list[list[tuple[float, float]]]:
    used: set[tuple] = set()
    loops: list[list[tuple[float, float]]] = []
    for start in adj:
        for nxt in adj[start]:
            edge = (start, nxt) if start < nxt else (nxt, start)
            if edge in used:
                continue
            path = [start]
            prev, cur = start, nxt
            used.add(edge)
            guard = 0
            while cur != start and guard < 1_000_000:
                guard += 1
                path.append(cur)
                found = None
                for cand in adj[cur]:
                    if cand == prev:
                        continue
                    e = (cur, cand) if cur < cand else (cand, cur)
                    if e not in used:
                        found = cand
                        used.add(e)
                        break
                if found is None:
                    break
                prev, cur = cur, found
            if len(path) >= 8:
                if path[0] != path[-1]:
                    path.append(path[0])
                loops.append(path)
    return loops


def rdp(pts: list[tuple[float, float]], eps: float) -> list[tuple[float, float]]:
    if len(pts) < 3:
        return pts
    stack = [(0, len(pts) - 1)]
    keep = [False] * len(pts)
    keep[0] = keep[-1] = True
    while stack:
        i, j = stack.pop()
        ay, ax = pts[i]
        by, bx = pts[j]
        dx, dy = bx - ax, by - ay
        den = dx * dx + dy * dy or 1.0
        maxd, idx = -1.0, i
        for k in range(i + 1, j):
            py, px = pts[k]
            t = ((px - ax) * dx + (py - ay) * dy) / den
            t = 0.0 if t < 0 else 1.0 if t > 1 else t
            dist = math.hypot(px - (ax + t * dx), py - (ay + t * dy))
            if dist > maxd:
                maxd, idx = dist, k
        if maxd > eps:
            keep[idx] = True
            stack.append((i, idx))
            stack.append((idx, j))
    return [p for p, k in zip(pts, keep) if k]


def trace_python(ink: np.ndarray, eps: float) -> tuple[int, int, list]:
    # Pool very large plates so tracing stays snappy; coords scale back.
    step = 2 if max(ink.shape) >= 1800 else 1
    work = ink[::step, ::step]
    loops = stitch_loops(marching_squares(work))
    simp = []
    for loop in loops:
        s = rdp(loop, eps)
        if len(s) >= 4:
            if step != 1:
                s = [(y * step, x * step) for y, x in s]
            simp.append(s)
    h, w = ink.shape
    return w, h, simp


def svg_from_loops(width: int, height: int, loops: list) -> str:
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        '<path fill="#000" fill-rule="evenodd" d="',
    ]
    cmds = []
    for loop in loops:
        y0, x0 = loop[0]
        cmds.append(f"M {x0:.2f} {y0:.2f}")
        for y, x in loop[1:]:
            cmds.append(f"L {x:.2f} {y:.2f}")
        cmds.append("Z")
    parts.append(" ".join(cmds))
    parts.append('"/></svg>\n')
    return "\n".join(parts)


def try_potrace(src_png: Path, svg_out: Path) -> bool:
    exe = shutil.which("potrace")
    if not exe:
        return False
    with tempfile.TemporaryDirectory() as tmp:
        bmp = Path(tmp) / "plate.bmp"
        Image.open(src_png).convert("1").save(bmp)
        r = subprocess.run(
            [exe, "-s", "-o", str(svg_out), str(bmp)],
            capture_output=True,
            text=True,
        )
    return r.returncode == 0 and svg_out.is_file() and svg_out.stat().st_size > 200


def pdf_from_loops(
    loops: list,
    src_w: int,
    src_h: int,
    pdf_out: Path,
    *,
    landscape: bool,
    margin_mm: float,
) -> None:
    page_w, page_h = (A4_PT[1], A4_PT[0]) if landscape else A4_PT
    margin = margin_mm * MM
    inner_w = page_w - 2 * margin
    inner_h = page_h - 2 * margin
    scale = min(inner_w / src_w, inner_h / src_h)
    fit_w, fit_h = src_w * scale, src_h * scale
    tx = margin + (inner_w - fit_w) / 2.0
    ty = margin + (inner_h - fit_h) / 2.0

    # PDF y-up: x_pdf = tx + x_img * scale ; y_pdf = ty + (src_h - y_img) * scale
    ops = ["q", "0 0 0 rg", "0 0 0 RG"]
    for loop in loops:
        y0, x0 = loop[0]
        ops.append(f"{tx + x0 * scale:.3f} {ty + (src_h - y0) * scale:.3f} m")
        for y, x in loop[1:]:
            ops.append(f"{tx + x * scale:.3f} {ty + (src_h - y) * scale:.3f} l")
        ops.append("h")
    ops.append("f*")  # even-odd fill — keeps colorable pockets white
    ops.append("Q")
    stream = "\n".join(ops).encode("ascii") + b"\n"

    def obj(i: int, body: bytes) -> bytes:
        return f"{i} 0 obj\n".encode() + body + b"\nendobj\n"

    catalog = b"<< /Type /Catalog /Pages 2 0 R >>"
    pages = b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>"
    page = (
        f"<< /Type /Page /Parent 2 0 R "
        f"/MediaBox [0 0 {page_w:.3f} {page_h:.3f}] "
        f"/Contents 4 0 R >>"
    ).encode()
    contents = f"<< /Length {len(stream)} >>\nstream\n".encode() + stream + b"endstream"
    chunks = [
        b"%PDF-1.4\n",
        obj(1, catalog),
        obj(2, pages),
        obj(3, page),
        obj(4, contents),
    ]
    xref_pos = sum(len(c) for c in chunks)
    offsets = [0]
    running = len(chunks[0])
    for c in chunks[1:]:
        offsets.append(running)
        running += len(c)
    xref = [b"xref\n0 5\n0000000000 65535 f \n"]
    for off in offsets[1:]:
        xref.append(f"{off:010d} 00000 n \n".encode())
    tail = (
        b"trailer\n<< /Size 5 /Root 1 0 R >>\nstartxref\n"
        + str(xref_pos).encode()
        + b"\n%%EOF\n"
    )
    pdf_out.parent.mkdir(parents=True, exist_ok=True)
    pdf_out.write_bytes(b"".join(chunks + xref + [tail]))


def jpeg_from_raster(src: Path, jpeg_out: Path, max_long: int = 3508) -> None:
    im = Image.open(src).convert("RGB")
    w, h = im.size
    long = max(w, h)
    if long > max_long:
        s = max_long / long
        im = im.resize((max(1, int(w * s)), max(1, int(h * s))), Image.Resampling.LANCZOS)
        im = im.convert("L").point(lambda p: 0 if p < 160 else 255).convert("RGB")
    jpeg_out.parent.mkdir(parents=True, exist_ok=True)
    im.save(jpeg_out, "JPEG", quality=95, optimize=True, dpi=(300, 300))


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input", type=Path, help="Clean binary plate PNG")
    p.add_argument("svg", type=Path, help="SVG output (working file, not for ibon)")
    p.add_argument("--pdf", type=Path, help="Vector A4 PDF for ibon document print")
    p.add_argument("--jpeg", type=Path, help="Optional JPEG fallback for ibon image print")
    p.add_argument("--eps", type=float, default=0.85, help="RDP simplify epsilon")
    p.add_argument("--margin-mm", type=float, default=14.0)
    p.add_argument(
        "--orientation",
        choices=("auto", "portrait", "landscape"),
        default="auto",
    )
    args = p.parse_args()
    if not args.input.is_file():
        print(f"FAIL missing input: {args.input}", file=sys.stderr)
        return 2

    used_potrace = False
    loops = []
    src_w = src_h = 0
    if try_potrace(args.input, args.svg):
        used_potrace = True
        ink = load_ink(args.input)
        src_h, src_w = ink.shape
        # PDF still needs loops; trace python on the same ink so fill matches.
        src_w, src_h, loops = trace_python(ink, args.eps)
    else:
        ink = load_ink(args.input)
        src_w, src_h, loops = trace_python(ink, args.eps)
        args.svg.parent.mkdir(parents=True, exist_ok=True)
        args.svg.write_text(svg_from_loops(src_w, src_h, loops), encoding="utf-8")

    if not loops:
        print("FAIL no loops traced", file=sys.stderr)
        return 1

    print(
        f"SVG {args.svg.resolve()} loops={len(loops)} "
        f"engine={'potrace' if used_potrace else 'marching-squares'}"
    )

    if args.pdf:
        land = args.orientation == "landscape" or (
            args.orientation == "auto" and src_w > src_h * 1.08
        )
        pdf_from_loops(
            loops, src_w, src_h, args.pdf, landscape=land, margin_mm=args.margin_mm
        )
        print(f"VECTOR PDF {args.pdf.resolve()}")
    if args.jpeg:
        jpeg_from_raster(args.input, args.jpeg)
        print(f"JPEG {args.jpeg.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
