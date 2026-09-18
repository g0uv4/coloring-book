# Worked examples index

Twenty original few-shot cases. They teach **analysis → intensity → filled prompt → QC → delivery**.

There are **no bundled coloring plates**. Do not copy subjects from these write-ups onto a user's photo. Do not feed a mood image as IMAGE 1.

Load one example that matches the current photo's **kind** and **intensity** before generating. For mixed photos, also read example 16 (kind priority). For all-three requests, read example 18.

| # | File | Kind | Intensity | What it trains |
|---|---|---|---|---|
| 01 | [examples/01-portrait-simple-child-headshot.md](../examples/01-portrait-simple-child-headshot.md) | portrait | simple | child face recipe, almost no inner seams |
| 02 | [examples/02-portrait-medium-adult-glasses.md](../examples/02-portrait-medium-adult-glasses.md) | portrait | medium | glasses + hair clumps + clothing blocks |
| 03 | [examples/03-portrait-advanced-elderly-hat-earrings.md](../examples/03-portrait-advanced-elderly-hat-earrings.md) | portrait | advanced | named accessories, still no wrinkles/pores |
| 04 | [examples/04-group-simple-two-kids.md](../examples/04-group-simple-two-kids.md) | group | simple | count + height order, thick silhouettes |
| 05 | [examples/05-group-medium-family-of-four.md](../examples/05-group-medium-family-of-four.md) | group | medium | overlaps, back-row faces stay simple |
| 06 | [examples/06-group-advanced-team-photo.md](../examples/06-group-advanced-team-photo.md) | group | advanced | extra garments/props per person, same line weight |
| 07 | [examples/07-pet-simple-sleeping-cat.md](../examples/07-pet-simple-sleeping-cat.md) | pet | simple | species silhouette first |
| 08 | [examples/08-pet-medium-dog-collar.md](../examples/08-pet-medium-dog-collar.md) | pet | medium | collar / breed silhouette |
| 09 | [examples/09-pet-advanced-rabbit-hutch.md](../examples/09-pet-advanced-rabbit-hutch.md) | pet | advanced | named hutch parts as closed shapes |
| 10 | [examples/10-scene-simple-mountain-lake.md](../examples/10-scene-simple-mountain-lake.md) | scene | simple | 3–6 large masses |
| 11 | [examples/11-scene-medium-beach-travel.md](../examples/11-scene-medium-beach-travel.md) | scene | medium | water/sky as big bands |
| 12 | [examples/12-scene-advanced-shuttle-launch.md](../examples/12-scene-advanced-shuttle-launch.md) | scene | advanced | intensity.md calibration memory |
| 13 | [examples/13-object-simple-birthday-cake.md](../examples/13-object-simple-birthday-cake.md) | object | simple | one hero object |
| 14 | [examples/14-object-medium-breakfast-table.md](../examples/14-object-medium-breakfast-table.md) | object | medium | a few supporting objects |
| 15 | [examples/15-object-advanced-camera-still-life.md](../examples/15-object-advanced-camera-still-life.md) | object | advanced | named camera parts, no texture hatch |
| 16 | [examples/16-mixed-person-dog-beach.md](../examples/16-mixed-person-dog-beach.md) | mixed | medium | kind priority: portrait > pet > scene |
| 17 | [examples/17-watermark-timestamp-drop.md](../examples/17-watermark-timestamp-drop.md) | portrait | medium | drop UI / date / stock ID |
| 18 | [examples/18-three-intensities-same-photo.md](../examples/18-three-intensities-same-photo.md) | scene | all three | same identity, three pages |
| 19 | [examples/19-wheelchair-keep-accessory.md](../examples/19-wheelchair-keep-accessory.md) | portrait | medium | never drop a distinctive mobility aid |
| 20 | [examples/20-costume-stylize-photo-not-official-art.md](../examples/20-costume-stylize-photo-not-official-art.md) | portrait | medium | stylize the photo; refuse official model sheets |

## How to use a case

1. Match kind + intensity (or the special gate: mixed / watermark / three-up / accessory / costume).
2. Copy the **filled inventory** pattern, not the fictional subjects.
3. Keep the shared Open-Line Plate lock verbatim from [prompt-templates.md](prompt-templates.md).
4. After cleanup, run the QC boxes listed in the case. One retry only.
