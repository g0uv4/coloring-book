# Photo Coloring Book — Super Grok skill

A portable `SKILL.md` pack. Upload a photograph to Grok (or any agent that can load this skill) and get a **print-ready A4 coloring page PDF** in the locked **Open-Line Plate** style.

This is not a grayscale filter. The agent rebuilds the photo as a coloring-book illustration: black outlines, empty white regions, simplified faces. Intensity is **simple**, **medium** (default), or **advanced** — advanced keeps more *named parts from the photo*, not denser hatch.

Public repo: [github.com/g0uv4/photo-coloring-book](https://github.com/g0uv4/photo-coloring-book)

## Install

```bash
git clone https://github.com/g0uv4/photo-coloring-book.git
```

Copy the cloned folder into a skills path, then start a new agent session.

**Grok Build / Super Grok**

```bash
cp -R photo-coloring-book ~/.grok/skills/photo-coloring-book
# or, project-local:
cp -R photo-coloring-book .grok/skills/photo-coloring-book
```

**Codex**

```bash
cp -R photo-coloring-book ~/.codex/skills/photo-coloring-book
```

**Claude Code**

```bash
cp -R photo-coloring-book ~/.claude/skills/photo-coloring-book
```

Needs Python 3 + Pillow + numpy for cleanup / QC / A4 composition:

```bash
python3 -m pip install -r photo-coloring-book/requirements.txt
python3 photo-coloring-book/scripts/check_installation.py photo-coloring-book
```

## Example prompts

```text
Use $photo-coloring-book on this photo. Turn it into a coloring page and give me an A4 PDF.
```

```text
把這張照片變成著色本，輸出 A4 PDF。用中等細節。
```

```text
同一張照片做簡單、中等、高階三張著色頁，各一頁 A4。
```

```text
Make a 3-page coloring book from these photos, advanced intensity, one A4 page each.
```

## Intensity

| | simple | medium | advanced |
|---|---|---|---|
| Default? | no | **yes** | no |
| Line | slightly thicker | medium felt-tip | **same as medium** |
| Keep | largest silhouettes | main structure | every named photo part that can be a closed shape |
| Still forbidden | mandala, hair strands, photoreal, broken lines | same | same — never denser hatch, never cartoon clip-art effects |

See [`references/intensity.md`](references/intensity.md).

## QC inspector

A **品管** step must pass before the A4 is composed:

- continuous lines (no dashed / dangling ends)
- closed colorable regions (no crayon leaks)
- ink purity, region size, speckle, stroke thickness
- visual identity, intensity honesty, photo-accurate effects

Machine: [`scripts/qc_plate.py`](scripts/qc_plate.py)  
SOP: [`references/qc-inspector.md`](references/qc-inspector.md)

## What you get

1. A black-and-white coloring plate (PNG)
2. The same plate centered on an A4 PDF (300 dpi, 14 mm margins)

## Style lock

Open-Line Plate — see [`references/style-guide.md`](references/style-guide.md). Portraits use [`references/portrait-rules.md`](references/portrait-rules.md). Mandala / zentangle density is out of scope for photo conversion at every intensity.

## Layout

```
photo-coloring-book/
├── SKILL.md
├── README.md
├── LICENSE
├── requirements.txt
├── agents/openai.yaml
├── assets/style-references/   4 original line plates (style only)
├── references/                law, intensity, QC inspector, prompts, A4 spec
└── scripts/                   cleanup, qc_plate, validate, A4 PDF
```

## License

MIT
