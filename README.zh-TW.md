[English](README.md) | 繁體中文

# 著色本 — Super Grok skill

這是一份可搶的 `SKILL.md` 包，名稱 **`coloring-book`**。上傳一張照片；agent 先出保留／省略清單，再譬成 **Open-Line Plate** 線稿，顯示線稿與圖片元素後**等你確認**。只有你點頭，才會合成 A4 PDF。

這是 **skill**，不是網站。不要部署成 App。不要把多張照片合併成一本書。

公開倉庫：[github.com/g0uv4/coloring-book](https://github.com/g0uv4/coloring-book)

## 安裝

```bash
git clone https://github.com/g0uv4/coloring-book.git ~/.grok/skills/coloring-book
```

接著開一次新的 agent 階段。用 Grok Build 測試前先 pull：

```bash
git -C ~/.grok/skills/coloring-book pull
python3 -m pip install -r ~/.grok/skills/coloring-book/requirements.txt
python3 ~/.grok/skills/coloring-book/scripts/check_installation.py ~/.grok/skills/coloring-book
```

**Codex** — clone 到 `~/.codex/skills/coloring-book`  
**Claude Code** — clone 到 `~/.claude/skills/coloring-book`

## 例句

```text
Use $coloring-book on this photo.
```

```text
把這張照片變成著色本。
```

看完保留／省略表之後說：`依這份畫`

線稿出來後會列出「圖片元素」（眼鏡、頭髮、人數、雲朵…）。可以直接指：

| 你說 | 結果 |
|---|---|
| 輸出 PDF | 只出 A4 PDF — **不會**改預設強度 |
| 只改眼鏡 / 雲多一塊 | 局部重畫那個元素 |
| 兩格 / 四格 / 直式 | 列印包 |
| 記住這個風格 / 以後都用高階 | 協調者自己寫入記憶（你不用打指令） |
| 忘記著色本設定 | 協調者刪掉記住的設定 |

## 強度

| | 簡單 | 中等 | 高階 |
|---|---|---|---|
| 預設？ | 否 | **是** | 否 |
| 線 | 稍厚 | 中等毛筆 | **與中等相同** |
| 保留 | 最大輪廓 | 主要結構 | 照片裡能閉合的命名元件 |

高階不是更密的線，而是更多照片裡的東西。詳見 [`references/intensity.md`](references/intensity.md)。

## 流程

1. 盤點照片 + 題材配方  
2. 出保留／省略表並等你勾  
3. 譬成 Open-Line Plate  
4. 清理 + 品管（閉合線、無洩漏、**線條平滑無鋸齒**）  
5. 出線稿 + 圖片元素表並等你  
6. 你說「輸出 PDF」→ A4（默認 1-bit CCITT，不走 JPEG）  
7. 你說「記住」或同一種風格調了兩次 → 協調者自己寫入記憶

品管腳本：[`scripts/qc_plate.py`](scripts/qc_plate.py)  
`validate_coloring.py` 已廢棄。

## 授權

MIT
