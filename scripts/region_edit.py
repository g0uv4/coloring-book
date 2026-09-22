#!/usr/bin/env python3
"""Crop one plate region for a host redraw, then paste only that box back."""
from __future__ import annotations

import argparse
import contextlib
import io
import os
import sys
import tempfile
from pathlib import Path

import numpy as np
from PIL import Image

from cleanup_lines import cleanup, to_rgb


def parse_region(text: str) -> tuple[int, int, int, int]:
    parts = text.split(",")
    if len(parts) != 4:
        raise ValueError("region must be x,y,w,h")
    try:
        x, y, w, h = (int(part) for part in parts)
    except ValueError as exc:
        raise ValueError("region must be x,y,w,h") from exc
    return x, y, w, h


def padded_context(
    plate_size: tuple[int, int],
    region: tuple[int, int, int, int],
    pad: int,
) -> tuple[tuple[int, int, int, int], tuple[int, int]]:
    plate_w, plate_h = plate_size
    x, y, w, h = region
    if pad < 0 or w < 1 or h < 1:
        raise ValueError("bad region or pad")
    if x < 0 or y < 0 or x + w > plate_w or y + h > plate_h:
        raise ValueError("region outside plate")
    left = max(0, x - pad)
    top = max(0, y - pad)
    right = min(plate_w, x + w + pad)
    bottom = min(plate_h, y + h + pad)
    context = (left, top, right - left, bottom - top)
    if context[2] == plate_w and context[3] == plate_h:
        raise ValueError("padded crop equals the full plate")
    return context, (x - left, y - top)


def load_rgb(path: Path) -> Image.Image:
    with Image.open(path) as im:
        rgb = to_rgb(im)
        rgb.load()
        return rgb


def publish_png(out: Path, arr: np.ndarray) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix="region-edit-", suffix=".png", dir=out.parent)
    os.close(fd)
    tmp = Path(name)
    try:
        Image.fromarray(np.ascontiguousarray(arr), mode="RGB").save(tmp, "PNG")
        os.replace(tmp, out)
    finally:
        if tmp.exists():
            tmp.unlink()


def crop_region(
    plate: Path,
    out: Path,
    region: tuple[int, int, int, int],
    pad: int,
) -> int:
    if not plate.is_file():
        print(f"FAIL missing plate: {plate}", file=sys.stderr)
        return 2
    try:
        im = load_rgb(plate)
    except OSError as exc:
        print(f"FAIL {exc}", file=sys.stderr)
        return 2
    try:
        (left, top, cw, ch), (ix, iy) = padded_context(im.size, region, pad)
    except ValueError as exc:
        print(f"FAIL {exc}", file=sys.stderr)
        return 2
    tile = im.crop((left, top, left + cw, top + ch))
    out.parent.mkdir(parents=True, exist_ok=True)
    tile.save(out, "PNG")
    x, y, w, h = region
    print(
        f"CROP {out} context={left},{top},{cw},{ch} inner={ix},{iy} "
        f"named={x},{y},{w},{h} plate={im.size[0]} x {im.size[1]}"
    )
    return 0


def paste_region(
    plate: Path,
    out: Path,
    region: tuple[int, int, int, int],
    pad: int,
    raw: Path,
) -> int:
    if not plate.is_file():
        print(f"FAIL missing plate: {plate}", file=sys.stderr)
        return 2
    if not raw.is_file():
        print(f"FAIL missing raw: {raw}", file=sys.stderr)
        return 2
    try:
        base_im = load_rgb(plate)
    except OSError as exc:
        print(f"FAIL {exc}", file=sys.stderr)
        return 2
    try:
        context, (ix, iy) = padded_context(base_im.size, region, pad)
    except ValueError as exc:
        print(f"FAIL {exc}", file=sys.stderr)
        return 2
    cw, ch = context[2], context[3]
    try:
        with Image.open(raw) as raw_im:
            raw_size = raw_im.size
    except OSError as exc:
        print(f"FAIL {exc}", file=sys.stderr)
        return 2
    if raw_size != (cw, ch):
        print(
            f"FAIL raw size {raw_size[0]}x{raw_size[1]} != context {cw}x{ch}",
            file=sys.stderr,
        )
        return 2

    with tempfile.TemporaryDirectory() as td:
        cleaned_path = Path(td) / "cleaned.png"
        cleaned_size = cleanup(
            raw,
            cleaned_path,
            threshold=128,
            min_long_edge=0,
            smooth=1.2,
        )
        if cleaned_size != (cw, ch):
            print("FAIL cleaned size != context", file=sys.stderr)
            return 1
        with Image.open(cleaned_path) as cleaned_im:
            cleaned = np.array(to_rgb(cleaned_im), dtype=np.uint8)
            cleaned = np.copy(cleaned)

    x, y, w, h = region
    base = np.array(base_im, dtype=np.uint8)
    base = np.copy(base)
    if base.dtype != np.uint8 or base.ndim != 3 or base.shape[2] != 3:
        print("FAIL plate is not uint8 RGB", file=sys.stderr)
        return 1
    if cleaned.shape != (ch, cw, 3) or cleaned.dtype != np.uint8:
        print("FAIL cleaned tile is not uint8 RGB", file=sys.stderr)
        return 1
    tile = cleaned[iy : iy + h, ix : ix + w]
    if tile.shape != (h, w, 3):
        print("FAIL inner tile shape", file=sys.stderr)
        return 1
    out_arr = base.copy()
    out_arr[y : y + h, x : x + w] = tile
    plate_h, plate_w = base.shape[:2]
    if out_arr.dtype != np.uint8 or out_arr.shape != (plate_h, plate_w, 3):
        print("FAIL result is not uint8 RGB", file=sys.stderr)
        return 1
    outside = np.ones((plate_h, plate_w), dtype=bool)
    outside[y : y + h, x : x + w] = False
    if not np.array_equal(out_arr[outside], base[outside]):
        print("FAIL pixels outside the named box changed", file=sys.stderr)
        return 1

    publish_png(out, out_arr)
    print(f"PASTE {out} {plate_w}x{plate_h} outside=identical")
    return 0


