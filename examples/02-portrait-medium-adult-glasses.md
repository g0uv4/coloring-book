# Example 02 — Portrait / medium / adult with glasses

## User request

```text
把這張照片變成著色本，輸出 A4 PDF。用中等細節。
Use $coloring-book. Medium detail. Printable A4.
```

## Photo (described — not bundled)

Half-body of one adult. Short side-part hair, rectangular glasses, navy crew-neck sweater, slight smile. Bookshelf softly out of focus behind.

## Analysis worksheet

```
USER_PHOTO path: /uploads/adult-glasses.jpg
Kind: portrait
Orientation: portrait
Crop: half body
Subject count: 1 person, 0 animals

Left-to-right subjects:
1. adult, short side-part hair, rectangular glasses with arms, navy crew-neck sweater (1–2 blocks), facing camera

Must-keep distinctive facts:
- one adult
- side-part hair silhouette
- rectangular glasses (not round)
- glasses arms visible
- crew-neck sweater
- half-body crop (do not invent legs)

Background masses:
- bookshelf as 2–4 large rectangles OR empty wall
- no readable book titles

Drop from the photo:
- fabric knit, pores, eyelid creases
- tiny shelf objects
- any watermark
```

## Intensity + tools

- Intensity: `medium` (user said 中等; also the default)
- Aspect ratio: `2:3`
- Tool: `imagine_image_to_image` on USER_PHOTO only

## Filled inventory

```
Kind: portrait
Crop: half body
Orientation: portrait
People: 1 adult; short side-part hair, rectangular glasses, navy crew-neck sweater, slight smile
Animals: none
Pose: standing / seated half-body, facing camera
Must-keep details: rectangular lenses + bridge + arms, side-part hair clumps, crew neck
Advanced extra parts: (not used at medium)
Background masses: wall, optional 2–4 bookshelf rectangles
Do not draw: readable titles, pores, extra people
```

## Expected plate

- Face recipe from portrait-rules.md
- Hair as 4–8 closed clumps
- Glasses: two rectangles + bridge + arms
- Sweater 1–3 clothing blocks; no invented fashion seams
- Bookshelf simplified to big rectangles if kept
- Medium felt-tip weight, white interiors

## QC gates

- [ ] Glasses stay rectangular (identity)
- [ ] Arms of glasses present if they were visible
- [ ] Not photoreal ink of the face
- [ ] Hair not filled solid black
- [ ] `QC SHIP`

## Common fail → retry

Hairline glasses or missing arms → redraw glasses as closed thick frames. Do not drop them because they are "busy".

## Delivery note

`QC SHIP / medium / adult glasses kept rectangular, half-body crop honored`
