# Example 05 — Group / medium / family of four

## User request

```text
家庭合照變著色本，中等細節。四個人都要在。
Family photo to coloring page, medium, keep all four people.
```

## Photo (described — not bundled)

Outdoor half-to-full group. Adult man back-left, adult woman back-right, two children in front. Man has a beard and glasses. Woman has long hair. Kids hold hands. Park trees behind.

## Analysis worksheet

```
USER_PHOTO path: /uploads/family-four.jpg
Kind: group
Orientation: landscape
Crop: half / full group
Subject count: 4 people, 0 animals

Left-to-right subjects:
1. adult man (back), short hair, glasses, beard as one mass, polo shirt
2. child (front-left), short hair, t-shirt
3. child (front-right), pigtails, dress
4. adult woman (back-right), long hair, blouse

Must-keep distinctive facts:
- count = 4
- height order (adults taller)
- overlaps: kids in front of adults
- man's glasses + beard mass
- girl's pigtails
- holding hands if clearly visible

Background masses:
- 3–6 tree / hedge masses
- ground
- sky as empty white or one band

Drop from the photo:
- leaves one-by-one, picnic litter, distant joggers
```

## Intensity + tools

- Intensity: `medium` (default / 家庭)
- Aspect ratio: `3:2` (landscape source)

## Filled inventory

```
Kind: group
Crop: full body
Orientation: landscape
People: 2 adults + 2 children; man glasses+beard polo; girl pigtails dress; boy t-shirt; woman long hair blouse
Animals: none
Pose: standing family group, kids in front holding hands
Must-keep details: count=4, overlaps, glasses, beard mass, pigtails
Advanced extra parts: (not used)
Background masses: ground, sky band, 3–6 tree masses
Do not draw: extra relatives, leaf veins, logos
```

## Expected plate

- All four present; back-row faces simpler but still have eyes/mouth
- Man: rectangular or oval glasses + one beard mass
- Medium clothing blocks; a few inner facts only
- Trees as big closed bushes, not foliage etchings

## QC gates

- [ ] Count is four
- [ ] Overlaps preserved (do not unstack everyone into a lineup unless the photo is a lineup)
- [ ] Faces not photoreal
- [ ] `QC SHIP`

## Common fail → retry

Dropped back-row adult → regenerate with inventory count forced to 4. Do not "simplify" by deleting a person.

## Delivery note

`QC SHIP / medium / family of four, overlaps kept, trees as masses`
