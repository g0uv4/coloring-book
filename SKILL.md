---
name: photo-coloring-book
description: Convert an uploaded photograph into a print-ready A4 coloring-book page at one of three intensities (simple, medium, advanced). Use when the user uploads a photo and asks for a coloring book, coloring page, 著色本, 著色頁, 線稿, line art for coloring, 簡單/中等/高階細節, or an A4 PDF coloring sheet. Never apply a grayscale or edge-detect filter. Translate the photo into Open-Line Plate illustration, then compose an A4 PDF.
license: MIT
compatibility: Grok, Codex, Claude, any agent with image generation plus a filesystem
metadata:
  version: "1.3.0"
  short-description: Photo to Open-Line Plate A4 coloring PDF (simple / medium / advanced)
  author: Inkplate
---

# Photo Coloring Book (Open-Line Plate)

Turn one user-uploaded photograph into a **printable coloring page**, then place it on an **A4 PDF**.

This is a **translation**, not a filter. Do not desaturate, posterize, Sobel, Canny, or "find edges" on the photo. Rebuild the scene as a coloring-book illustration with one locked style called **Open-Line Plate**, at one of three intensities: **simple**, **medium** (default), **advanced**.

If no photograph is attached, ask for one and stop.

## Locked style — Open-Line Plate

Read [references/style-guide.md](references/style-guide.md) and [references/intensity.md](references/intensity.md) before generating.

One sentence: **medium-thick black ink, pure white interiors, closed continuous shapes, cartoon-illustration of the real subjects.** Intensity only changes **which photo parts you keep**, not how dense or thin the ink is.

| Do | Do not |
|---|---|
| Black lines on paper white | Gray, beige, or colored fills |
| Closed continuous loops a crayon can fill | Broken, dashed, or hairline strokes |
| Keep identity (count, pose, haircut, glasses, clothes) | Invent people, pets, or landmarks that are not in the photo |
| Simplify a face to coloring-book features | Photoreal contour tracing of a face |
| Keep distinctive accessories as simple shapes | Drop glasses, hats, or wheelchair because they are "busy" |
| Effects that match the photo’s silhouette | Clip-art flames, sparkles, campfire tongues |
| Background as large masses | Dense mandala / zentangle fills (forbidden at every intensity) |

Mandala and filigree plates are **out of style** for photo conversion even if the user attached one as a mood image, including at **advanced**. If a line would break because it is too fine, omit that detail.

## Intensity

Read [references/intensity.md](references/intensity.md). Pick **one**:

| Intensity | When | What changes |
|---|---|---|
| `simple` | user says 簡單 / 小孩 / 少一點線 | only the largest silhouettes, slightly thicker lines |
| `medium` | default, or 中等 / 家庭 | main subjects + a few easy inner facts (ages ~8–14) |
| `advanced` | 高階 / 進階 / 更多細節 / 更多元件 | **more named parts from the photo**, same line weight as medium. Never thinner, never denser hatch. Skip any part you cannot close as a loop. |

If they ask for all three, run the pipeline three times on the same photo and deliver three labeled pages.

## Input lock

- `USER_PHOTO` = the photograph uploaded in **this** request. Record its exact local path. Never substitute a bundled reference, a previous result, or a screenshot.
- `STYLE_REFS` = files in `assets/style-references/`. Style only. Never place a style ref in the output.
- `INTENSITY` = `simple` | `medium` | `advanced`
- `PLATE` = the generated coloring page (temporary).
- `CLEAN_PLATE` = `PLATE` after `scripts/cleanup_lines.py`.
- `QC_REPORT` = JSON from `scripts/qc_plate.py`.
- `PDF` = A4 deliverable from `scripts/compose_a4_pdf.py`.

## Tool contract

1. Confirm an image-generation edit tool is callable (`imagine_image_to_image` / `imagine_reference_to_image`, or an images-edits API). If none exist, stop and say so. Do **not** fake the plate with Pillow, OpenCV, Canny, or CSS filters.
2. Use Python scripts only for cleanup, **QC**, and A4 composition — never to draw the picture.
3. Return the plate to the user only after **QC SHIP**. Return the PDF only after `DELIVERY PASS`.
4. If generation, cleanup, QC, or composition fails, name the failed stage and return no final PDF.

## Workflow

### 1. Install check

```bash
python3 scripts/check_installation.py
```

Run it from this skill directory (or pass the directory as argv1). Stop on `INSTALL FAIL`.

### 2. Inspect the photograph

Read `USER_PHOTO` with the environment's image viewer (`read_file` on the path). Then complete the worksheet in [references/analysis-method.md](references/analysis-method.md).

Record, in order:

- kind: `portrait` | `group` | `pet` | `scene` | `object`
- orientation: `portrait` | `landscape` | `square`
- people/pets count, ages-as-appearance (adult/child), hair, glasses, clothing blocks
- pose and crop (headshot / half / full body)
- 5–12 distinctive facts that must survive (a red backpack, a temple roof, a specific dog breed silhouette)
- background reduced to a handful of large masses
- anything that must **not** be drawn (watermarks, timestamps, UI chrome)

