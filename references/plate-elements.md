# Plate elements — list after generate

After QC SHIP and **with the plate image**, list the named parts the coordinator already recognized. This is not a new analysis pass. Copy from the confirmed keep/omit card, then drop anything that did not actually land on the plate.

The user should see what they can ask to change (`只改眼鏡`, `雲多一塊`, `人數少一個`) without guessing.

## What to print

Use the user's language. Keep it scannable on a phone (about 8–16 rows).

```text
圖片元素（可以說「只改X」或「拿掉X」）
- 人數：{n}
- 眼鏡
- 頭髮（馬尾 / 瀏海 / …）
- 衣服條紋
- 砧板 / 雞刀
- 雲朵 / 穹頂
```

English fallback:

```text
Elements on this plate (say "only change X" or "drop X"):
- people count: {n}
- glasses
- hair
- …
```

## Rules

- Only list parts that are **on this plate** or were **intentionally omitted**. Do not invent clouds if the photo had none.
- Group similar items (`眼鏡 ×4` not four separate rows).
- Names must be short enough to reuse in a local-redraw request (`只改砧板`).
- After a local redraw, reprint the list (mark what changed).
- This list is **not** the keep/omit card. The card happens before generate. The element list happens after the plate exists.
