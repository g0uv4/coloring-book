# Example 03 — Portrait / advanced / elderly hat + earrings

## User request

```text
高階細節，把阿嬤這張照片變成著色頁。帽子和耳環都要留下。A4 PDF。
Advanced intensity. Keep the hat and earrings. A4 PDF.
```

## Photo (described — not bundled)

Elderly woman, three-quarter view. Soft bun, small brimmed hat, round earrings, collared jacket with visible buttons, light scarf. Garden foliage behind.

## Analysis worksheet

```
USER_PHOTO path: /uploads/amah-hat.jpg
Kind: portrait
Orientation: portrait
Crop: half body
Subject count: 1 person, 0 animals

Left-to-right subjects:
1. elder, bun under brimmed hat, no glasses, collared jacket + scarf, three-quarter smile

Must-keep distinctive facts:
- apparent elder (do not add wrinkles as texture)
- bun silhouette
- brimmed hat
- round earrings as loops
- collar
- jacket buttons as tiny circles
- scarf as one or two closed bands

Background masses:
- a few large leaf / bush masses (not hundreds of veins)
- optional simple ground

Drop from the photo:
- wrinkle fields, pores, fabric weave
- individual hat-weave straw lines
- distant unreadable flowers as specks
```

## Intensity + tools

- Intensity: `advanced` (高階 / keep named accessories)
- Aspect ratio: `2:3`
- Same line weight as medium — not hairline

## Filled inventory

```
Kind: portrait
Crop: half body
Orientation: portrait
People: 1 elder; bun, brimmed hat, round earrings, collared jacket, scarf, three-quarter view
Animals: none
Pose: half-body, looking slightly off-camera, gentle smile
Must-keep details: hat brim, bun, earrings as loops, collar, scarf bands
Advanced extra parts: jacket buttons as tiny circles, hat crown vs brim as two shapes, scarf knot if closable
Background masses: 3–6 foliage masses, no leaf veins
Do not draw: wrinkles, pores, straw weave, extra people
```

## Expected plate

- Same face recipe as medium: no wrinkle map, no lashes
- Extra **named parts** only: hat crown/brim, earrings, collar, buttons, scarf
- Foliage = large closed leaves / bushes
- Advanced ≠ denser hatch

## QC gates

- [ ] Hat and earrings still there
- [ ] Face is not a traced elder photograph
- [ ] Line weight matches medium
- [ ] No zentangle in the hat or foliage
- [ ] `QC SHIP`

## Common fail → retry

Too empty for advanced →

```
Add missing NAMED OBJECTS from the inventory as closed shapes. Do not add extra hatch or thinner lines.
```

## Delivery note

`QC SHIP / advanced / hat + earrings + collar kept as closed shapes, no wrinkle texture`