Read [references/portrait-rules.md](references/portrait-rules.md) whenever a face is visible.

### 2b. Pick intensity

Use the table above. If unspecified, `medium`.

### 3. Pick 1 style reference

Use [references/style-reference-index.md](references/style-reference-index.md).

| kind | file |
|---|---|
| portrait / group | `assets/style-references/01-portrait.png` |
| scene / landscape | `assets/style-references/02-scene.png` |
| pet | `assets/style-references/03-pet.png` |
| object / still life | `assets/style-references/04-objects.png` |

Inspect the chosen file so you can describe its line weight. Do not copy its subject matter.

### 4. Generate the plate

Build the prompt from [references/prompt-templates.md](references/prompt-templates.md). Fill the inventory block with facts from step 2. Insert the **intensity block** for `simple`, `medium`, or `advanced`. Keep the shared lock verbatim.

**Preferred (2+ images):** `imagine_reference_to_image`

- `image_paths`: `[USER_PHOTO, STYLE_REF]`
- Tell the model IMAGE 0 is content evidence, IMAGE 1 is line-language only
- `aspect_ratio`: `3:4` for portrait/square sources, `4:3` for landscape sources

**Fallback (1 image):** `imagine_image_to_image` on `USER_PHOTO` with the same prompt (style described in text).

**Chat / API fallback:** `POST /v1/images/edits` with the user photo (and the style ref when the API allows multiple images). Model `grok-imagine-image-2.0` or `grok-imagine-image-quality`.

Do not generate from text alone when the user uploaded a photo — identity will drift.

Copy the returned sandbox path to the run folder as `plate-raw.png` (keep the original too).

### 5. Cleanup

```bash
python3 scripts/cleanup_lines.py plate-raw.png plate-clean.png --threshold 128
```

### 5b. QC inspector (品管人員)

Read [references/qc-inspector.md](references/qc-inspector.md) and **become that person**. Do not compose a PDF until they sign off.

```bash
python3 scripts/qc_plate.py plate-clean.png \
  --overlay qc-overlay.png \
  --report qc-report.json
```

Then **look at** `plate-clean.png` and, if it exists, `qc-overlay.png`.

- Red on the overlay = dangling / broken ends.
- Orange = regions that leak until a crayon-sized gap is sealed.
- Visual boxes in `qc-inspector.md` are mandatory even when the machine says PASS (it cannot catch a traced face or the wrong intensity).

Verdict:

- **SHIP** → go to step 6
- **RETRY** (first fail) → regenerate once with the matching add-on in `qc-inspector.md`
- **STOP** (second fail) → show the best plate + QC fails, no PDF

### 6. Compose A4 PDF

Read [references/pdf-spec.md](references/pdf-spec.md).

```bash
python3 scripts/compose_a4_pdf.py plate-clean.png plate-a4.pdf \
  --dpi 300 --margin-mm 14 --orientation auto \
  --preview plate-a4.png
```

Add `--title "..."` only when the user asked for a title. Default is a clean sheet with no header/footer chrome on the artwork.

If Python is unavailable, generate the plate at 3:4 (or 4:3), then use any PDF tool that can place a PNG on an A4 page with ~14 mm margins. Last resort: return the PNG and tell the user to print "fit to A4, no crop".

### 7. Deliver

Show, in this order:

1. The clean plate image
2. The A4 PDF (downloadable)
3. One short note: intensity used, what was simplified, and `QC SHIP`

Do not show the raw pre-cleanup image unless they ask. Do not show style references as if they were the result.

## Safety and rights

- Family photos, including children in ordinary scenes, are in scope as coloring pages.
- Refuse sexualized, violent-gore, or exploitative requests. Do not "draw someone nude as a coloring page".
- Do not reproduce trademarked character model sheets. If the photo is a person in a costume, stylize **that photo**; do not swap in official character art.
- Do not copy watermarks, stock-site IDs, or UI chrome from the source.

## Multiple photos

One photo = one A4 page. Several photos = one PDF with one page per photo, same intensity, same margins. Compose each page with `compose_a4_pdf.py`, then merge if a PDF merger is available; otherwise deliver separate PDFs.

## Resources (load on demand)

- [references/style-guide.md](references/style-guide.md) — visual law
- [references/intensity.md](references/intensity.md) — simple / medium / advanced
- [references/portrait-rules.md](references/portrait-rules.md) — faces and bodies
- [references/prompt-templates.md](references/prompt-templates.md) — copy-ready prompts
- [references/analysis-method.md](references/analysis-method.md) — inventory worksheet
- [references/pdf-spec.md](references/pdf-spec.md) — A4 geometry
- [references/qc-inspector.md](references/qc-inspector.md) — 品管人員 (closed lines + extra gates)
- [references/quality-checklist.md](references/quality-checklist.md) — pass/fail summary
- [references/style-reference-index.md](references/style-reference-index.md) — which PNG to feed
