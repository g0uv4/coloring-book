# QC inspector — 品管人員

After cleanup, the agent **becomes the QC inspector**. No plate is shown as final, and no A4 is composed, until this person signs off. After QC **SHIP**, still **wait for the user** to confirm a PDF or request edits.

**Attach `plate-clean.png` in the chat.** The PDF must never be the first time they see the drawing. Do not say 「走管線」 on a preview turn. Do not pass `--pdf`.

Machine script: `scripts/qc_plate.py`

## Who this person is

A coloring-book print buyer. A filled black cat on a filled black sofa is a poster, not a coloring page. Fail it.

## Step A — machine

```bash
python3 scripts/qc_plate.py plate-clean.png --report qc-report.json
```

Add `--overlay qc-overlay.png` **only on FAIL**.

Must print `QC PASS`. Overlay:

| Overlay | Meaning |
|---|---|
| Red | dangling ends / broken strokes |
| Orange | leaky pockets |
| Purple / blue | solid-fill cores — body, clothes, or background painted black |
| JSON stair / jagged | 1-pixel stair-steps on diagonals |

Do not argue with the machine on **filled black**, ink purity, broken lines, leaks, hairline, speckle, or jaggies.

## Step B — visual

### B1. Lines and regions

- [ ] Continuous strokes, no dashed/hairline gaps
- [ ] Every colorable area is a closed pocket
- [ ] Smooth ink, no stair-steps

### B2. Colorability (poster gate)

- [ ] Interiors are **empty white**. Fur, body, clothes, sofa, walls, sky, water stay white
- [ ] Only the outline is black. No filled silhouettes
- [ ] Looks like a coloring book at thumbnail size, **not** a B&W photo or poster

A single filled torso / filled sofa / filled night sky / filled black cat is an automatic **FAIL**.

### B3. Identity

- [ ] Counts, pose, glasses, haircut, props match the photo
- [ ] No extra people/pets/landmarks

### B4. Intensity and effects

- [ ] Advanced = more named parts, not more black paint
- [ ] Effects follow the photo silhouette

### B5. Print

- [ ] Subject not clipped mid-shape
- [ ] Even line weight

## Step C — verdict

| Verdict | Action |
|---|---|
| **SHIP** | attach `plate-clean.png` in chat + 圖片元素. **Do not compose PDF this turn.** |
| **RETRY** | first fail — regenerate once with the add-on |
| **STOP** | second fail — show the plate, list fails, **no PDF** |

## Retry add-ons

Filled black / B&W poster / dark subject painted in:

```
This is a COLORING BOOK page, not a black-and-white illustration.
ONLY outlines are black. Every interior stays PURE WHITE: fur, body, clothes,
sofa, walls, sky, shadows. A black cat's body is a WHITE pocket.
No filled silhouettes. No solid black shapes.
```

Broken / dashed:

```
Redraw with fewer shapes. Medium-thick CONTINUOUS felt-tip outlines. Every region a closed loop.
```

Orange leaks:

```
Close every colorable region. No gaps. Do not add more inner lines.
```

Jagged:

```
Same closed shapes, smoother continuous ink. No pixel stairs.
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

## Extra gates

1. Crayon test
2. Ink purity
3. Identity
4. Intensity honesty
5. Effect honesty
6. Speckle
7. Even stroke
8. No contamination
9. Print crop
10. Smooth ink
11. **No filled paint** — if a region a child would color is already black, FAIL. Purple overlay marks those cores.

## Must not

- Do not ship a pretty poster.
- Do not skip showing the PNG in chat.
- Do not compose PDF because QC passed — the user still has to say 輸出 PDF.
- Do not say 「走管線」 or pass `--pdf` on a preview turn.
