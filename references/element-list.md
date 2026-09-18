# Image elements — after the plate

After QC SHIP, show the clean plate **and** a list of **recognized parts already on that plate**. This is not a new analysis of the photo and not a request for the user to invent objects.

The list tells them what they can say `只改X` / `拿掉X` / `眼鏡再簡` about.

## Format (user language)

```text
圖片元素（可以說「只改X」或「拿掉X」）
- 人數：{n}
- 眼鏡
- 頭髮（馬尾 / 瀏海 / …）
- 衣服條紋
- 砧板 / 雞刀
- 雲朵 / 穹頂
```

English:

```text
Elements on this plate (say "only change X" or "drop X"):
- people count: {n}
- glasses
- hair
- …
```

## What may appear

Only parts that **are drawn on the plate** (or were confirmed on the keep list and survived QC):

- count of people / pets
- glasses, hat, earrings, watch
- hair silhouette / bun / bangs
- clothing blocks or stripes
- named props (phone, board, bowl, faucet, collar)
- large background masses actually drawn (cloud band, hood, doorway)

## What must not appear

- omitted textures (knit mesh, wood grain) — those were dropped
- things not in the photo
- QC numbers, file paths, intensity jargon unless they asked
- a second inventory card (that already happened before generate)

Cap at ~12 lines. Group tiny bits (`藍瓜+香菇碗` as one line).

If they name a listed element → local redraw (6c) or drop it and regenerate once.
If they name something not listed and not in the photo → refuse that add.
