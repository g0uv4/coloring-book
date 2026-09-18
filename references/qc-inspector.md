# QC inspector — 品管人員

After cleanup, the agent **becomes the QC inspector**. No plate ships, and no A4 is composed, until this person signs off.

Machine script: `scripts/qc_plate.py`  
Visual script: this file  
One retry if the plate fails. Then stop.

## Who this person is

A coloring-book print buyer. They do not care how clever the prompt was. They care whether a child can color the page without the crayon leaking, and whether the picture still is the photograph.

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

Do not argue with the machine on ink purity, broken lines, leaks, hairline strokes, or speckle. Those are its job.

## Step B — visual (you look)

Open `plate-clean.png` at something like a phone-screen size, then at full size. Tick every box. A single **no** is a fail.

### B1. Lines and regions (non-negotiable)

- [ ] Every stroke looks continuous — no dashed, fading, or hairline gaps
- [ ] Every area you would color is a **closed** pocket. A crayon starting inside cannot reach a neighbor without crossing ink
- [ ] If a detail cannot be closed, it should not be there (omit, don't leave a gap)

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

## Step C — verdict

| Verdict | When | Action |
|---|---|---|
| **SHIP** | machine PASS + every visual box ticked | compose A4 |
| **RETRY** | first fail | regenerate **once** with the matching add-on below |
| **STOP** | second fail | show the best plate, the QC fails, and do **not** compose a PDF |

Write one line into the run notes, e.g. `QC SHIP / medium / closed lines, identity ok`.

## Retry add-ons (copy into the image prompt)

Broken / dashed / red overlay:

```
Redraw with fewer shapes. Medium-thick CONTINUOUS felt-tip outlines. Every region a closed loop. If you cannot close a line, omit that detail. No hairline, no dashed lattice.
```

Orange leaks / unclosed pockets:

```
Close every colorable region. No gaps in outlines. Do not add more inner lines; join the ones you already drew.
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

These are the additions beyond “lines connected + regions closed”:

1. **Crayon test** — if a 6-year-old cannot land a crayon in the pocket, the pocket is decoration, not coloring.
2. **Ink purity** — leftover photo gray is a failed plate, even with closed lines.
3. **Identity** — a perfect closed drawing of the wrong person still fails.
4. **Intensity honesty** — advanced may not buy quality by drawing more cracks.
5. **Effect honesty** — exhaust, lamps, water follow the photo, not clip-art.
6. **Speckle** — dirt, JPEG crumbs, isolated dots fail.
7. **Even stroke** — mixed hairline + marker blobs fail.
8. **No contamination** — extra objects that are not in the photo never appear.
9. **Print crop** — a closed shape cut by the page edge is an unclosed region.

## What the inspector must not do

- Do not “fix” the plate with Pillow / OpenCV / Canny. Only the image model may redraw.
- Do not ship because the composition is nice.
- Do not loop more than once.
