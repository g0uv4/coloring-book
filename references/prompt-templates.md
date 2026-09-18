# Prompt templates

Put the **white-interior lock first**, intensity second, inventory third, don'ts last. Write the inventory in English even if the user wrote in Chinese.

Always insert **exactly one** intensity block: `simple`, `medium`, or `advanced`. Default `medium`.

Edit **only the user photograph**. Never attach third-party coloring pages as style images.

## Master prompt (image-to-image)

```
Redraw this photograph as a printable COLORING BOOK page.

OUTLINES ONLY. Every interior stays PURE WHITE so a crayon can fill it.
Do not fill fur, hair, clothes, furniture, sky, or animal bodies with black.
A black cat, black dog, black shirt, or dark sofa is still a WHITE shape with a medium-thick black outline.
The only solid-black dots allowed are tiny pupils or a nose button.
This is not a black-and-white poster and not a filtered photo.

{INTENSITY_BLOCK}

Shared Open-Line Plate rules:
- Pure white background
- Black outlines only, one consistent MEDIUM-THICK felt-tip weight (not hairline)
- Every region is a CLOSED loop a crayon can fill. No broken, dashed, or fading lines
- If a detail is too small to close as a complete shape, omit it
- Cartoon-illustration of the real subjects. Keep identity: count, pose, haircut, glasses, clothing.
- Faces: oval eyes with a round pupil, simple brows, small U-nose, simple smile, no eyelashes, no wrinkles, no pores
- Hair as closed WHITE clumps, never individual strands, never filled solid black
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
- Keep only the 3 to 6 largest subjects as closed WHITE silhouettes
- Almost no inner seams
- Faces: oval head, two eyes, brows, U-nose, simple smile — stop there
- Drop any part you cannot draw as a complete closed shape the size of a thumb on A4
```

### medium

```
INTENSITY: MEDIUM (family coloring book, ages about 8–14). Default.
- Medium-thick even felt-tip outlines
- Hair as 4 to 8 WHITE clumps; clothes as 1–3 WHITE blocks
- Background as 4 to 12 large WHITE shapes
- Drop any part smaller than a fingernail on A4, or any line you cannot close
```

### advanced

```
INTENSITY: ADVANCED means MORE NAMED PARTS from the photograph, NOT denser lines and NOT filled ink.
- Same medium-thick felt-tip weight as medium. Do not fill shapes black to look finished
- Draw each named object as its own CLOSED WHITE shape
- Hair still WHITE clumps, never strands, never solid black
- Effects must match the photo silhouette — no clip-art flames
- No cross-hatching, no stipple, no zentangle fills
```

## Inventory block

```
Kind: {portrait|group|pet|scene|object}
Animals: {or none; if fur is dark, still draw as white pockets}
Must-keep details: {glasses, collar, whiskers, …}
Advanced extra parts: {named objects in the photo}
Do not draw: {watermarks, timestamps, phone UI, solid black fills}
```

## Retry prompt add-ons

Solid black fills / filled cat:

```
COLORING BOOK page, not a black-and-white illustration.
OUTLINES ONLY. Fur, body, clothes, furniture, sky stay PURE WHITE.
A black animal is still a white shape with a medium-thick outline.
```

Broken / dashed:

```
Redraw with fewer shapes. Medium-thick CONTINUOUS outlines. Every region a closed loop.
```

Too gray / photoreal:

```
Pure white interiors, no gray, no shading, no hair strands.
```

Too empty when advanced:

```
Add missing NAMED OBJECTS as closed WHITE shapes with outlines. Do not fill them black.
```

## Aspect ratio

- Source taller or square → `2:3`
- Source clearly wide → `3:2`
