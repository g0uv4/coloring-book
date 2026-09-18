# Inventory card

Name the parts you will draw. Do **not** replace the plate preview.

The user wants to **see the coloring page in chat**. A keep/omit list is not a preview.

## When to wait vs draw now

| Situation | Do this |
|---|---|
| Pet, portrait, or one object + a photo already attached | Print a **short** keep/omit block **and generate this turn**. Do not stop. |
| User said 先畫 / 給我看 / 直接畫 / generate | Generate this turn even if the scene is busy. |
| Kitchen, group, travel clutter, many unnamed objects | Show the card and **wait** for `依這份畫` |

Busy kitchens still need the wait. A single cat does not.

## What to show

Use the user's language.

```text
強度：{simple|medium|advanced} · 題材：{portrait|group|pet|food|kitchen-object|architecture|scene}

保留
1. …

省略
- 水印 / 時間戳 / 螢幕 UI
- 細毛 / 織紋 / 木紋
```

If you generate this turn, add one line: `下面是線稿預覽。要輸出 A4 PDF 還是改元件？`
If you wait, add: `要改清單、換強度，或回「依這份畫」。`

## Rules

- Keep list = named photo parts. Cap ~6 simple, ~12 medium, ~18 advanced.
- Omit always includes watermarks, UI, hair strands, fabric weave, wood grain unless they override.
- Do not add objects that are not in the photo.
- After they confirm a waited card, generate once. Do not re-ask the card unless intensity or photo changes.