def self_check() -> int:
    def invoke(argv: list[str]) -> tuple[int, str, str]:
        stdout, stderr = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            code = main(argv)
        return code, stdout.getvalue().strip(), stderr.getvalue().strip()

    def fail(msg: str) -> int:
        print(f"FAIL {msg}", file=sys.stderr)
        return 1

    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        plate_path = root / "plate.png"
        plate = Image.new("RGB", (20, 16), (255, 255, 255))
        pix = plate.load()
        for y in range(4, 8):
            for x in range(4, 10):
                pix[x, y] = (0, 0, 0)
        plate.save(plate_path, "PNG")

        crop_path = root / "crop.png"
        code, text, err = invoke(
            ["crop", str(plate_path), str(crop_path), "--region", "4,4,6,4", "--pad", "2"]
        )
        expect = (
            f"CROP {crop_path} context=2,2,10,8 inner=2,2 "
            f"named=4,4,6,4 plate=20 x 16"
        )
        if code != 0 or text != expect or not crop_path.is_file():
            return fail(f"crop {code} {text!r} {err}")

        with Image.open(crop_path) as crop_im:
            raw = to_rgb(crop_im)
            raw.load()
        if raw.size != (10, 8):
            return fail(f"crop size {raw.size}")
        raw_px = raw.load()
        for y in range(2, 6):
            for x in range(2, 8):
                raw_px[x, y] = (255, 255, 255)
        raw_path = root / "raw.png"
        raw.save(raw_path, "PNG")

        out_path = root / "out.png"
        code, text, err = invoke(
            [
                "paste",
                str(plate_path),
                str(out_path),
                "--region",
                "4,4,6,4",
                "--pad",
                "2",
                "--raw",
                str(raw_path),
            ]
        )
        if code != 0 or text != f"PASTE {out_path} 20x16 outside=identical":
            return fail(f"paste {code} {text!r} {err}")
        with Image.open(plate_path) as im:
            orig = np.array(to_rgb(im), dtype=np.uint8)
        with Image.open(out_path) as im:
            got = np.array(to_rgb(im), dtype=np.uint8)
        if got.dtype != np.uint8 or got.shape != (16, 20, 3):
            return fail(f"result {got.dtype} {got.shape}")
        outside = np.ones((16, 20), dtype=bool)
        outside[4:8, 4:10] = False
        if not np.array_equal(got[outside], orig[outside]):
            return fail("outside changed")
        if np.array_equal(got[4:8, 4:10], orig[4:8, 4:10]):
            return fail("inside unchanged")

        bad_raw = root / "bad-raw.png"
        Image.new("RGB", (20, 16), (255, 255, 255)).save(bad_raw, "PNG")
        bad_out = root / "bad-out.png"
        bad_out.write_bytes(b"keep-size")
        code, text, err = invoke(
            [
                "paste",
                str(plate_path),
                str(bad_out),
                "--region",
                "4,4,6,4",
                "--pad",
                "2",
                "--raw",
                str(bad_raw),
            ]
        )
        if code != 2 or text or bad_out.read_bytes() != b"keep-size":
            return fail(f"size reject code={code} {text!r} {err}")

        full_out = root / "full.png"
        full_out.write_bytes(b"keep-full")
        code, text, err = invoke(
            ["crop", str(plate_path), str(full_out), "--region", "4,4,6,4", "--pad", "20"]
        )
        if code != 2 or text or full_out.read_bytes() != b"keep-full":
            return fail(f"full plate code={code} {text!r} {err}")

        clamp_out = root / "clamp.png"
        code, text, err = invoke(
            ["crop", str(plate_path), str(clamp_out), "--region", "1,2,6,4", "--pad", "4"]
        )
        expect = (
            f"CROP {clamp_out} context=0,0,11,10 inner=1,2 "
            f"named=1,2,6,4 plate=20 x 16"
        )
        if code != 0 or text != expect:
            return fail(f"clamp {code} {text!r} {err}")

    print("SELF-CHECK PASS")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-check", action="store_true")
    sub = parser.add_subparsers(dest="cmd", required=False)

    def add_common(cmd: str) -> argparse.ArgumentParser:
        subparser = sub.add_parser(cmd)
        subparser.add_argument("plate", type=Path)
        subparser.add_argument("out", type=Path)
        subparser.add_argument("--region", required=True)
        subparser.add_argument("--pad", type=int, required=True)
        return subparser

    add_common("crop")
    paste = add_common("paste")
    paste.add_argument("--raw", type=Path, required=True)

    args = parser.parse_args(argv)
    if args.self_check:
        return self_check()
    if args.cmd not in ("crop", "paste"):
        parser.print_usage(sys.stderr)
        return 2
    try:
        region = parse_region(args.region)
    except ValueError as exc:
        print(f"FAIL {exc}", file=sys.stderr)
        return 2
    if args.cmd == "crop":
        return crop_region(args.plate, args.out, region, args.pad)
    return paste_region(args.plate, args.out, region, args.pad, args.raw)


if __name__ == "__main__":
    raise SystemExit(main())
