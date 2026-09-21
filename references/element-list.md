# Image elements — after the plate

After QC SHIP, show the clean plate **and** a list of **recognized parts already on that plate**.

The list tells them what they can say `只改X` / `拿掉X` / `眼鏡再簡` / `天空用菱格紋` about.

## Format (user language)

```text
圖片元素（可以說「只改X」「拿掉X」或加格紋）
- 人數：{n}
- 眼鏡
- 頭髮
- 天空 / 海面 / 道路
```

If sky / sea / road / wall / floor is listed, add:

```text
大面積可加格紋：菱格紋、百步蛇紋、變形蟲紋、山形紋、波浪帶紋
例如「天空用菱格紋」
```

## Rules

- Only list parts on this plate.
- Cap at ~12 lines.
- Pattern fills: [pattern-fills.md](pattern-fills.md). Opt-in. Large fields only.
