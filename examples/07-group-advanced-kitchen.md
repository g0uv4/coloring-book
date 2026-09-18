# Example 07 — Group / advanced / kitchen cooking scene

## Teaching goal

Advanced on a busy kitchen means **more named objects from the photo** (board, bowls, hood, faucet), not knit mesh, wood grain, or extra hatch. Textures that would speckle must become **large closed shapes**.

This case is the calibration memory for group + many props. First-pass QC often fails speckle on a vest or floor; retry by omitting texture lines.

## User request

```text
這張廚房照片做高階著色頁。
Advanced coloring page of this kitchen photo.
```

## Photo facts (from a real test; do not copy these people onto another photo)

Four adults in a home kitchen. Foreground woman chops on a board. A man works at the sink. Another man holds a phone in the doorway hall. A woman at the door makes a peace sign.

## Analysis worksheet

```
USER_PHOTO path: /uploads/kitchen-group.jpg
Kind: group
Orientation: portrait
Crop: full / three-quarter, busy interior
Subject count: 4 people, 0 animals

Left-to-right / front-to-back subjects:
1. adult woman, glasses, ponytail + clip, striped shirt, watch, chopping in front
2. adult man, short hair, glasses, dark tee, at the sink with bottles
3. adult man, glasses, striped polo, holding a phone, mid-ground
4. adult woman, glasses, white vest, shorts, peace sign at the doorway

Must-keep distinctive facts:
- count = 4
- glasses on every visible face that has them
- ponytail + clip on person 1
- striped shirt on person 1 (a few large stripe blocks, not every thread)
- chopping pose + knife + board
- phone in person 3 hands
- peace-sign hand on person 4
- range hood, faucet, sink, fridge mass, doorway

Named extra parts (advanced):
- cutting board rectangle
- knife silhouette
- carrot pieces as a few ovals (not shred-by-shred)
- mushroom bowl as bowl + a few cap shapes
- zucchini bowl as bowl + a few slice rings
- bottles on the counter as simple cylinders
- range hood block, faucet loop

Background masses:
- upper cabinets / hood
- fridge slab
- doorway + hall wall
- floor as ONE closed shape

Drop from the photo:
- knit / mesh texture on the vest — vest is one closed garment
- wood-grain floor and board grain
- hair strands; hair is white clumps
- readable bottle labels, watch text, phone UI
- every utensil in a drawer pile
```

## Intensity decision

`advanced` — user asked 高階. Keep named kitchen parts that can close. Same line weight as medium.

## Filled inventory

```
Kind: group
Crop: three-quarter interior
Orientation: portrait
People: 4 adults; person 1 chopping glasses ponytail striped shirt; person 2 at sink glasses; person 3 phone glasses; person 4 doorway vest peace sign
Animals: none
Pose: cooking group, foreground action, back row standing
Must-keep details: count=4, glasses, ponytail+clip, board, knife, hood, faucet, phone, peace sign
Advanced extra parts: board, knife, carrot ovals, two bowls, bottles, hood, faucet, fridge, doorway
Background masses: cabinets/hood, fridge, doorway, floor slab
Do not draw: vest knit mesh, wood grain, hair strands, label lettering, extra people
```

## QC expected

- Run `qc_plate.py` with `--kind group` (looser speckle than portrait).
- Machine `QC PASS` after texture is omitted.
- Visual: count=4, board+bowls present, vest is a simple shape, floor is one slab, no cartoon clip-art steam.
- First fail is often speckle on vest/floor → retry with large closed shapes, not more lines.
- Verdict: SHIP → preview and **wait**. No PDF until the user confirms.
- Confirming PDF does **not** change remembered default intensity.

## Common fail → retry

Speckle / pinholes on knit or grain →

```
Redraw textures as LARGE closed shapes. Vest is one garment outline. Floor is one slab. No knit mesh, no wood grain, no hair strands.
```

## Delivery note

`QC SHIP / advanced / group kitchen / four people, named bowls+board+hood as closed shapes`
Then ask: 要輸出成 A4 PDF 嗎？還是繼續修改？
