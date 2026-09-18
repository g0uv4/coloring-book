#!/usr/bin/env python3
"""Open-Line Plate QC inspector (machine half).

Hard rules:
  1. lines are continuous (few dangling skeleton endpoints)
  2. colorable regions are closed (crayon-sized gaps do not leak)

Extra gates: ink purity, region size, speckle, stroke thickness.

Exit 0 on QC PASS, 1 on QC FAIL. JSON on stdout.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image

NEIGH8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))


def load_ink(path: Path) -> tuple[np.ndarray, tuple[int, int]]:
    im = Image.open(path).convert("L")
    orig = im.size
    arr = np.asarray(im, dtype=np.uint8)
    return arr < 128, orig


def max_pool(mask: np.ndarray, factor: int) -> np.ndarray:
    if factor <= 1:
        return mask
    h, w = mask.shape
    h2, w2 = h // factor, w // factor
    if h2 < 8 or w2 < 8:
        return mask
    return mask[: h2 * factor, : w2 * factor].reshape(h2, factor, w2, factor).max(axis=(1, 3))


def dilate(mask: np.ndarray, times: int = 1) -> np.ndarray:
    out = mask
    for _ in range(times):
        p = np.pad(out, 1, constant_values=False)
        acc = p.copy()
        h, w = out.shape
        for dy, dx in NEIGH8:
            acc[1:-1, 1:-1] |= p[1 + dy : h + 1 + dy, 1 + dx : w + 1 + dx]
        out = acc[1:-1, 1:-1]
    return out


def erode4(mask: np.ndarray) -> np.ndarray:
    p = np.pad(mask, 1, constant_values=False)
    return (
        p[1:-1, 1:-1]
        & p[:-2, 1:-1]
        & p[2:, 1:-1]
        & p[1:-1, :-2]
        & p[1:-1, 2:]
    )


def neighbor_count(mask: np.ndarray) -> np.ndarray:
    p = np.pad(mask.astype(np.uint8), 1)
    h, w = mask.shape
    n = np.zeros((h, w), dtype=np.uint8)
    for dy, dx in NEIGH8:
        n += p[1 + dy : h + 1 + dy, 1 + dx : w + 1 + dx]
    return n


def zhang_suen(ink: np.ndarray, max_iter: int = 24) -> np.ndarray:
    img = ink.copy()
    h, w = img.shape
    for _ in range(max_iter):
        changed = False
        for step in (0, 1):
            p = np.pad(img, 1, constant_values=False)
            p2 = p[0:-2, 1:-1]
            p3 = p[0:-2, 2:]
            p4 = p[1:-1, 2:]
            p5 = p[2:, 2:]
            p6 = p[2:, 1:-1]
            p7 = p[2:, 0:-2]
            p8 = p[1:-1, 0:-2]
            p9 = p[0:-2, 0:-2]
            b = (
                p2.astype(np.uint8)
                + p3
                + p4
                + p5
                + p6
                + p7
                + p8
                + p9
            )
            a = (
                ((~p2) & p3).astype(np.uint8)
                + ((~p3) & p4)
                + ((~p4) & p5)
                + ((~p5) & p6)
                + ((~p6) & p7)
                + ((~p7) & p8)
                + ((~p8) & p9)
                + ((~p9) & p2)
            )
            if step == 0:
                cond = img & (b >= 2) & (b <= 6) & (a == 1) & (~(p2 & p4 & p6)) & (~(p4 & p6 & p8))
            else:
                cond = img & (b >= 2) & (b <= 6) & (a == 1) & (~(p2 & p4 & p8)) & (~(p2 & p6 & p8))
            if cond.any():
                img = img & ~cond
                changed = True
        if not changed:
            break
    return img


def label_bool(mask: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    h, w = mask.shape
    labels = np.zeros((h, w), dtype=np.int32)
    parent: list[int] = [0]

    def find(a: int) -> int:
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    next_id = 1
    for y in range(h):
        row = mask[y]
        prow = labels[y - 1] if y else None
        crow = labels[y]
        for x in range(w):
            if not row[x]:
                continue
            left = crow[x - 1] if x else 0
            up = prow[x] if prow is not None else 0
            if left and up:
                crow[x] = left
                ra, rb = find(left), find(up)
                if ra != rb:
                    parent[rb] = ra
            elif left:
                crow[x] = left
            elif up:
                crow[x] = up
            else:
                parent.append(next_id)
                crow[x] = next_id
                next_id += 1

    if next_id == 1:
        return labels, np.zeros(1, dtype=np.int32)

    remap = np.zeros(len(parent), dtype=np.int32)
    running = 1
    for i in range(1, len(parent)):
        r = i
        while parent[r] != r:
            r = parent[r]
        if remap[r] == 0:
            remap[r] = running
            running += 1
        remap[i] = remap[r]

    mapped = remap[labels.ravel()]
    labels = mapped.reshape(h, w)
    areas = np.bincount(mapped, minlength=running)
    areas[0] = 0
    return labels, areas


def analyze(path: Path) -> dict:
    im = Image.open(path).convert("L")
    full = np.asarray(im, dtype=np.uint8)
    n = int(full.size)
    black = int((full < 40).sum())
    white = int((full > 220).sum())
    mid = n - black - white
    width, height = im.size

    ink_full, _orig = load_ink(path)
    factor = 2 if max(ink_full.shape) >= 900 else 1
    ink = max_pool(ink_full, factor)
    h, w = ink.shape
    ink_frac = float(ink.mean())

    skel = zhang_suen(ink)
    ncount = neighbor_count(skel)
    end_mask = skel & (ncount == 1)
    iso_mask = skel & (ncount == 0)
    skel_px = int(skel.sum())
    end_px = int(end_mask.sum())
    iso_px = int(iso_mask.sum())
    end_rate = (end_px / skel_px) if skel_px else 1.0

    min_region = max(30, int(0.0002 * h * w))
    lab0, areas0 = label_bool(~ink)
    bg_id = int(np.argmax(areas0)) if areas0.size > 1 else 0
    bg0 = lab0 == bg_id if bg_id else np.zeros_like(ink)

    sealed = dilate(ink, times=3)
    lab1, areas1 = label_bool(~sealed)
    bg_id1 = int(np.argmax(areas1)) if areas1.size > 1 else 0
    rescued = (~sealed) & bg0 & (lab1 != bg_id1) if bg_id1 else np.zeros_like(ink)
    _lab_r, areas_r = label_bool(rescued)
    leak_pockets = int((areas_r[1:] >= min_region).sum()) if areas_r.size > 1 else 0
    leak_mask = rescued

    interior = [int(a) for a in areas0[1:] if a >= min_region]
    if interior:
        interior.sort(reverse=True)
        colorable = interior[1:]  # drop background
    else:
        colorable = []

    tiny_white = int(((areas0[1:] > 0) & (areas0[1:] < min_region)).sum()) if areas0.size > 1 else 0
    _blab, b_areas = label_bool(ink)
    speckle = int(((b_areas[1:] > 0) & (b_areas[1:] < 5)).sum()) if b_areas.size > 1 else 0

    remain = float(erode4(ink).sum()) / float(ink.sum()) if ink.sum() else 0.0

    return {
        "path": str(path.resolve()),
        "dimensions": [width, height],
        "qc_scale": [w, h],
        "mean_luma": round(float(full.mean()), 2),
        "min_luma": int(full.min()),
        "max_luma": int(full.max()),
        "black_frac": round(black / n, 4),
        "white_frac": round(white / n, 4),
        "mid_frac": round(mid / n, 4),
        "ink_frac_qc": round(ink_frac, 4),
        "skeleton_px": skel_px,
        "endpoints": end_px,
        "isolated_ink": iso_px,
        "endpoint_rate": round(end_rate, 4),
        "leak_pockets": leak_pockets,
        "tiny_white_specks": tiny_white,
        "ink_specks": speckle,
        "stroke_remain_after_erode": round(remain, 4),
        "colorable_regions": len(colorable),
        "median_region_px": int(np.median(colorable)) if colorable else 0,
        "smallest_colorable_px": min(colorable) if colorable else 0,
        "_end_mask": end_mask,
        "_iso_mask": iso_mask,
        "_leak_mask": leak_mask,
        "_ink": ink,
    }


def judge(report: dict) -> list[str]:
    fails: list[str] = []
    w, h = report["dimensions"]
    if w < 400 or h < 400:
        fails.append("image too small for print")
    if report["white_frac"] < 0.50:
        fails.append("not enough paper-white area to color")
    if report["black_frac"] < 0.012:
        fails.append("almost no ink — generation likely failed")
    if report["black_frac"] > 0.32:
        fails.append("too much solid black — hair/clothes may be filled")
    if report["mid_frac"] > 0.18:
        fails.append("too much gray — looks like a sketch or photo, not a plate")
    if report["mean_luma"] < 170:
        fails.append("overall too dark for a coloring page")
    if report["max_luma"] < 230:
        fails.append("background is not paper white")

    if report["endpoint_rate"] > 0.085 and report["endpoints"] > 90:
        fails.append(
            f"broken lines — {report['endpoints']} dangling ends "
            f"(rate {report['endpoint_rate']:.1%} of skeleton)"
        )
    elif report["endpoints"] > 420:
        fails.append(f"too many dangling ends ({report['endpoints']}) — lines look dashed")

    if report["leak_pockets"] > 10:
        fails.append(
            f"unclosed regions — {report['leak_pockets']} pockets leak through crayon-sized gaps"
        )

    if report["colorable_regions"] < 3:
        fails.append("almost no enclosed colorable pockets")
    if report["ink_specks"] > 120:
        fails.append(f"ink speckle / dirt ({report['ink_specks']} tiny black islands)")
    if report["stroke_remain_after_erode"] < 0.22 and report["black_frac"] > 0.02:
        fails.append("strokes are hairline — they will break or vanish in print")
    if report["tiny_white_specks"] > 400:
        fails.append("too many uncolorable pinholes")
    return fails


def save_overlay(dest: Path, report: dict) -> None:
    ink = report["_ink"]
    rgb = np.stack([np.where(ink, 28, 255)] * 3, axis=-1).astype(np.uint8)
    leak = dilate(report["_leak_mask"], times=1)
    rgb[leak] = (232, 140, 32)
    mark = dilate(report["_end_mask"] | report["_iso_mask"], times=2)
    rgb[mark] = (200, 32, 32)
    Image.fromarray(rgb, "RGB").save(dest, "PNG")


def public_report(report: dict, fails: list[str]) -> dict:
    return {k: v for k, v in report.items() if not k.startswith("_")} | {
        "ok": len(fails) == 0,
        "fails": fails,
        "legend": {
            "overlay_red": "dangling line ends / isolated ink",
            "overlay_orange": "regions that only close after sealing crayon-sized gaps",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--overlay", type=Path, help="PNG with dangling ends (red) and leaks (orange)")
    parser.add_argument("--report", type=Path, help="Write JSON report")
    args = parser.parse_args()
    if not args.input.is_file():
        print(json.dumps({"ok": False, "fails": ["missing file"]}))
        return 1
    report = analyze(args.input)
    fails = judge(report)
    out = public_report(report, fails)
    text = json.dumps(out, indent=2)
    print(text)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(text + "\n")
    if args.overlay:
        args.overlay.parent.mkdir(parents=True, exist_ok=True)
        save_overlay(args.overlay, report)
        print(f"OVERLAY {args.overlay.resolve()}", file=sys.stderr)
    if fails:
        print("QC FAIL: " + "; ".join(fails), file=sys.stderr)
        return 1
    print("QC PASS", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
