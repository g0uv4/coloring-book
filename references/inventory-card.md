# Inventory card — confirm parts before drawing

After the analysis worksheet and **before** `imagine_image_to_image`, show a keep / omit table and **stop**. Do not generate until the user ticks the list (or says 可以依這份畫 / go / generate).

Busy kitchens, tables, and travel scenes need this. Headshots may use a short card (5 lines) but still wait.

## What to show

Use the user's language. Intensity and kind on the first line.

```text
強度：{simple|medium|advanced} · 題材：{portrait|group|pet|food|kitchen-object|architecture|scene}

保留（會畫成閉合區塊）
1. …
2. …

省略（不畫；紋理改成大塊）
- 水印 / 時間戳 / 螢幕 UI
- 針織網、木紋、草叶
- 讀不到的標籤字

要改清單、換強度，或回「依這份畫」。
```

English fallback:

```text
Keep (closed shapes) / Omit (textures → slabs)
Reply with edits, or say generate.
```

## Rules

- Keep list = named photo parts that will appear. Cap at ~12 for medium, ~18 for advanced, ~6 for simple.
- Omit list always includes watermarks, UI, hair strands, fabric weave, wood grain unless they override.
- If they delete a keep-row, do not draw it.
- If they add a row that is **not in the photo**, refuse that row (照片裡沒有，不加).
- Textures they want to keep still become **one closed mass**, not a hatch.
- After they confirm the card, generate once. Do not re-ask the card unless they change intensity or upload a new photo.

## Skip the wait only when

- they already listed keep/omit in the same message as the photo, and
- the scene is a simple headshot with ≤ 4 facts

Still print the card in one short block so they can correct it after the plate if needed.
