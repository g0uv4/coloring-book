# Local redraw — edit one region, keep the plate

When the user says 只改X、臉不要動、fix the cutting board only, do **not** regenerate the whole page from the photo alone.

## Inputs

- `USER_PHOTO` — original photograph (identity)
- `CLEAN_PLATE` — last QC-SHIP plate (`plate-clean.png`)
- `REGION` — their words: board, vest, left glasses, faucet…

## Tool call

`imagine_image_to_image` with **two** images if the tool allows a content image plus a structure image:

1. IMAGE content = `CLEAN_PLATE` (keep every unmentioned line)
2. IMAGE reference = `USER_PHOTO` (only for the named region’s identity)

If the tool accepts only one image, pass `CLEAN_PLATE` as the edit source and describe the region from the photo in text. Do **not** pass a third-party coloring page.

## Prompt add-on (append, keep Open-Line Plate lock)

```
Edit ONLY this region of the existing coloring plate: {REGION}.
Keep every other outline identical — same faces, same poses, same line weight.
Rebuild {REGION} as closed medium-thick black loops with white interiors,
matching the photograph’s silhouette of that object.
Do not restyle the page. Do not add hatch. Do not invent new objects.
```

Then run `cleanup_lines.py` and `qc_plate.py --kind {KIND}` on the new file. Preview again. PDF still waits for confirm.

## Fail → retry once

If the model redraws the whole page or changes a face you were told to freeze:

```
The previous plate is correct except {REGION}. Copy all other lines exactly.
Change only {REGION}.
```

Second fail → show both plates, ask whether to keep the old one.
