# Pattern fills — judge five schemes per plate

Large empty fields (sky, sea, road, wall, floor, tabletop) are dull to color. After the first plate is on screen, the coordinator **judges this photo** and offers **exactly five** fill schemes. The user picks one (or says no).

Default on the first plate is still empty white. Never auto-apply a pattern. Never generate five sample pictures unless they ask to see one scheme.

## When this step runs

After QC SHIP + 圖片元素, if the plate has at least one large empty field, print:

```text
大面積填滿（選 1–5，或說不要）
1. {區域} · {名稱} — {一句畫法}
2. …
3. …
4. …
5. …
```

If there is no large empty field (tight headshot), skip this block.

Do not offer patterns on faces, hair, hands, small props, animals, or lettering.

## How to pick the five (do this every time)

Look at the photo and the plate. Invent five schemes **for these blanks**. Do not paste the same five names on every job.

Rules for the set of five:

1. Name the **region** in each row (`天空` / `海` / `步道` / `牆`).
2. At least two schemes target the largest blank.
3. At least one scheme is simple bands or large slabs (easy for kids).
4. At least one scheme is denser but still crayon-sized cells (advanced).
5. Match the scene: waterfront → waves / scales / sail triangles; kitchen → tile diamonds / wood-slab bands (not wood grain); mountain → chevrons; night sky → large star pockets, not glitter.
6. You may use library motifs below **or invent** a closed-cell geometry. Invented names must be short enough to reuse (`雲塊紋`, `魚鱗紋`, `石板紋`).
7. Indigenous-inspired names (菱格、百步蛇、山形) are allowed when they fit. They are geometric homages, not ceremonial replicas. Do not put snake heads on a person.

## Library (steal or ignore)

| Motif | Draw as |
|---|---|
| 菱格紋 | large diamonds, one pocket each |
| 百步蛇紋 | diamond chain; optional triangular head every 4th cell |
| 變形蟲紋 | packed irregular blobs sharing walls |
| 山形紋 | 3–6 horizontal chevron bands |
| 波浪帶紋 | 3–8 undulating bands |
| 魚鱗紋 | large overlapping scale arcs |
| 雲塊紋 | 5–12 cloud-shaped closed masses |
| 石板紋 | 4–10 big pavement slabs, not a tile grid |
| 帆三角 | large triangles pointing one way |
| 同心圓 | 3–5 nested rings in one corner of sky, rest empty |

## Cell-size law (QC)

- Simple: ~6–10 cells in the region.
- Medium: ~8–16.
- Advanced: ~12–24. Still crayon-sized.
- A cell smaller than a fingernail on A4 is forbidden — merge it.
- Same medium felt-tip as the plate. White interiors. No black fill.
- Pattern stays inside the named region.

## How to apply

User says `1` / `天空用菱格` / `海用波浪帶`. Then [local-redraw.md](local-redraw.md) that region only:

```
Edit ONLY {REGION} of the existing coloring plate.
Fill {REGION} with {PATTERN}: {one-sentence recipe}.
Keep every other outline identical.
Each cell is a CLOSED white pocket, medium-thick outline.
Do not hatch. Do not fill cells black. Do not decorate faces.
```

Cleanup + QC + embed PNG. PDF still waits.
If QC fails on density, retry once with half as many cells.

## Must not

- Do not lock every job to the same five catalog names.
- Do not generate five preview pictures of the motifs (text list is enough).
- Do not pattern the whole page or faces.
- Do not claim a tribe commissioned the page.
