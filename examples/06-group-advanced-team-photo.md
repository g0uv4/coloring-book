# Example 06 — Group / advanced / team photo

## Teaching goal

Advanced on a group means **more named garments and props per person**, not a denser hatch and not extra teammates.

## User request

```text
團隊合照變著色頁，高階細節，背心與工牌要留。
Advanced coloring page of this team photo. Keep lanyards and badges.
```

## Photo facts (invented)

Five adults in two rows against an office wall. Front row seated. One wears a lanyard; one holds a notebook; one has round glasses.

## Analysis worksheet

```
USER_PHOTO path: /uploads/team-five.jpg
Kind: group
Orientation: landscape
Crop: half body group
Subject count: 5 people, 0 animals

Left-to-right subjects:
1. adult, short hair, no glasses, polo, standing back-left
2. adult, bob hair, round glasses, blouse, standing back-center
3. adult, bun, lanyard + badge, cardigan, standing back-right
4. adult, short hair, notebook in hands, seated front-left
5. adult, shoulder-length hair, crew sweater, seated front-right

Must-keep distinctive facts:
- count = 5
- two-row overlap
- round glasses on person 2
- lanyard + badge on person 3
- notebook on person 4

Background masses:
- wall
- optional table edge

Drop from the photo:
- readable company logo / badge text
- ceiling fixture detail
- pores, fabric weave
```

## Intensity decision

`advanced` — user asked 高階 and named accessories.

## Filled inventory

```
Kind: group
Crop: half body
Orientation: landscape
People: 5 adults; two rows; person 2 round glasses; person 3 lanyard+badge; person 4 notebook
Animals: none
Pose: team portrait, back row standing, front row seated
Must-keep details: count=5, glasses, lanyard, badge as a rectangle, notebook
Advanced extra parts: lanyard loop, badge rectangle, notebook rectangle, collar on cardigan, table edge
Background masses: wall, table edge
Do not draw: extra teammates, readable trademarks, UI
```

## QC expected

- Machine `QC PASS`
- Visual: count=5, lanyard present, no official logo lettering, line weight = medium, faces not traced
- Verdict: SHIP → preview the plate and **wait**. No PDF until the user confirms.

## Common fail → retry

Too empty for advanced → add named objects (lanyard, badge, notebook) as closed shapes. Do not add hatch.

## Delivery note

`QC SHIP / advanced / five people, lanyard+badge+notebook as closed shapes`
Then ask: 要輸出成 A4 PDF 嗎？還是繼續修改？
