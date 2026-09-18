# 著色本 — Super Grok 技能

[English](README.md) | [繁體中文](README.zh-TW.md)

這是一份可搬運的 `SKILL.md` 包，名稱 **`coloring-book`**。上傳照片後，代理會先出「保留／省略」清單，再把照片譬成 **Open-Line Plate** 線稿，列出已辨識的圖片元素，然後**停下等你確認**。只有你點頭後才會合成 A4 PDF。

這是 **skill**，不是網站。不要部署成應用程式。不要把多張照片合併成一本書。

公開倉儲：[github.com/g0uv4/coloring-book](https://github.com/g0uv4/coloring-book)

## 安裝

```bash
git clone https://github.com/g0uv4/coloring-book.git ~/.grok/skills/coloring-book
```

換新階段後再用 Grok Build 測試：

```bash
git -C ~/.grok/skills/coloring-book pull
python3 -m pip install -r ~/.grok/skills/coloring-book/requirements.txt
python3 ~/.grok/skills/coloring-book/scripts/check_installation.py ~/.grok/skills/coloring-book
```

**Codex** — clone 到 `~/.codex/skills/coloring-book`  
**Claude Code** — clone 到 `~/.claude/skills/coloring-book`

## 範例提示

```text
Use $coloring-book on this photo.
```

```text
把這張照片變成著色本。
```

看完保留／省略表之後：`依這份畫`

線稿出來之後：

| 你說 | 結果 |
|---|---|
| 輸出 PDF | 只出 A4 PDF — **不改** 預設強度 |
| 兩格 / 四格 / 直式 | 列印包（`--nup 2\|4` 或 `--orientation portrait`） |
| 只改砧板 | 只重畫那一塊 |
| 記住這個風格 / 以後都用高階 | 存成預設強度 |
| 忘記著色本設定 | 刪除已記的設定 |

風格記憶由協調者自己寫入。你不用手動下任何記憶指令。

## 強度

| | 簡單 | 中等 | 高階 |
|---|---|---|---|
| 預設？ | 否 | **是** | 否 |
| 線條 | 稍厚 | 中等毛尖筆 | **與中等相同** |
| 保留 | 最大輪廓 | 主體 + 少數內部 | 照片裡每個可閉合的命名元件 |

詳見 [`references/intensity.md`](references/intensity.md)。

## 流程

1. 盤點照片 + 題材配方  
2. 出保留／省略表並等待  
3. 譬成 Open-Line Plate  
4. 清理 + 品管（線條連續、區塊閉合、**線條平滑無鋸齒**）  
5. 出線稿 + 圖片元素並等待  
6. 你說輸出 PDF → A4（`compose_a4_pdf.py --nup 1\|2\|4`）  
7. 協調者自動記下站著規則與重複習慣

機器品管：[`scripts/qc_plate.py`](scripts/qc_plate.py)  
`validate_coloring.py` 已廢棄。

## 授權

MIT
