# Plate elements — list after generate

After QC SHIP and **with the plate image**, list the named parts the coordinator already recognized. This is not a new analysis pass. Copy from the confirmed keep/omit card, then drop anything that did not actually land on the plate.

The user should see what they can ask to change (`只改眼鏡`, `雲多一塊`, `人數少一個`) without guessing.

## What to print

Use the user's language. Keep it scannable on a phone (about 8–16 rows).

```text
圖片元素（可指定要改的）
人物：人數 {N}；{眼鏡 / 馬尾 / 條紋衣 / 手勢}
配件：{手錶、手機、磚板、刀}
背景：{抽油煙機、水槽、雲朵、地板}
省略：{木紋、針織網、標籤字、水印}
```

English fallback:

```text
Recognized elements (ask to change any of these)
People: count N; glasses / ponytail / striped shirt
Props: watch, phone, board, knife
Background: hood, sink, clouds, floor
Omitted: wood grain, knit mesh, labels, watermark
```

## Rules

- Only list parts that are **on this plate** or were **intentionally omitted**. Do not invent clouds if the photo had none.
- Group similar items (`眼鏡 ×4` not four separate rows).
- Names must be short enough to reuse in a local-redraw request (`只改磚板`).
- After a local redraw, reprint the list (mark what changed).
- This list is **not** the keep/omit card. The card happens before generate. The element list happens after the plate exists.
