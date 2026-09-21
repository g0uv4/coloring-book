---
name: coloring-book
description: Convert an uploaded photograph into a coloring-book page. After the plate preview, if large empty fields exist, judge and offer five pattern-fill schemes for this photo. A4 PDF only after the user confirms. Use when they upload a photo and ask for a coloring book, coloring page, 著色本, 著色頁, 線稿, or line art for coloring. Never fill interiors black. Never PDF before confirmation.
license: MIT
compatibility: Grok, Codex, ChatGPT, Claude Code, Antigravity, Gemini CLI, Kimi, Cursor, any agent with an image tool plus a filesystem
metadata:
  version: "1.9.7"
  short-description: Photo to Open-Line Plate; five judged pattern schemes; preview PNG; vector A4 PDF after confirm
  author: g0uv4
---

# Coloring Book (Open-Line Plate)

Translate one uploaded photo into a printable coloring page.

If no photograph is attached, ask for one and stop.

Not a website. Not a multi-photo book. Never tell the user to type `/memory-with-docs`.

## Hard stops

1. Pet / portrait / one object + a photo → print a short keep list **and draw this turn**. Do not stop at the list.
2. After QC, **embed `plate-clean.png` as an image in the chat**.
3. Preview turn: no `vectorize_plate.py`, no `compose_a4_pdf.py`, no `pipeline.py --pdf`. Do not say 「走管線」.
4. Dark fur / hair / clothes stay white pockets. A filled poster is QC FAIL.
5. If the plate has a large empty field, **judge five fill schemes for this photo** ([references/pattern-fills.md](references/pattern-fills.md)). Do not reuse the same five names every time. Do not apply a pattern until they pick one.

## Speed

- `check_installation.py` once per session.
- Load only the refs you need.
- Generate once. QC overlay only on FAIL.
- Cleanup `--min-long-edge 2400`.

## Locked style

Medium-thick black outlines, paper-white interiors, closed loops. Intensity changes which photo parts you keep, not line density.

## Workflow

### 1–5

Install → inspect → inventory → host image tool → cleanup → QC as in 1.9.6. Host table: [references/image-backend.md](references/image-backend.md).

### 6. Preview in chat — wait

Embed `plate-clean.png`. List 圖片元素.
If sky / sea / road / wall / floor exists, print **five judged schemes** from [pattern-fills.md](references/pattern-fills.md). Ask PDF or edit. Stop.

| User | Action |
|---|---|
| 輸出 / PDF / 可以 | next turn step 7 |
| 1–5 / `天空用…` | apply that scheme to the named region → QC → embed PNG |
| 只改X | local-redraw → QC → embed PNG |
| 記住 / 以後都用X | write memory. PDF still needs yes. |

### 7. Deliver PDF — only after they said yes

`vectorize_plate.py` → A4. Fallback `compose_a4_pdf.py`. Never upload SVG to ibon.

## Safety

Family photos in scope. Refuse sexualized / gore / official character sheets. Pattern schemes are geometric, not ceremonial indigenous works.
