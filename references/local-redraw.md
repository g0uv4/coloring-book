# Local redraw — edit one region, keep the plate

When the user says 只改X、臈不要動、fix the cutting board only, do **not** regenerate the whole page from the photo alone.

## Inputs (required)

- `USER_PHOTO` — original photograph (identity of the named region)
- `CLEAN_PLATE` — last QC-SHIP plate (`plate-clean.png`)
- `REGION` — their words: board, vest, left glasses, faucet, cat tail…

If `CLEAN_PLATE` is missing, say so and stop. Do not start over from the photo only.

## Tool call

Use the **same host backend** as the first plate ([image-backend.md](image-backend.md)). Prefer image-to-image with two references when the tool allows it:

1. Structure / base = `CLEAN_PLATE` (keep every unmentioned line)
2. Identity = `USER_PHOTO` (only for the named region)

If the tool accepts only one image, edit `CLEAN_PLATE` and describe the region from the photo in text. Never attach a third-party coloring page.

## Prompt add-on

```
Edit ONLY this region of the existing coloring plate: {REGION}.
Keep every other outline identical — same faces, same poses, same line weight.
Rebuild {REGION} as closed medium-thick black loops with WHITE interiors,
matching the photograph’s silhouette of that object.
If {REGION} is dark in the photo (black fur, black shirt, dark wood), it still stays white inside.
Do not restyle the page. Do not add hatch. Do not invent new objects.
```

## After the edit (required)

```bash
python3 scripts/cleanup_lines.py plate-raw.png plate-clean.png --threshold 128 --min-long-edge 2400 --smooth 1.2
python3 scripts/qc_plate.py plate-clean.png --report qc-report.json
```

QC must pass the **fill / silhouette gates** and the broken-line gates. Overlay only on FAIL.

Then **attach the new `plate-clean.png` in chat**. Do not run vectorize / compose / `pipeline.py --pdf`. Do not say 「走管線」.

## Fail → retry once

If the model redraws the whole page, fills a region black, or changes a frozen face:

```
The previous plate is correct except {REGION}. Copy all other lines exactly.
Change only {REGION}. White interiors. No filled paint.
```

Second fail → show both plates, ask whether to keep the old one. No PDF.
