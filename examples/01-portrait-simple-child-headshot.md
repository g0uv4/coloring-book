# Example 01 — Portrait / simple / child headshot

## User request

```text
把這張小朋友的照片變成著色頁，簡單一點，給幼兒著。輸出 A4 PDF。
Use $photo-coloring-book on this photo. Simple intensity. A4 PDF.
```

## Photo (described — not bundled)

Indoor headshot of one child, about age 5. Short bangs, round face, smiling, pale hoodie. Soft indoor wall behind. Phone timestamp `2026-04-12` in the corner.

## Analysis worksheet

```
USER_PHOTO path: /uploads/child-headshot.jpg
Kind: portrait
Orientation: portrait
Crop: headshot
Subject count: 1 person, 0 animals

Left-to-right subjects:
1. child, short bangs + two side clumps, no glasses, pale hoodie as one block, facing camera, smile

Must-keep distinctive facts (5–12):
- one child only
- short bangs covering forehead
- round head, large coloring-book eyes
- simple smile
- hoodie silhouette to upper chest
- no invented toys or animals

Background masses (≤ 8):
- plain wall (one mass) or empty white
- optional ground-of-shoulders crop line

Drop from the photo:
- timestamp / UI
- pores, flyaway hairs, fabric knit
- room clutter behind the child

Open questions that would change the drawing: none
```

## Intensity + tools

- Intensity: `simple` (user said 簡單 / 幼兒)
- Aspect ratio: `2:3`
- Tool: `imagine_image_to_image` on USER_PHOTO only

## Filled inventory

```
Kind: portrait
Crop: headshot
Orientation: portrait
People: 1 child; short bangs, no glasses, pale hoodie, facing camera, smiling
Animals: none
Pose: head-and-shoulders, looking at camera
Must-keep details: bangs silhouette, hoodie as one garment, child-sized head
Advanced extra parts: (not used)
Background masses: plain wall or empty white
Do not draw: timestamp, pores, individual hair strands, extra toys
```

## Expected plate

- Oval head, 3–5 hair clumps, two oval eyes + pupils, one-stroke brows, U-nose, simple smile
- Hoodie = one closed silhouette; no pocket, no seams
- Slightly thicker outlines than medium
- Empty white interiors; no gray skin
- Timestamp gone

## QC gates

- [ ] Face is a coloring-book child, not a traced photo and not a stick figure
- [ ] Hair is clumps, not strands
- [ ] No date / UI chrome
- [ ] Regions large enough for a crayon
- [ ] Machine `QC PASS` then visual SHIP

## Common fail → retry

Photoreal face or gray skin → add:

```
Pure white interiors, no gray, no shading, no hair strands. Faces stay coloring-book simple.
```

## Delivery note

`QC SHIP / simple / child headshot, timestamp dropped, hoodie one block`
