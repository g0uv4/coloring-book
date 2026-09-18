# A4 PDF spec

## Page

| | Portrait | Landscape |
|---|---|---|
| Size | 210 × 297 mm | 297 × 210 mm |
| Default | Portrait | Only when the plate is clearly wider than tall |
| Print raster | 300 dpi → 2480 × 3508 px | 3508 × 2480 px |
| Margins | 14 mm | same |
| Page color | `#FFFFFF` | same |

Artwork is **fitted** (never cropped, never stretched). Letterboxing stays white.

## Ink, not JPEG

The PDF page must be **1-bit CCITT** (Pillow `mode="1"`). Do not store the page as JPEG (`DCTDecode`). JPEG ringing is what looks like 鋸齒 on gantry beams when the user zooms or prints landscape.

Pipeline that keeps lines smooth:

1. `cleanup_lines.py` LANCZOS-upscales the **grayscale** plate to `--min-long-edge 3200`, optional `--smooth 1.2`, **then** thresholds.
2. `compose_a4_pdf.py` fits that plate into the A4 box, snaps back to black/white, writes a 1-bit PDF.

Never threshold a ~1200 px plate and then stretch it onto A4.

```bash
python3 scripts/cleanup_lines.py plate-raw.png plate-clean.png \
  --threshold 128 --min-long-edge 3200 --smooth 1.2
python3 scripts/compose_a4_pdf.py plate-clean.png plate-a4.pdf \
  --dpi 300 --margin-mm 14 --orientation auto --nup 1 \
  --preview plate-a4.png
```

## Chrome

Default: no page number, no logo on the artwork.
`--title` is a single black line in the bottom margin, only if asked.

## Print advice

Print at 100% on A4, no “fit to page” crop. Uncoated paper for crayons.
