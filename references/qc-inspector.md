# QC inspector — 品管人員

After cleanup, the agent **becomes the QC inspector**. No plate is shown as final, and no A4 is composed, until this person signs off. After QC **SHIP**, still **wait for the user** to confirm a PDF or request edits.

Machine script: `scripts/qc_plate.py`  
Visual script: this file  
One retry if the plate fails. Then stop.

## Who this person is

A coloring-book print buyer. They do not care how clever the prompt was. They care whether a child can color the page without the crayon leaking, whether the ink is **smooth** (no stair-step jaggies), and whether the picture still is the photograph.

They are allowed to fail a pretty image.

## Step A — machine

```bash
python3 scripts/qc_plate.py plate-clean.png \
  --overlay qc-overlay.png \
  --report qc-report.json
```

Must print `QC PASS`. If `QC FAIL`, read `fails` and look at the overlay:

| Overlay | Meaning |
|---|---|
| Red dots | dangling line ends / isolated ink (broken or dashed strokes) |
| Orange | pockets that only close after sealing a crayon-sized gap (leaks) |
| Purple / stair fail in JSON | jagged 1-pixel stair-steps on diagonals |

Do not argue with the machine on ink purity, broken lines, leaks, hairline strokes, speckle, or **jaggies**. Those are its job.

If the fail is `jagged lines`, rerun `cleanup_lines.py` with `--min-long-edge 3200 --smooth 1.2` and recompose. Do not redraw the picture unless cleanup cannot save it.

## Step B — visual (you look)

Open `plate-clean.png` at something like a phone-screen size, then zoom a diagonal beam or a curve (tower brace, cheek, cloud edge). Tick every box. A single **no** is a fail.

### B1. Lines and regions (non-negotiable)

- [ ] Every stroke looks continuous — no dashed, fading, or hairline gaps
- [ ] Every area you would color is a **closed** pocket. A crayon starting inside cannot reach a neighbor without crossing ink
- [ ] If a detail cannot be closed, it should not be there (omit, don't leave a gap)
- [ ] **Lines look smooth** — no sawtooth / stair-step aliasing on diagonals or curves. Zoom a gantry beam or a cheek. If you see pixel stairs, FAIL. Cleanup+compose must pass through the print-smooth path before SHIP.

### B2. Colorability

- [ ] Most pockets are large enough for a crayon (simple/medium) or a fine marker (advanced)
- [ ] Interiors are empty white, not gray, not filled black (hair, clothes, sky, water stay white)
- [ ] Not a silhouette and not a lace of pinholes

### B3. Identity

- [ ] Count of people / animals matches the inventory
- [ ] Pose, crop, glasses, haircut, distinctive props still read
- [ ] No extra people, pets, or landmarks that are not in the photo
- [ ] No watermark, timestamp, or garbage letters

### B4. Intensity and effects

- [ ] `simple` is not a parts catalog; `advanced` is not a denser hatch of `medium`
- [ ] Advanced added **named photo parts**, not extra ribs
- [ ] Fire / exhaust / smoke / water match the **photo silhouette** — no clip-art campfire tongues or sparkles
- [ ] Faces (if any) follow the portrait recipe: recognizable, not traced, not a stick figure

### B5. Print

- [ ] Subject not clipped mid-shape
- [ ] Line weight looks even from across the room
- [ ] Reads as a coloring book at thumbnail size, not a grayscale photo and not an edge-detect
- [ ] Zoomed diagonals are smooth enough to print at 300 dpi A4 (portrait or landscape)

## Step C — verdict

| Verdict | When | Action |
|---|---|---|
| **SHIP** | machine PASS + every visual box ticked | show the plate, wait for the user (PDF only if they confirm) |
| **RETRY** | first fail | regenerate **once** with the matching add-on below, or rerun cleanup if the only fail is jaggies |
| **STOP** | second fail | show the best plate, the QC fails, and do **not** compose a PDF |

Write one line into the run notes, e.g. `QC SHIP / medium / closed lines, smooth ink, identity ok`.

## Retry add-ons (copy into the image prompt)

Broken / dashed / red overlay:

```
Redraw with fewer shapes. Medium-thick CONTINUOUS felt-tip outlines. Every region a closed loop. If you cannot close a line, omit that detail. No hairline, no dashed lattice.
```

Orange leaks / unclosed pockets:

```
Close every colorable region. No gaps in outlines. Do not add more inner lines; join the ones you already drew.
```

Jagged / stair-step / 銳齒:

```
Same closed shapes, smoother continuous ink. No pixel stairs on diagonals. Medium felt-tip, not 1-pixel jaggies.
```

Then also rerun:

```bash
python3 scripts/cleanup_lines.py plate-raw.png plate-clean.png --threshold 128 --min-long-edge 3200 --smooth 1.2
```

Hairline / will vanish in print:

```
Same picture, thicker even outlines, still white interiors. One felt-tip weight.
```

Gray / photoreal:

```
Pure white interiors, no gray, no shading, no hair strands.
```

Too empty for advanced:

```
Add missing NAMED OBJECTS from the inventory as closed shapes. Do not add extra hatch or thinner lines.
```

Cartoon effects:

```
Match the photograph’s silhouette of fire, smoke, water, or exhaust. No clip-art flames or sparkles.
```

## Extra gates this inspector also owns

1. **Crayon test** — if a 6-year-old cannot land a crayon in the pocket, the pocket is decoration, not coloring.
2. **Ink purity** — leftover photo gray is a failed plate, even with closed lines.
3. **Identity** — a perfect closed drawing of the wrong person still fails.
4. **Intensity honesty** — advanced may not buy quality by drawing more cracks.
5. **Effect honesty** — exhaust, lamps, water follow the photo, not clip-art.
6. **Speckle** — dirt, JPEG crumbs, isolated dots fail.
7. **Even stroke** — mixed hairline + marker blobs fail.
8. **No contamination** — extra objects that are not in the photo never appear.
9. **Print crop** — a closed shape cut by the page edge is an unclosed region.
10. **Smooth ink** — stair-step / sawtooth diagonals fail. Only smooth lines ship.

## What the inspector must not do

- Do not “fix” the plate with Pillow / OpenCV / Canny except the official `cleanup_lines.py` / `compose_a4_pdf.py` print-smooth path.
- Do not ship because the composition is nice.
- Do not loop more than once.
