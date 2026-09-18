# Coloring Book — Super Grok skill

A portable `SKILL.md` pack named **`coloring-book`**. Upload a photograph; the agent translates it into an **Open-Line Plate** coloring page, shows it, and **waits**. An A4 PDF is composed only after you confirm.

This is a **skill**, not a website. Do not deploy it as an app.

This is not a grayscale filter. Intensity is **simple**, **medium** (default), or **advanced** — advanced keeps more *named parts from the photo*, not denser hatch.

Style is locked in text. **No third-party coloring pages are bundled.**

Public repo: [github.com/g0uv4/coloring-book](https://github.com/g0uv4/coloring-book)

## Install

```bash
git clone https://github.com/g0uv4/coloring-book.git ~/.grok/skills/coloring-book
```

Then start a new agent session.

**Codex**

```bash
git clone https://github.com/g0uv4/coloring-book.git ~/.codex/skills/coloring-book
```

**Claude Code**

```bash
git clone https://github.com/g0uv4/coloring-book.git ~/.claude/skills/coloring-book
```

Needs Python 3 + Pillow + numpy for cleanup / QC / A4 composition:

```bash
python3 -m pip install -r ~/.grok/skills/coloring-book/requirements.txt
python3 ~/.grok/skills/coloring-book/scripts/check_installation.py ~/.grok/skills/coloring-book
```

## Example prompts

```text
Use $coloring-book on this photo.
```

```text
把這張照片變成著色本。
```

```text
同一張照片做簡單、中等、高階三張著色頁。
```

After the plate appears, say **輸出 PDF** or describe what to change.

## Intensity

| | simple | medium | advanced |
|---|---|---|---|
| Default? | no | **yes** | no |
| Line | slightly thicker | medium felt-tip | **same as medium** |
| Keep | largest silhouettes | main structure | every named photo part that can be a closed shape |
| Still forbidden | mandala, hair strands, photoreal, broken lines | same | same — never denser hatch, never cartoon clip-art effects |

See [`references/intensity.md`](references/intensity.md).

## Flow

1. Inventory the photo  
2. Translate to Open-Line Plate  
3. Cleanup + QC inspector  
4. **Show the plate and wait**  
5. On confirm → A4 PDF (300 dpi, 14 mm margins)

Machine QC: [`scripts/qc_plate.py`](scripts/qc_plate.py)  
SOP: [`references/qc-inspector.md`](references/qc-inspector.md)

## Style lock

Open-Line Plate — see [`references/style-guide.md`](references/style-guide.md). Portraits use [`references/portrait-rules.md`](references/portrait-rules.md).

## Layout

```
coloring-book/
├── SKILL.md
├── README.md
├── LICENSE
├── requirements.txt
├── agents/openai.yaml
├── references/
└── scripts/
```

## License

MIT
