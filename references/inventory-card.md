# Inventory card — show before generate

After the analysis worksheet and **before** calling the image model, show the user a keep / omit table. Wait for them to tick it. Kitchen and other cluttered scenes need this most.

Do not generate in the same turn as the card unless they already said `直接畫` / `skip inventory` / `不用確認清單`.

## What to list

From the worksheet, split facts into two columns. Keep the list short enough to scan on a phone (about 8–16 rows total).

```text
強度：{simple|medium|advanced}
場景：{kind} / {crop}

保留
- {named part}
- …

省略
- 水印 / 時間戳 / UI
- {texture that would speckle: knit, wood grain, hair strands}
- {tiny objects that cannot close}

回「可以畫」或勾選要加／減的元件。
```

English fallback:

```text
Intensity: {simple|medium|advanced}
Kind: {kind}

Keep
- …

Omit
- watermarks / timestamps / UI
- …

Reply "draw it" or name parts to add/drop.
```

## How they answer

| User says | Action |
|---|---|
| 可以畫 / 畫吧 / draw it / OK | generate with this card |
| 加 {X} / 要留 {X} | move X to Keep, then generate (or re-show if the list changed a lot) |
| 去掉 {Y} / 不要 {Y} | move Y to Omit, then generate |
| 換強度 | change intensity, re-show the card |
| 直接畫 / skip inventory | generate now; do not ask again this session unless the photo changes |

Do not treat `可以畫` as `輸出 PDF`. The card is not the plate.

## Intensity effect on the card

- `simple` — Keep is only the largest silhouettes. Extra named objects go to Omit.
- `medium` — Keep main subjects + a few easy inner facts.
- `advanced` — Keep every named photo part that can be a closed loop. Still Omit textures and anything that would break.

## After they tick

Copy the final Keep / Omit lines into the prompt inventory. Then generate (workflow step 3).
