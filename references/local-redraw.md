# Local redraw — edit one region, keep the plate

When the user says 只改X / 只改某一塊 / 其他不要動, do **not** regenerate the whole page from the photo alone. Do **not** send the full plate to the image tool.

## Inputs (required)

- `USER_PHOTO` — original photograph. Text, or a second reference. Never the image being edited.
- `CLEAN_PLATE` — last QC-SHIP plate (`plate-clean.png`)
- `REGION` — their words: board, vest, left glasses, faucet, cat tail…

If `CLEAN_PLATE` is missing, say so and stop. Do not start over from the photo only.

## Crop

Look at `plate-clean.png`. Pick `--region x,y,w,h` in plate pixels (top-left origin, half-open `[x, x+w) × [y, y+h)`). `--pad N` is extra context; paste discards that ring.

```bash
python3 scripts/region_edit.py crop plate-clean.png plate-region.png --region x,y,w,h --pad N
```

Send **only** `plate-region.png` to the same host image tool as the first plate ([image-backend.md](image-backend.md)). Save the return as `plate-region-raw.png`. Do not scale it.

## Prompt add-on

```
This file is one crop of a coloring plate, not the full page.
Redraw the crop as closed medium-thick black loops with white interiors.
Rebuild only {REGION}. Dark photo areas stay white inside.
Do not add a border, caption, or letterbox.
Do not hatch. Do not invent objects.
```

## Paste, then QC

```bash
python3 scripts/region_edit.py paste plate-clean.png plate-clean.png --region x,y,w,h --pad N --raw plate-region-raw.png
python3 scripts/qc_plate.py plate-clean.png --report qc-report.json
```

Same `--region` and `--pad` as crop. Paste writes only the named box. Do **not** run `cleanup_lines.py` on the full plate during this turn.

QC must pass the **fill / silhouette gates** and the broken-line gates. Overlay only on FAIL.

Then **attach the new `plate-clean.png` in chat**. Do not run vectorize / compose / `pipeline.py --pdf`. Do not say 「走管線」.

## Fail → retry once

If paste exits 2, keep the old plate and retry the host once.

If QC fails, retry the host once on the same crop. Do not run `cleanup_lines.py` on the full plate.

Second fail → show both, no PDF.
