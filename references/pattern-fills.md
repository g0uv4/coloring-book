# Pattern fills — large empty regions only

Sky, sea, road, wall, and floor often leave a huge white field that is dull to color. The user may ask to fill **that named region** with a repeating closed-cell pattern.

Default is **no pattern**. Never auto-pattern a first plate.

These are coloring-book geometries inspired by common Taiwan textile motifs. They are not ceremonial replicas, not tribal authorization, and not a substitute for living indigenous design. Keep cells large enough for a crayon.

## When to offer

After the plate preview, if a listed element is a large empty field (sky / sea / water / road / pavement / wall / floor), add one line:

```text
大面積可加格紋：菱格紋、百步蛇紋、變形蟲紋、山形紋、波浪帶紋
例如「天空用菱格紋」「海用波浪帶」「道路用山形紋」
```

Do not offer patterns on faces, hair, hands, small props, or the otter-sized objects.

## The five patterns

| id | 中文 | Use on | What to draw |
|---|---|---|---|
| `rhombus` | 菱格紋 | sky, wall, floor | A grid of **large** diamonds. Each diamond is one closed white pocket. About 8–20 cells in the region. |
| `hundred-pacer` | 百步蛇紋 | sky, wall, sash-like bands | A **row of large diamonds** (snake-back). Every 4th unit may be a simple triangular head. No realistic scales, no tiny lace. |
| `amoeba` | 變形蟲紋 | sky, sea, ground | Packed **large irregular closed blobs**. Neighbors share walls. No speckles. |
| `mountain` | 山形紋 | road, wall, distant hills, sky band | Horizontal **chevron / zigzag bands**. 3–6 bands, each a closed strip. |
| `wave` | 波浪帶紋 | sea, water, sky | Parallel **undulating bands** (3–8). Each band is a closed pocket. No ripple hatch. |

Aliases the user may type:

- 菱形 / 菱格 / diamond / 祖靈之眼 → `rhombus`
- 百步蛇 / 蛇紋 / snake → `hundred-pacer`
- 變形蟲 / 雲漩 / amoeba → `amoeba`
- 山形 / 鋸齒 / 山脈 / zigzag → `mountain`
- 波浪 / 海紋 / wave → `wave`

## Cell-size law (QC)

- Simple: ~6–10 cells in the whole region.
- Medium: ~8–16.
- Advanced: ~12–24. Still crayon-sized. Never hairline mesh.
- A cell smaller than a fingernail on A4 is forbidden — merge it.
- Pattern lines use the **same medium felt-tip** as the rest of the plate.
- Interiors stay paper white. Pattern is outlines, not black fill.
- Pattern stays **inside** the named region. Do not let diamonds crawl onto faces or the bridge.

## How to apply

This is a [local-redraw.md](local-redraw.md) of **one region** on `CLEAN_PLATE`.

```
Edit ONLY {REGION} of the existing coloring plate.
Fill {REGION} with the {PATTERN} coloring-book pattern:
{PATTERN_RECIPE}
Keep every other outline identical.
Each pattern cell is a CLOSED white pocket with a medium-thick outline.
Do not hatch. Do not fill cells black. Do not decorate faces.
```

Then cleanup + QC + embed PNG. PDF still waits.

If QC fails because the pattern is too dense: retry once with half as many cells.

## Must not

- Do not put 百步蛇 heads on a person's body.
- Do not claim a tribe commissioned this page.
- Do not mix two patterns in one region unless the user asked.
- Do not pattern the whole page.
