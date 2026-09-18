#!/usr/bin/env python3
"""Place a coloring plate onto a print-ready A4 PDF (and optional PNG preview).

The plate is fitted inside printer-safe margins on a pure white page.
Nothing in the artwork is redrawn. Optional title sits in the bottom margin.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError as exc:  # pragma: no cover
    raise SystemExit("Pillow is required: python -m pip install Pillow") from exc

A4_PORTRAIT_MM = (210.0, 297.0)
A4_LANDSCAPE_MM = (297.0, 210.0)


def mm_to_px(mm: float, dpi: int) -> int:
    return int(round(mm / 25.4 * dpi))


def fit_inside(src_w: int, src_h: int, box_w: int, box_h: int) -> tuple[int, int]:
    scale = min(box_w / src_w, box_h / src_h)
    return max(1, int(src_w * scale)), max(1, int(src_h * scale))


def load_font(size: int) -> ImageFont.ImageFont:
    for name in (
        "DejaVuSans.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ):
        try:
            return ImageFont.truetype(name, size=size)
        except OSError:
            continue
    return ImageFont.load_default()


def compose(
    src: Path,
    pdf_out: Path,
    *,
    dpi: int,
    margin_mm: float,
    title: str | None,
    force: str,
    preview: Path | None,
) -> None:
    art = Image.open(src).convert("RGB")
    art_w, art_h = art.size
    landscape = force == "landscape" or (force == "auto" and art_w > art_h * 1.08)
    page_mm = A4_LANDSCAPE_MM if landscape else A4_PORTRAIT_MM
    page_w = mm_to_px(page_mm[0], dpi)
    page_h = mm_to_px(page_mm[1], dpi)
    margin = mm_to_px(margin_mm, dpi)
    title_band = mm_to_px(8.0, dpi) if title else 0

    box_w = page_w - margin * 2
    box_h = page_h - margin * 2 - title_band
    fit_w, fit_h = fit_inside(art_w, art_h, box_w, box_h)
    fitted = art.resize((fit_w, fit_h), Image.Resampling.LANCZOS)

    page = Image.new("RGB", (page_w, page_h), (255, 255, 255))
    x = (page_w - fit_w) // 2
    y = margin + (box_h - fit_h) // 2
    page.paste(fitted, (x, y))

    if title:
        draw = ImageDraw.Draw(page)
        font = load_font(max(14, mm_to_px(3.2, dpi)))
        text = title.strip()[:80]
        bbox = draw.textbbox((0, 0), text, font=font)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        tx = (page_w - tw) // 2
        ty = page_h - margin - title_band + (title_band - th) // 2
        draw.text((tx, ty), text, fill=(90, 86, 80), font=font)

    pdf_out.parent.mkdir(parents=True, exist_ok=True)
    page.save(pdf_out, "PDF", resolution=float(dpi))
    if preview is not None:
        preview.parent.mkdir(parents=True, exist_ok=True)
        page.save(preview, "PNG", optimize=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Clean coloring-plate PNG")
    parser.add_argument("output", type=Path, help="A4 PDF path")
    parser.add_argument("--title", default="", help="Optional footer title")
    parser.add_argument("--dpi", type=int, default=300)
    parser.add_argument("--margin-mm", type=float, default=14.0)
    parser.add_argument(
        "--orientation",
        choices=("auto", "portrait", "landscape"),
        default="auto",
    )
    parser.add_argument("--preview", type=Path, default=None, help="Optional A4 PNG")
    args = parser.parse_args()
    if not args.input.is_file():
        print(f"FAIL missing input: {args.input}", file=sys.stderr)
        return 2
    if args.dpi < 72 or args.dpi > 600:
        print("FAIL dpi must be 72-600", file=sys.stderr)
        return 2
    compose(
        args.input,
        args.output,
        dpi=args.dpi,
        margin_mm=args.margin_mm,
        title=args.title or None,
        force=args.orientation,
        preview=args.preview,
    )
    print(f"DELIVERY PASS {args.output.resolve()}")
    if args.preview:
        print(f"PREVIEW {args.preview.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
