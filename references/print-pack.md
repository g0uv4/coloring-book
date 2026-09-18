# Print pack

Single-page A4 is the default. Extra layouts are **print packs**, still one plate (or copies of it), never a multi-photo book.

## Flags for `scripts/compose_a4_pdf.py`

| Flag | Meaning |
|---|---|
| `--orientation auto\|portrait\|landscape` | page direction |
| `--orientation portrait` | **force portrait A4** even if the plate is wide (letterbox the extra width) |
| `--nup 1` | default, one plate per page |
| `--nup 2` | two copies stacked on portrait A4 (kids / classroom) |
| `--nup 4` | 2×2 copies on portrait A4 |

Always `--dpi 300 --margin-mm 14` unless they ask otherwise.

```bash
# default
python3 scripts/compose_a4_pdf.py plate-clean.png plate-a4.pdf \
  --dpi 300 --margin-mm 14 --orientation auto --nup 1

# landscape photo forced onto portrait A4
python3 scripts/compose_a4_pdf.py plate-clean.png plate-a4.pdf \
  --orientation portrait --nup 1

# two-up kids pack
python3 scripts/compose_a4_pdf.py plate-clean.png plate-a4-2up.pdf \
  --orientation portrait --nup 2

# four-up
python3 scripts/compose_a4_pdf.py plate-clean.png plate-a4-4up.pdf \
  --orientation portrait --nup 4
```

## When to offer

After they confirm the plate, if they say 小孩、課堂、一頁兩張、四格、直式列印 — use the matching pack. Do not invent a second different drawing.

Do **not** merge different photos onto one PDF here. That book feature is out of scope.

## Visual rules

- Copies share one plate. Gutters 8 mm between tiles, outer margin 14 mm.
- No decorative frame, no page number, no logo on the artwork.
- Title footer only if they asked.
