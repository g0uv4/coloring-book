#!/usr/bin/env python3
"""Machine-check that an image is a colorable Open-Line Plate, not a photo.

Exit 0 on PASS, 1 on FAIL. Prints a JSON report either way.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    import numpy as np
    from PIL import Image
except ImportError as exc:  # pragma: no cover
    raise SystemExit("Pillow and numpy are required") from exc


def analyze(path: Path) -> dict:
    im = Image.open(path).convert("L")
    arr = np.asarray(im, dtype=np.uint8)
    n = int(arr.size)
    black = int((arr < 40).sum())
    white = int((arr > 220).sum())
    mid = n - black - white
    width, height = im.size
    return {
        "path": str(path.resolve()),
        "dimensions": [width, height],
        "mean_luma": round(float(arr.mean()), 2),
        "min_luma": int(arr.min()),
        "max_luma": int(arr.max()),
        "black_frac": round(black / n, 4),
        "white_frac": round(white / n, 4),
        "mid_frac": round(mid / n, 4),
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
    return fails


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    if not args.input.is_file():
        print(json.dumps({"ok": False, "fails": ["missing file"]}))
        return 1
    report = analyze(args.input)
    fails = judge(report)
    report["ok"] = len(fails) == 0
    report["fails"] = fails
    print(json.dumps(report, indent=2))
    if fails:
        print("VALIDATION FAIL: " + "; ".join(fails), file=sys.stderr)
        return 1
    print("VALIDATION PASS", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
