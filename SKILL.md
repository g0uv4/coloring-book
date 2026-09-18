---
name: coloring-book
description: Convert an uploaded photograph into a coloring-book page. Inventory first, QC, then preview. A4 vector PDF only after the user confirms. Use when they upload a photo and ask for a coloring book, coloring page, 著色本, 著色頁, 線稿, or line art for coloring. Never grayscale or edge-detect. Never PDF before confirmation.
license: MIT
compatibility: Grok, Codex, ChatGPT, Claude Code, Antigravity, Gemini CLI, Kimi, Cursor, any agent with image generation plus a filesystem
metadata:
  version: "1.9.4"
  short-description: Photo to Open-Line Plate; host image backend; preview PNG then PDF
  author: g0uv4
---

# Coloring Book (Open-Line Plate)

Translate one uploaded photo into a printable coloring page. **Wait** on the keep/omit card. After QC, show the plate + 圖片元素 and **wait**. Compose an A4 PDF only after they agree.

Not a website. Not a multi-photo book. Never tell the user to type `/memory-with-docs`.

If no photograph is attached, ask for one and stop.

## Speed (do this)

- Run `check_installation.py` **once per session**, not every photo.
- Load only the refs you need this turn. Do **not** open examples 01–07 unless the kind matches.
- Generate the plate **once**. QC overlay only if machine FAIL.
- After confirm: `vectorize_plate.py` → PDF. Do **not** also run `compose_a4_pdf.py` unless vectorize fails.
- Cleanup long-edge default 2400 is enough. Do not upscale to 4K.
- Never run `pipeline.py --pdf` before the user confirms the PNG in chat.

## Locked style

Read [references/style-guide.md](references/style-guide.md) and [references/intensity.md](references/intensity.md).

Medium-thick black ink, paper-white interiors, closed loops. Intensity changes **which photo parts you keep**, not line density.

No gray fills, no broken lines, no clip-art flames, no mandala hatch, no knit/wood/brick texture grids. Textures = one closed slab. Filled-black subjects (B&W photo / silhouette) are not a coloring book.

| Intensity | When |
|---|---|
| simple | 簡單 / 小孩 |
| medium | default / 中等 |
| advanced | 高階 / 更多元件 — more **named parts**, same stroke |

## Workflow

### 1. Install (once)

```bash
python3 scripts/check_installation.py
```

### 2. Inspect

Read the photo. Worksheet: [references/analysis-method.md](references/analysis-method.md).
Kind + recipe: [references/recipes.md](references/recipes.md) / [references/portrait-rules.md](references/portrait-rules.md) only if needed.
Memory: [references/style-memory.md](references/style-memory.md) — recall silently. This-turn words win.

### 2d. Inventory card — wait

[references/inventory-card.md](references/inventory-card.md). Show keep/omit. **Stop.** Skip wait only for a simple headshot with ≤ 4 facts already listed.

### 3. Generate

Read [references/image-backend.md](references/image-backend.md). Then [references/prompt-templates.md](references/prompt-templates.md) + confirmed keep list.

Same Open-Line prompt. Image-to-image on `USER_PHOTO` only. Route by host:

| Host | Tool |
|---|---|
| Grok / SuperGrok | Imagine |
| OpenAI harness / Codex / ChatGPT | ChatGPT Images |
| Antigravity / Gemini CLI | Nano Banana |
| Kimi / Kimi Code | Kimi built-in image generation |
| Claude Code | first connected image tool (MCP / plugin) |
| Cursor / Windsurf / Cline / OpenCode / Copilot | first image-to-image tool in this session |
| Anything else | that host's native image-edit tool |

Aspect 2:3 or 3:2. No third-party style images. Save as `plate-raw.png`. Name the backend in the preview note.

### 4. Cleanup

```bash
python3 scripts/cleanup_lines.py plate-raw.png plate-clean.png --threshold 128 --min-long-edge 2400 --smooth 1.2
```

### 5. QC

[references/qc-inspector.md](references/qc-inspector.md).

```bash
python3 scripts/qc_plate.py plate-clean.png --report qc-report.json
```

Add `--overlay qc-overlay.png` **only** on FAIL.

SHIP → preview. First fail → one retry (or re-cleanup if the only fail is jaggies). Second fail → stop, no PDF. A filled B&W photo / silhouette is FAIL — regenerate, do not PDF.

### 6. Preview — wait

**Attach `plate-clean.png` in the chat** so the user sees the line art without opening a PDF. Then list 圖片元素 ([references/element-list.md](references/element-list.md)). Ask whether to output A4 PDF, print pack, or edit an element.

Hard rules for this turn:

- Do **not** run `vectorize_plate.py`, `compose_a4_pdf.py`, or `pipeline.py --pdf`.
- Do **not** attach a PDF yet. The PNG is the preview.
- If QC FAIL because the plate is a filled B&W photo / silhouette, say so and regenerate. Do not hide the fail inside a PDF.

| User | Action |
|---|---|
| 輸出 / PDF / 可以 | step 7. Do not write default intensity. |
| 兩格 / 四格 / 直式 | step 7 with [print-pack.md](references/print-pack.md) |
| 只改X | [local-redraw.md](references/local-redraw.md) then QC + preview |
| 記住 / 以後都用X | coordinator writes memory. PDF still needs yes. |
| 忘記著色本設定 | delete coloring-book profile |

### 6b. Memory

Coordinator writes. Never name the tool to the user. Reply `已記住…`. Layer C: same habit twice this chat → persist. `輸出 PDF` does not change default intensity.

### 7. Deliver — vector PDF for ibon

[references/ibon-print.md](references/ibon-print.md) and [references/pdf-spec.md](references/pdf-spec.md).

```bash
python3 scripts/vectorize_plate.py plate-clean.png plate.svg \
  --pdf plate-a4.pdf --orientation portrait --margin-mm 14
```

Add `--jpeg plate-a4.jpg` only if they asked for a picture file.
If vectorize fails:

```bash
python3 scripts/compose_a4_pdf.py plate-clean.png plate-a4.pdf \
  --dpi 300 --margin-mm 14 --orientation portrait --nup 1
```

`--nup 2|4` uses compose (copies of the same plate), not vectorize.
Never upload SVG to ibon. Tell them: A4 黑白一般用紙，100% / 實際大小。

## Safety

Family photos are in scope. Refuse sexualized / gore / official character sheets. No watermarks. No other people's coloring pages in the repo.
