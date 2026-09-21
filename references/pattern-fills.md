# Pattern fills — large empty regions only

Sky, sea, road, and floor often stay one blank pocket. That is correct by default. If the user asks to fill those regions with a lattice so they are easier to color, use **one** of the five packs below.

Never apply a pack to faces, hair, animals, clothes, or small props unless they name that object.

This is a **geometric homage** for a coloring page. It is not a ceremonial replica, not a tribal emblem, and not a filled texture hatch.

## When

| User says | Do |
|---|---|
| 天空用菱格紋 / 海用山形紋 / fill the sky with diamonds | local-redraw that region with the matching pack |
| 大塊空白難以上色 / 要格紋 | show the five-pack table and wait for a name |
| nothing about fills | leave large regions empty white |

Default intensity does **not** turn pattern fills on.

## The five packs

Every cell is a **closed white pocket**. Same medium felt-tip as the rest of the plate. Cell width on A4 ≈ a crayon tip to a thumbnail. About 6–14 cells across a sky band. If a cell would be hairline, omit it.

| id | Name | Geometry | Best on | Do not |
|---|---|---|---|---|
| `rhombus` | **菱格紋** | Tessellated diamonds. Inspired by Atayal / Truku / Seediq woven rhombus (often called 祖靈之眼 in popular writing). | sky, wall, floor | nested micro-diamonds |
| `snake-scale` | **蛇鱗菱紋** | A band of large stacked diamonds — a simplified snake-back lattice. Inspired by Paiwan / Rukai / Bunun scale geometry. | sea band, road, shawl-like slab | draw a snake, fangs, or a chiefly totem |
| `zigzag` | **山形曲折紋** | Horizontal chevron / mountain bands. Common geometric weave across several nations. | sea, hills, road | lightning bolts as clip-art |
| `star8` | **八角星網** | Large 8-point stars whose gaps are also closed pockets. Inspired by Amis star embroidery geometry. | sky | tiny sparkles, 20-point lace |
| `curl` | **捲曲帶紋** | Large closed kidney / paisley blobs in a row. This is the coloring-book stand-in for what people in Taiwan often call 變形蟲紋 (that name is popular for paisley / boteh, **not** a traditional Indigenous weave). | sea, cloth slab | amoeba hatch, overlapping lace |

## Prompt add-on (append after the Open-Line lock)

```
Fill ONLY this named region: {REGION}.
Use pattern pack {PACK_ID} ({PACK_NAME}).
The pattern is a lattice of CLOSED medium-thick outlines with PAPER-WHITE interiors.
Each cell must be large enough for a crayon.
Do not fill any other region. Do not paint cells black. Do not add hatch inside a cell.
Do not draw a realistic snake, face totem, or ceremonial badge.
```

Then cleanup + QC + embed PNG. PDF still waits.

## QC extras for a patterned region

- Cells are closed. A crayon in one cell cannot leak into the next.
- Cell count across the region ≤ ~14. More is FAIL (too dense).
- The rest of the plate is unchanged.
- No solid-black cells.
- Pattern stays inside the named outline.

## Cultural note (say this once, short)

These packs are simplified coloring lattices inspired by published geometric weaves. They are not official tribal emblems. Paiwan / Rukai hundred-pacer imagery is historically restricted; this skill only uses a large diamond-scale lattice, never a snake figure.
