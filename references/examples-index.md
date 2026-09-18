# Worked examples index

Worked few-shot cases. They teach **analysis → intensity → filled prompt → QC → preview**. Compose a PDF only after the user confirms.

There are **no bundled coloring plates**. Do not copy subjects from these write-ups onto a user's photo. Do not feed a mood image as IMAGE 1.

Load **one existing example** that matches the current photo's **kind** and **intensity** before generating. If no row matches, use the closest kind at the same intensity. **Do not open a path that is not in the table below.**

Only files that exist in `examples/` are listed.

| # | File | Kind | Intensity | What it trains |
|---|---|---|---|---|
| 01 | [examples/01-portrait-simple-child-headshot.md](../examples/01-portrait-simple-child-headshot.md) | portrait | simple | child face recipe, almost no inner seams |
| 02 | [examples/02-portrait-medium-adult-glasses.md](../examples/02-portrait-medium-adult-glasses.md) | portrait | medium | glasses + hair clumps + clothing blocks |
| 03 | [examples/03-portrait-advanced-elderly-hat-earrings.md](../examples/03-portrait-advanced-elderly-hat-earrings.md) | portrait | advanced | named accessories, still no wrinkles/pores |
| 04 | [examples/04-group-simple-two-kids.md](../examples/04-group-simple-two-kids.md) | group | simple | count + height order, thick silhouettes |
| 05 | [examples/05-group-medium-family-of-four.md](../examples/05-group-medium-family-of-four.md) | group | medium | overlaps, back-row faces stay simple |
| 06 | [examples/06-group-advanced-team-photo.md](../examples/06-group-advanced-team-photo.md) | group | advanced | extra garments/props per person, same line weight |
| 07 | [examples/07-group-advanced-kitchen.md](../examples/07-group-advanced-kitchen.md) | group | advanced | busy kitchen: named bowls/board/hood; vest and floor as slabs not texture |

Special gates that used to live as examples 16–20 are **rules in the skill**, not missing files:

- Mixed person+pet+place → kind priority portrait > pet > scene ([analysis-method.md](analysis-method.md))
- Watermark / timestamp / stock ID → drop UI chrome
- All three intensities → run the pipeline three times; preview all three; PDF each only after confirm
- Wheelchair / glasses / distinctive aid → never drop it because it is "busy"
- Costume photo → stylize **that photo**; refuse official character model sheets

## How to use a case

1. Match kind + intensity from the table.
2. Copy the **filled inventory** pattern, not the fictional subjects.
3. Keep the shared Open-Line Plate lock verbatim from [prompt-templates.md](prompt-templates.md).
4. After cleanup, run `qc_plate.py --kind {kind}` and the QC boxes in the case. One retry only.
5. Show the plate. Wait. PDF only if the user confirms.
6. Confirming a PDF does **not** rewrite remembered default intensity.
