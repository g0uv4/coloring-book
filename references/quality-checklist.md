# Quality checklist

A plate is shown only when the **QC inspector** signs **SHIP**. An A4 PDF is composed only after the **user confirms**. Full SOP: [qc-inspector.md](qc-inspector.md).

## Machine (`scripts/qc_plate.py`)

Must print `QC PASS`.

- Paper white vs ink vs leftover gray
- Dangling skeleton ends (broken / dashed lines)
- Leak pockets (regions that only close after sealing a crayon-sized gap)
- Colorable region count
- Ink speckle
- Stroke thickness (hairline fails)
- Uncolorable pinholes

Optional overlay: red = dangling ends, orange = leaks.

`validate_coloring.py` is the older luma-only subset. Shipping uses `qc_plate.py`.

## Visual (mandatory, you look at the PNG)

- Every stroke continuous; every color pocket closed
- Reads as a coloring book at thumbnail size
- Not a grayscale photograph / not an edge-detected tracing
- Faces follow the portrait recipe (if any)
- Hair/clothes interiors are white, not filled black
- Distinctive photo facts are still there (count, glasses, pose)
- No extra people or landmarks
- No watermark, no garbled letters unless the source had a sign you translated into outline letters
- Line weight even
- Intensity matches the request (advanced ≠ denser hatch)
- Effects match the photo silhouette, not clip-art flames

## PDF (only after the user says yes)

- User confirmed the plate (or requested edits were done and they confirmed again)
- `DELIVERY PASS`
- Artwork not cropped
- Artwork not rotated wrongly
- Margins exist (not bleeding off the paper)

## Common fails → one retry

Use the add-ons in [qc-inspector.md](qc-inspector.md).
