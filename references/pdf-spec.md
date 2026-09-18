# A4 PDF spec

## Page

| | Portrait | Landscape |
|---|---|---|
| Size | 210 × 297 mm | 297 × 210 mm |
| Default | Portrait | Use when the plate is clearly wider than tall |
| Print raster | 300 dpi → 2480 × 3508 px (portrait) | 3508 × 2480 px |
| Margins | 14 mm on all sides | same |
| Page color | `#FFFFFF` | same |

The artwork is **fitted** (not cropped, not stretched) inside the margin box and centered. Letterboxing stays white.

## Chrome

Default: **no** page number, no logo, no "Inkplate" mark on the artwork.

Optional `--title` draws a single muted line in the bottom margin, outside the plate. Use only when the user asked for a title or a book name.

Never overlay text on the drawing.

## Script

```bash
python3 scripts/compose_a4_pdf.py plate-clean.png plate-a4.pdf \
  --dpi 300 --margin-mm 14 --orientation auto \
  --preview plate-a4.png
```

Success prints `DELIVERY PASS` and the PDF path.

## Print advice to the user (one line)

Print at 100% scale on A4, no "fit to page" crop, draft or normal quality is enough. Crayons prefer uncoated paper.

## Multi-page books

One plate per page, identical margins. Cover page only if the user asked for a book title.
