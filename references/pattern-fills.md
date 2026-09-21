# Pattern fills — judge the plate, offer five schemes

Large empty fields (sky, sea, water, road, pavement, wall, floor, field) are dull to color. After every plate preview that has at least one such field, the coordinator **must invent five schemes for this photo** and list them.

Do **not** reuse a fixed five-name catalog. Do **not** limit the vocabulary to 菱格 / 百步蛇 / 變形蟲. Those names are allowed when they fit. So are stripes, scallops, bricks-as-slabs, concentric arcs, cloud pockets, window bands, chevrons, stars, pebbles.

Default is still **no pattern on the first plate**. Never bake a fill until they pick a numbered scheme or say `天空用X`.

## After preview — required block

Look at the plate + the photo. Name the large blank fields. Then print exactly five options:

```text
大面積空白（{fields}）可加格紋。這張照的五種方案：
1. {name} — {which field} — {one-line geometry}
2. …
3. …
4. …
5. …
回「1」「天空用菱格」或「先不加格紋」。
```

Do **not** generate five sample images unless they ask `先看樣張`. Text recipes are the offer. Sample-image failure is not an excuse to skip the five names.

## How to judge the five

Pick for **this** photo. Mix region + rhythm:

| Photo cue | Lean toward |
|---|---|
| Big empty sky | large diamonds, cloud pockets, concentric arcs, sparse stars, horizontal bands |
| Sea / river | wave bands, pebble ovals, long chevrons, scallops |
| Road / pavement | chevron bands, large flagstones, 3–5 stripes |
| Wall / building face | window-sized rectangles, brick slabs (few), diamond grid |
| Indoor floor | wood-plank slabs, large tiles |
| Mountain / hillside | mountain zigzags, terrace bands |
| Night sky | sparse 6–8 pointed stars as closed pockets, not sparkles |
| Fabric / blanket already in the photo | echo a simplified weave from the photo |

Rules for inventing a scheme:

1. Name it in the user's language (short, 2–6 characters if Chinese).
2. Say **which field** it applies to.
3. Geometry is closed cells a crayon can fill. ~6–24 cells in that field. Same medium stroke.
4. At least two of the five should target different fields if the plate has more than one blank (sky + sea, not five sky-only variants).
5. One of the five may be `保持空心` (leave that field blank) so they can refuse fills without hunting for the words.
6. Do not put a pattern on faces, hair, hands, animals, or small props.
7. Indigenous-inspired names (菱格、蛇鱗菱、山形、八角星) are fine as **geometry labels**. Never claim a tribe commissioned the page. Never draw a realistic snake or a ceremonial badge.

## Apply

This is a [local-redraw.md](local-redraw.md) of one named region on `CLEAN_PLATE`.

```
Edit ONLY {REGION} of the existing coloring plate.
Fill {REGION} with this coloring-book lattice: {GEOMETRY}.
Each cell is a CLOSED white pocket, medium-thick outline, crayon-sized.
Keep every other outline identical. No hatch. No black-filled cells.
```

Cleanup + QC + embed PNG. PDF still waits.
If QC says too dense: retry once with half the cells.

## Cell-size law

- Simple: ~6–10 cells in the region.
- Medium: ~8–16.
- Advanced: ~12–24. Still fingernail-or-larger on A4.
- Same felt-tip weight as the plate.
- Pattern stays inside the named outline.

## Must not

- Do not lock the skill to five immortal motif names.
- Do not skip the five-scheme block when a large blank exists.
- Do not generate five Imagine samples by default (they fail often and slow the turn).
- Do not pattern the whole page.
- Do not mix two patterns in one region unless they asked.
