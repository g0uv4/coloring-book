#!/usr/bin/env python3
"""Turn a generated coloring plate into pure black-on-white ink.

JPEG/model output often carries light gray shading and compression haze.
This script keeps only dark ink and blows everything else to paper white.
It never invents new lines.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    from PIL import Image, ImageFilter, ImageOps
except ImportError as exc:  # pragma: no cover
    raise SystemExit("Pillow is required: python -m pip install Pillow") from exc


def cleanup(src: Path, dest: Path, threshold: int) -> None:
    im = Image.open(src)
    if im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info):
        bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
        rgba = im.convert("RGBA")
        bg.paste(rgba, mask=rgba.split()[-1])
        im = bg.convert("RGB")
    else:
        im = im.convert("RGB")

    gray = ImageOps.grayscale(im)
    gray = gray.filter(ImageFilter.MedianFilter(size=3))
    bw = gray.point(lambda p: 0 if p < threshold else 255, mode="L")
    rgb = Image.merge("RGB", (bw, bw, bw))
    dest.parent.mkdir(parents=True, exist_ok=True)
    rgb.save(dest, "PNG", optimize=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument(
        "--threshold",
        type=int,
        default=128,
        help="Pixels darker than this become ink (0-255). Default 128.",
    )
    args = parser.parse_args()
    if not args.input.is_file():
        print(f"FAIL missing input: {args.input}", file=sys.stderr)
        return 2
    if not 16 <= args.threshold <= 240:
        print("FAIL threshold must be 16-240", file=sys.stderr)
        return 2
    cleanup(args.input, args.output, args.threshold)
    print(f"CLEAN {args.output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
