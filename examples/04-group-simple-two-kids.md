# Example 04 — Group / simple / two kids

## User request

```text
兩個小孩的照片，簡單著色頁，給他們著。A4。
Simple coloring page of these two children. A4 PDF.
```

## Photo (described — not bundled)

Full-body outdoor snapshot. Girl on the left in a dress, boy on the right in a striped tee and shorts, both waving. Grass and a bit of sky.

## Analysis worksheet

```
USER_PHOTO path: /uploads/two-kids.jpg
Kind: group
Orientation: portrait
Crop: full body
Subject count: 2 people, 0 animals

Left-to-right subjects:
1. child girl, shoulder-length hair, dress as one silhouette, waving right hand
2. child boy, short hair, striped tee (at simple: treat shirt as ONE block), shorts, waving left hand

Must-keep distinctive facts:
- exactly two children
- left/right order and relative height
- waving hands
- dress vs tee+shorts
- full-body shoes

Background masses:
- ground line + 1–2 bushes OR empty
- optional sun only if the photo has bright sky / sun

Drop from the photo:
- grass blades, distant people
- inner stripes at simple intensity
```

## Intensity + tools

- Intensity: `simple`
- Aspect ratio: `2:3`

## Filled inventory

```
Kind: group
Crop: full body
Orientation: portrait
People: 2 children; girl in a dress waving, boy in tee and shorts waving
Animals: none
Pose: standing, both waving
Must-keep details: count=2, height order, wave gestures, dress vs shorts
Advanced extra parts: (not used)
Background masses: ground, 1–2 bushes
Do not draw: extra children, grass blades, readable logos
```

## Expected plate

- Two complete bodies, slightly thicker ink
- Each garment one silhouette (boy shirt NOT striped at simple)
- Cartoon hands, 3–5 hair clumps each
- Faces: oval, eyes, brows, U-nose, smile — stop there

## QC gates

- [ ] Count is two — nobody dropped, nobody added
- [ ] Left girl / right boy still reads
- [ ] Simple is not a parts catalog
- [ ] `QC SHIP`

## Common fail → retry

Too busy for simple →

```
Keep only the largest silhouettes. Thicken remaining outlines.
```

## Delivery note

`QC SHIP / simple / two kids, stripes dropped, waves kept`
