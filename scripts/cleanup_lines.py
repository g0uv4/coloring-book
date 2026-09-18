#!/usr/bin/env python3
"""Turn a generated coloring plate into pure black-on-white ink.

Upscale the grayscale plate first, then threshold. Thresholding a small
image and later stretching it onto A4 is what makes diagonal beams jagged.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    from PIL import Image, ImageFilter, ImageOps
except ImportError as exc:  # pragma: no cover
    raise SystemExit("Pillow is required: python -m pip install Pillow") from exc


def to_rgb(im: Image.Image) -> Image.Image:
    if im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info):
        bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
        rgba = im.convert("RGBA")
        bg.paste(rgba, mask=rgba.split()[-1])
        return bg.convert("RGB")
    return im.convert("RGB")


def cleanup(
    src: Path,
    dest: Path,
    *,
    threshold: int,
    min_long_edge: int,
    smooth: float,
) -> tuple[int, int]:
    gray = ImageOps.grayscale(to_rgb(Image.open(src)))
    gray = gray.filter(ImageFilter.MedianFilter(size=3))
    w, h = gray.size
    long_edge = max(w, h)
    if min_long_edge > 0 and long_edge < min_long_edge:
        scale = min_long_edge / long_edge
        gray = gray.resize(
            (max(1, int(round(w * scale))), max(1, int(round(h * scale)))),
            Image.Resampling.LANCZOS,
        )
    if smooth > 0:
        gray = gray.filter(ImageFilter.GaussianBlur(radius=float(smooth)))
    bw = gray.point(lambda p: 0 if p < threshold else 255, mode="L")
    rgb = Image.merge("RGB", (bw, bw, bw))
    dest.parent.mkdir(parents=True, exist_ok=True)
    rgb.save(dest, "PNG", optimize=True)
    return rgb.size


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--threshold", type=int, default=128)
    parser.add_argument(
        "--min-long-edge",
        type=int,
        default=3200,
        help="LANCZOS-upscale grayscale to this long edge before threshold. 0 = off.",
    )
    parser.add_argument(
        "--smooth",
        type=float,
        default=1.2,
        help="Gaussian radius on the upscaled gray plate before threshold. 0 = off.",
    )
    args = parser.parse_args()
    if not args.input.is_file():
        print(f"FAIL missing input: {args.input}", file=sys.stderr)
        return 2
    if not 16 <= args.threshold <= 240:
        print("FAIL threshold must be 16-240", file=sys.stderr)
        return 2
    if args.min_long_edge < 0 or args.min_long_edge > 8000:
        print("FAIL min-long-edge must be 0-8000", file=sys.stderr)
        return 2
    if args.smooth < 0 or args.smooth > 4:
        print("FAIL smooth must be 0-4", file=sys.stderr)
        return 2
    w, h = cleanup(
        args.input,
        args.output,
        threshold=args.threshold,
        min_long_edge=args.min_long_edge,
        smooth=args.smooth,
    )
    print(f"CLEAN {args.output.resolve()} {w}x{h}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
