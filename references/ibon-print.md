# 7-11 ibon print

Goal: one A4 coloring page the kiosk will print without jaggies or a clipped border.

## What to hand the machine

| File | ibon | Use |
|---|---|---|
| **A4 PDF, no password, not zipped** | 文件列印 | **Primary.** Vector PDF from `vectorize_plate.py --pdf` |
| JPEG | 圖片列印 or 文件列印 | Fallback only. Line art + JPEG ringing looks dirty |
| PNG | some cloud paths | OK, PDF is stabler |
| **SVG** | **not accepted** | Working file only. Never upload SVG to ibon |

Cloud upload ~15–30 MB per file. Email is tighter (~10 MB). Do not encrypt.

## Paper at the kiosk

- Size: **A4**
- Mode: **黑白**
- Paper: **一般用紙** (about NT$3). Do not pick photo paper.
- Scale: **100% / 實際大小**. Never 「符合紙張」.
- ibon printable area is about **20.2 × 28.3 cm**. The skill’s 14 mm margin keeps ink off the gripper.

Do not use 4×6 photo print for these plates (that path wants JPG and is the wrong paper).

## Pipeline

```text
photo → Open-Line Plate (raster)
     → cleanup (gray upscale, then threshold)
     → QC (closed + smooth)
     → vectorize_plate.py → SVG (work) + vector A4 PDF (ibon)
     → optional JPEG fallback
```

If `vectorize_plate.py` fails, fall back to `compose_a4_pdf.py` (1-bit raster PDF). Still do not give ibon an SVG.

```bash
python3 scripts/vectorize_plate.py plate-clean.png plate.svg \
  --pdf plate-a4.pdf --jpeg plate-a4.jpg \
  --orientation portrait --margin-mm 14
```
