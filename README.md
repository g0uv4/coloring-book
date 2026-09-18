# Coloring Book — Super Grok skill

[English](README.md) | [繁體中文](README.zh-TW.md)

A portable `SKILL.md` pack named **`coloring-book`**. Upload a photograph; the agent shows a keep/omit card, translates it into an **Open-Line Plate**, lists recognized image elements, and **waits**. An A4 PDF is composed only after you confirm.

This pack is a **skill**. Do not deploy it as an app. Do not merge many photos into one book.

Public repo: [github.com/g0uv4/coloring-book](https://github.com/g0uv4/coloring-book)

## Install

```bash
git clone https://github.com/g0uv4/coloring-book.git ~/.grok/skills/coloring-book
```

Then start a new agent session. Pull before Grok Build tests:

```bash
git -C ~/.grok/skills/coloring-book pull
python3 -m pip install -r ~/.grok/skills/coloring-book/requirements.txt
python3 ~/.grok/skills/coloring-book/scripts/check_installation.py ~/.grok/skills/coloring-book
```

**Codex** — clone to `~/.codex/skills/coloring-book`  
**Claude Code** — clone to `~/.claude/skills/coloring-book`

## Example prompts

```text
Use $coloring-book on this photo.
```

```text
把這張照片變成著色本。
```

After the keep/omit card: `依這份畫`

After the plate:

| You say | Result |
|---|---|
| 輸出 PDF | A4 PDF only — does **not** change default intensity |
| 兩格 / 四格 / 直式 | print pack (`--nup 2\|4` or `--orientation portrait`) |
| 只改砧板 | local redraw of that region |
| 記住這個風格 / 以後都用高階 | store default intensity |
| 忘記著色本設定 | delete stored profile |

The coordinator writes style memory itself. You never type a memory command.

## Intensity

| | simple | medium | advanced |
|---|---|---|---|
| Default? | no | **yes** | no |
| Line | slightly thicker | medium felt-tip | **same as medium** |
| Keep | largest silhouettes | main structure | every named photo part that can be a closed shape |

See [`references/intensity.md`](references/intensity.md).

## Flow

1. Inventory the photo + subject recipe  
2. Show keep/omit card and wait  
3. Translate to Open-Line Plate  
4. Cleanup + QC (closed lines, no leaks, **smooth ink**)  
5. Show the plate + image elements and wait  
6. On 輸出 PDF → A4 (`compose_a4_pdf.py --nup 1\|2\|4`)  
7. Coordinator persists standing style and repeated habits

Machine QC: [`scripts/qc_plate.py`](scripts/qc_plate.py)  
`validate_coloring.py` is deprecated.

## License

MIT
