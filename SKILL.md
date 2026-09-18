---
name: coloring-book
description: Convert an uploaded photograph into a coloring-book page. For a pet or portrait, draw in the same turn and embed the PNG in chat. A4 PDF only after the user confirms. Use when they upload a photo and ask for a coloring book, coloring page, 著色本, 著色頁, 線稿, or line art for coloring. Never fill interiors black. Never PDF before confirmation.
license: MIT
compatibility: Grok, Codex, ChatGPT, Claude Code, Antigravity, Gemini CLI, Kimi, Cursor, any agent with an image tool plus a filesystem
metadata:
  version: "1.9.5"
  short-description: Photo to Open-Line Plate; embed PNG in chat; vector A4 PDF after confirm
  author: g0uv4
---

# Coloring Book (Open-Line Plate)

Translate one uploaded photo into a printable coloring page.

If no photograph is attached, ask for one and stop.

Not a website. Not a multi-photo book. Never tell the user to type `/memory-with-docs`.

## Hard stops

1. Pet / portrait / one object + a photo → print a short keep list **and draw this turn**. Do not stop at the list. See [references/inventory-card.md](references/inventory-card.md).
2. After QC, **embed `plate-clean.png` as an image in the chat**. A path, a PDF, or a list is not a preview. See [references/preview-in-chat.md](references/preview-in-chat.md).
3. Preview turn: do **not** run `vectorize_plate.py`, `compose_a4_pdf.py`, or `pipeline.py --pdf`. Do not say 「走管線」.
4. Dark fur / hair / clothes stay **white pockets** with outlines. A filled poster is QC FAIL. Retry once. Never hide it in a PDF.

## Speed

- `check_installation.py` once per session.
- Load only the refs you need. Do not dump examples 01–07.
- Generate once. QC overlay only on FAIL.
- Cleanup `--min-long-edge 2400`.

## Locked style

[references/style-guide.md](references/style-guide.md) and [references/intensity.md](references/intensity.md).

Medium-thick black outlines, paper-white interiors, closed loops. Hair, fur, clothes, furniture, sky stay white. Only pupils / a tiny nose / a button may be solid black.

| Intensity | When |
|---|---|
| simple | 簡單 / 小孩 |
| medium | default / 中等 |
| advanced | 高階 — more named parts, same stroke, still white interiors |

## Workflow

### 1. Install (once)

```bash
python3 scripts/check_installation.py
```

### 2. Inspect

[references/analysis-method.md](references/analysis-method.md).
Pet / dark object: [references/recipes.md](references/recipes.md).
Memory: [references/style-memory.md](references/style-memory.md) — recall silently.

### 2d. Inventory

[references/inventory-card.md](references/inventory-card.md).

| Situation | Action |
|---|---|
| Pet, portrait, or one object + photo attached | Short keep/omit **and generate this turn** |
| User said 先畫 / 給我看 / 直接畫 | Generate this turn |
| Kitchen / group / clutter | Show the card and wait for `依這份畫` |

### 3. Generate — this host's image tool

[references/image-backend.md](references/image-backend.md) and [references/prompt-templates.md](references/prompt-templates.md).

| Host | Tool |
|---|---|
| Grok | Imagine / `imagine_image_to_image` |
| OpenAI / Codex | `image_gen` / ChatGPT Images |
| Antigravity / Gemini CLI | Nano Banana Pro, else Nano Banana 2 |
| Kimi Agent | `generate_image` |
| Claude Code / Cursor / others | first image-edit tool already in this session |

Image-to-image on `USER_PHOTO`. Aspect 2:3 or 3:2. Save `plate-raw.png`. If no image tool exists, stop.

### 4. Cleanup

```bash
python3 scripts/cleanup_lines.py plate-raw.png plate-clean.png --threshold 128 --min-long-edge 2400 --smooth 1.2
```

### 5. QC

[references/qc-inspector.md](references/qc-inspector.md).

```bash
python3 scripts/qc_plate.py plate-clean.png --report qc-report.json
```

Overlay only on FAIL. Fill / too-dark / not-enough-white → retry with the dark-subject add-on. QC FAIL = show the PNG + reason, **no PDF**.

### 6. Preview in chat — wait

[references/preview-in-chat.md](references/preview-in-chat.md) and [references/element-list.md](references/element-list.md).

Embed `plate-clean.png`. List 圖片元素. Ask `要輸出成 A4 PDF 嗎？還是繼續修改？` Stop.

| User | Action |
|---|---|
| 輸出 / PDF / 可以 | **next turn** step 7 |
| 兩格 / 四格 / 直式 | next turn print-pack |
| 只改X | [local-redraw.md](references/local-redraw.md) → QC → embed PNG again |
| 記住 / 以後都用X | write memory. PDF still needs yes. |

### 6b. Memory

Coordinator writes. Never name the tool. Reply `已記住…`. `輸出 PDF` does not change default intensity.

### 7. Deliver PDF — only after they said yes

```bash
python3 scripts/vectorize_plate.py plate-clean.png plate.svg \
  --pdf plate-a4.pdf --orientation portrait --margin-mm 14
```

If vectorize fails, `compose_a4_pdf.py`. Never upload SVG to ibon.

## Safety

Family photos are in scope. Refuse sexualized / gore / official character sheets.
