# Prompt templates

Image models follow the first concrete visual orders hardest. Put the lock first, the intensity block second, the inventory third, the don'ts last. Write the inventory in English even if the user wrote in Chinese — the image model is more reliable that way.

Always insert **exactly one** intensity block: `simple`, `medium`, or `advanced`. Default `medium`.

Edit **only the user photograph**. Never attach third-party coloring pages as style images.

## Master prompt (image-to-image)

```
Redraw this photograph as a printable coloring-book page.

ONLY THE OUTLINES ARE BLACK. Every interior stays PURE WHITE so a crayon can color it.
A black cat, black dog, black hair, black clothes, dark sofa, or night sky is a WHITE pocket with a black outline — never a filled silhouette and never a B&W poster.

This is a translation into Open-Line Plate illustration, not a filter and not an edge-detected tracing of the photo.

{INTENSITY_BLOCK}

Shared Open-Line Plate rules:
- Pure white background
- Black outlines only, one consistent MEDIUM-THICK felt-tip weight (not hairline)
- Every region is a CLOSED loop a crayon can fill. No broken, dashed, or fading lines
- If a detail is too small to close as a complete shape, omit it
- Cartoon-illustration of the real subjects. Keep identity: count, pose, haircut, glasses, clothing.
- Faces: oval eyes with a round pupil, simple brows, small U-nose, simple smile, no eyelashes, no wrinkles, no pores
- Hair as closed clumps, never individual strands, never filled solid black
- Animal fur as closed clumps; body and dark coat stay white inside
- Hands simplified to cartoon fingers
- Effects (fire, smoke, water, exhaust) follow the PHOTO silhouette — not clip-art flames or sparkles
- No shading, no gray fills, no hatching, no stipple, no watercolor, no paper texture
- No watermark, no logo, no caption, no frame
- Do not add people, animals, or landmarks that are not in the photograph
- Tiny trademarks become a simple geometric badge or are omitted

Inventory:
{INVENTORY}
```

## Intensity blocks

### simple

```
INTENSITY: SIMPLE (young children).
- Slightly thicker even outlines
- Keep only the 3 to 6 largest subjects as closed outlines with white interiors
- Almost no inner seams: one outline per garment, 3 to 5 hair clumps, background as 2 to 5 masses
- Faces: oval head, two eyes, brows, U-nose, simple smile — stop there
- Drop any part you cannot draw as a complete closed shape the size of a thumb on A4
- Scene machines as clean stacked shapes, not panel maps
```

### medium

```
INTENSITY: MEDIUM (family coloring book, ages about 8–14). Default.
- Medium-thick even felt-tip outlines
- Main subjects plus a handful of inner facts that are easy to close (window band, a few rings, simple lattice)
- Hair as 4 to 8 clumps; clothes as 1–3 blocks; striped shirts 2–5 wide stripes
- Background as 4 to 12 large shapes
- Drop any part smaller than a fingernail on A4, or any line you cannot close
```

### advanced

```
INTENSITY: ADVANCED means MORE NAMED PARTS from the photograph, NOT denser or thinner lines, NOT more black paint.
- Same medium-thick felt-tip weight as medium. Do not go hairline. Do not add hatch, ribs, or tile grids just to look busy
- Inventory every distinctive object a viewer would name in the photo (mast, bag, glasses temples, gantry arm, tail, sign, collar) and draw each as its own CLOSED white-inside shape
- Skip any part that would force broken or dashed lines
- Hair still clumps (you may split a few more clumps if the haircut needs it), never strands
- Whiskers on a cat: at most 3 to 6 lines per side, not filled wedges
- Glasses include temples if they are visible; extra garments/props only if they are in the photo
- Effects must match the photo: rocket exhaust is smooth vertical plumes, not cartoon campfire tongues or spark teardrops
- No cross-hatching, no stipple, no zentangle fills, no filled-black animals or furniture
```

## Inventory block (fill from analysis)

For **advanced**, list extra named parts that simple/medium would drop.

```
Kind: {portrait|group|pet|scene|object}
Crop: {headshot|half body|full body}
Orientation: {portrait|landscape}
People: {N adults, M children; left-to-right one-line descriptions}
Animals: {or none}
Pose: {what they are doing}
Must-keep details: {glasses, backpack, temple roof, ...}
Advanced extra parts (named objects in the photo): {lightning mast, gantry arms, OMS pods, ...}
Background masses: {sky, trees, building, road}
Do not draw: {watermarks, timestamps, phone UI, cartoon clip-art that is not in the photo}
Do not fill: {animal body, dark fur, dark clothes, dark furniture — white interiors}
```

## Retry prompt add-ons

Prefer the copies in [qc-inspector.md](qc-inspector.md) after a QC fail. Shortcuts:

Filled black / silhouette / B&W poster:

```
ONLY outlines are black. Every interior stays PURE WHITE: fur, body, clothes, sofa, walls, sky.
A black cat's body is a WHITE pocket. No filled silhouettes. No solid black shapes.
```

Broken / dashed / hairline lines:

```
Redraw with fewer shapes. Medium-thick CONTINUOUS outlines. Every region a closed loop. If you cannot close a line, omit that detail.
```

Too gray / photoreal (any intensity):

```
Pure white interiors, no gray, no shading, no hair strands. Faces stay coloring-book simple.
```

Too empty when intensity is advanced:

```
Add missing NAMED OBJECTS from the inventory as closed shapes. Do not add extra hatch, ribs, or thinner lines.
```

Too busy when intensity is simple:

```
Keep only the largest outlines. Thicken remaining outlines. White interiors.
```

Cartoon effects that ignore the photo:

```
Match the photograph’s silhouette of fire, smoke, water, or exhaust. No clip-art flames, sparkles, or campfire tongues.
```

## Aspect ratio

- Source taller or square → `2:3` (fits portrait A4)
- Source clearly wide → `3:2` (fits landscape A4)
