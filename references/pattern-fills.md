# Pattern fills — judge five schemes per plate

Large empty fields (sky, sea, road, wall, floor, tabletop) are dull to color. After the first plate is on screen, the coordinator **judges this photo** and offers **exactly five** fill schemes. The user picks one, several, or none.

Default on the first plate is still empty white. Never auto-apply a pattern. Never generate five sample pictures unless they ask to see one scheme.

## When this step runs

After QC SHIP + 圖片元素, if the plate has at least one large empty field, print:

```text
大面積填滿（選 1–5，可多選如 2.3.5，或說不要）
1. {區域} · {名稱} — {一句畫法}
2. …
3. …
4. …
5. …
```

If there is no large empty field (tight headshot), skip this block.

Do not offer patterns on faces, hair, hands, small props, animals, or lettering.

## Multi-pick

`2.3.5`, `2 3 5`, or `2、3、5` means apply schemes 2 + 3 + 5. One crop+paste per distinct region (same region: one crop, both schemes in the prompt).
Different numbers must target different regions. Two schemes for one region share that crop.
Keep faces and named props frozen.

## How to pick the five (do this every time)

Look at the photo and the plate. Invent five schemes **for these blanks**. Do not paste the same five names on every job.

1. Name the **region** in each row (`天空` / `海` / `步道` / `牆`).
2. At least two schemes target the largest blank.
3. At least one scheme is simple bands or large slabs.
4. At least one scheme is denser but still crayon-sized.
5. Match the scene.
6. Library motifs below **or invent** a closed-cell geometry (`雲塊紋`, `魚鱗紋`, `石板紋`).
7. Indigenous-inspired names are geometric homages, not ceremonial replicas. No snake heads on a person.

## Library (steal or ignore)

| Motif | Draw as |
|---|---|
| 菱格紋 | 8–16 **large** diamonds, one pocket each. Not a tight mesh. |
| 百步蛇紋 | diamond chain; optional triangular head every 4th cell |
| 變形蟲紋 | packed irregular blobs sharing walls |
| 山形紋 | 3–6 horizontal chevron bands |
| 波浪帶紋 | 3–6 undulating bands |
| 魚鱗紋 | large overlapping scale arcs |
| 雲塊紋 | 5–12 cloud-shaped closed masses |
| 石板紋 | 4–8 big pavement slabs, not a tile grid |
| 帆三角 | large triangles pointing one way |
| 同心圓 | 3–5 nested rings in one corner of sky |

## Cell-size law (QC)

- Simple: ~6–10 cells in the region.
- Medium: ~8–16.
- Advanced: ~8–16 large cells. Never a hairline diamond lace.
- A cell smaller than a fingernail on A4 is forbidden — merge it.
- Same medium felt-tip. White interiors. No black fill.
- Pattern stays inside the named region.

A tight 菱格 mesh usually fails QC (`too many dangling ends`, `ink speckle`). Draw fewer, larger diamonds.

## How to apply

On a copy of the plate. One box per chosen region. Faces are not inside any box. Do not send the full plate to the image tool for a fill.

Same crop / paste as [local-redraw.md](local-redraw.md): one `region_edit.py` crop+paste per distinct region. Same region: one crop, both schemes in the prompt. Do not run `cleanup_lines.py` on the full plate.

```
This file is one crop of {REGION}, not the full page.
Fill the crop with {PATTERN}: {one-sentence recipe}.
Each cell is a closed white pocket, medium-thick outline.
Do not hatch. Do not fill cells black.
```

QC + embed PNG. PDF still waits.

If QC fails on density / dangling ends: retry **once** with half as many cells (sky 菱格 → about 8 large diamonds, not a grid).
Second fail → show the plate, name the QC fail, **do not PDF** unless they still say 輸出.

## Must not

- Do not lock every job to the same five catalog names.
- Do not generate five preview pictures of the motifs (text list is enough).
- Do not pattern the whole page or faces.
- Do not claim a tribe commissioned the page.
