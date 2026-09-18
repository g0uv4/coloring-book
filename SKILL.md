---
name: coloring-book
description: Convert an uploaded photograph into a coloring-book page at simple, medium, or advanced intensity. After QC, show the plate and wait — compose an A4 PDF only when the user confirms. Use when they upload a photo and ask for a coloring book, coloring page, 著色本, 著色頁, 線稿, or line art for coloring. Never grayscale or edge-detect. Never PDF before confirmation.
license: MIT
compatibility: Grok, Codex, Claude, any agent with image generation plus a filesystem
metadata:
  version: "1.6.0"
  short-description: Photo to Open-Line Plate coloring page; A4 PDF only after user confirms
  author: Inkplate
---

# Coloring Book (Open-Line Plate)

Turn one user-uploaded photograph into a **printable coloring page**. Compose an **A4 PDF only after the user looks at the plate and agrees**.

This is a **translation**, not a filter. Do not desaturate, posterize, Sobel, Canny, or "find edges" on the photo. Rebuild the scene as a coloring-book illustration with one locked style called **Open-Line Plate**, at one of three intensities: **simple**, **medium** (default), **advanced**.

This pack is a **skill**, not a website. Do not scaffold or deploy a web app for it.

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

If they ask for all three, run the pipeline three times on the same photo and **preview all three plates** before asking which (or all) should become PDFs.

## Input lock

- `USER_PHOTO` = the photograph uploaded in **this** request. Record its exact local path. Never substitute a previous result or a screenshot.
- `INTENSITY` = `simple` | `medium` | `advanced`
- `PLATE` = the generated coloring page (temporary).
- `CLEAN_PLATE` = `PLATE` after `scripts/cleanup_lines.py`.
- `QC_REPORT` = JSON from `scripts/qc_plate.py`.
- `PDF` = A4 deliverable from `scripts/compose_a4_pdf.py`. Only after the user confirms.

There are **no bundled style images**. Open-Line Plate is defined in text (`references/style-guide.md`). If the user attached coloring-book examples, they are **mood only**: do not copy them, do not feed them as IMAGE 1, do not add them to this repo.

## Tool contract

1. Confirm an image-generation edit tool is callable (`imagine_image_to_image`, or an images-edits API with the user photo). If none exist, stop and say so. Do **not** fake the plate with Pillow, OpenCV, Canny, or CSS filters.
2. Use Python scripts only for cleanup, **QC**, and A4 composition — never to draw the picture.
3. Show the plate only after **QC SHIP**. **Do not compose a PDF until the user confirms** in a later message.
4. If generation, cleanup, or QC fails, name the failed stage and return no PDF.

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

Read [references/style-memory.md](references/style-memory.md). Recall this user's Grok memory for `$coloring-book`.

- Remembered **default intensity** applies if this turn does not name one.
- Remembered extra locks (no cartoon fire, no knit texture, …) always apply unless this turn contradicts them.
- This-turn words win. Skill table above is the fallback when memory is empty (`medium`).

### 2c. Remembered style overlay

If a profile exists, add its extra locks into the inventory `Do not draw` line. Do not skip QC because memory exists.

### 3. Generate the plate

Build the prompt from [references/prompt-templates.md](references/prompt-templates.md). Fill the inventory block with facts from step 2. Insert the **intensity block** for `simple`, `medium`, or `advanced`. Keep the locked style block verbatim.

**Required:** `imagine_image_to_image` on `USER_PHOTO` only (or `POST /v1/images/edits` with that single photo). Model `grok-imagine-image-2.0` or `grok-imagine-image-quality`.

- `aspect_ratio`: `2:3` for portrait/square sources, `3:2` for landscape sources
- Do **not** pass third-party coloring pages, bundled samples, or previous outputs as style images
- Do not generate from text alone when the user uploaded a photo — identity will drift

Copy the returned sandbox path to the run folder as `plate-raw.png` (keep the original too).

### 4. Cleanup

```bash
python3 scripts/cleanup_lines.py plate-raw.png plate-clean.png --threshold 128
```

### 5. QC inspector (品管人員)

Read [references/qc-inspector.md](references/qc-inspector.md) and **become that person**. Do not compose a PDF until QC signs off **and** the user confirms.

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

- **SHIP** → go to step 6 (preview). Do **not** compose a PDF yet.
- **RETRY** (first fail) → regenerate once with the matching add-on in `qc-inspector.md`
- **STOP** (second fail) → show the best plate + QC fails, no PDF

### 6. Preview — wait for the user

Show the **clean plate image**. One short note: intensity used and what was simplified. Do not show the raw pre-cleanup image unless they ask.

Then **ask and stop**. Do not run `compose_a4_pdf.py` in this turn, even if the original request mentioned PDF.

Ask in the user's language, for example:

- 這張線稿可以嗎？要輸出成 A4 PDF，還是要再改（強度、元件、臉、衣服、背景）？
- Keep this plate and make an A4 PDF, or keep editing?

On the next message:

| User says | Action |
|---|---|
| 可以 / 輸出 / PDF / 列印 / OK / yes / ship | step 6b, then 7 |
| 再改、加／減元件、換強度、臉不對… | back to step 3 with those notes, then QC, then step 6 again |
| 記住這個風格 / 以後都這樣 | step 6b only (PDF still needs an explicit yes) |
| 取消 | stop, no PDF |

Keep the last `plate-clean.png` path so PDF composition does not need a new generation.

### 6b. Persist style (`$memory-with-docs`)

When they **like** the plate or give a standing rule, read [references/style-memory.md](references/style-memory.md) and invoke **`$memory-with-docs`** (`/memory-with-docs`) with that payload.

- Replace the previous coloring-book profile; do not append duplicates.
- Do not store the photo or who is in it.
- Then continue to step 7 if they also asked for a PDF in the same message.

### 7. Compose A4 PDF

Read [references/pdf-spec.md](references/pdf-spec.md).

```bash
python3 scripts/compose_a4_pdf.py plate-clean.png plate-a4.pdf \
  --dpi 300 --margin-mm 14 --orientation auto \
  --preview plate-a4.png
```

Add `--title "..."` only when the user asked for a title. Default is a clean sheet with no header/footer chrome on the artwork.

If Python is unavailable, use any PDF tool that can place the PNG on an A4 page with ~14 mm margins. Last resort: return the PNG and tell the user to print "fit to A4, no crop".

### 8. Deliver PDF

Show the A4 PDF (downloadable) and `DELIVERY PASS`. Do not regenerate unless they ask.

## Safety and rights

- Family photos, including children in ordinary scenes, are in scope as coloring pages.
- Refuse sexualized, violent-gore, or exploitative requests. Do not "draw someone nude as a coloring page".
- Do not reproduce trademarked character model sheets. If the photo is a person in a costume, stylize **that photo**; do not swap in official character art.
- Do not copy watermarks, stock-site IDs, or UI chrome from the source.
- Do not ship, bundle, or regenerate other people's coloring pages. Mood examples stay in the chat.

## Multiple photos

One photo = one page. Several photos = one plate each, same intensity. Confirm **each** plate (or the set) before composing PDFs. Compose each agreed page with `compose_a4_pdf.py`, then merge if a PDF merger is available; otherwise deliver separate PDFs.

## Resources (load on demand)

- [references/style-guide.md](references/style-guide.md) — visual law
- [references/intensity.md](references/intensity.md) — simple / medium / advanced
- [references/portrait-rules.md](references/portrait-rules.md) — faces and bodies
- [references/prompt-templates.md](references/prompt-templates.md) — copy-ready prompts
- [references/analysis-method.md](references/analysis-method.md) — inventory worksheet
- [references/pdf-spec.md](references/pdf-spec.md) — A4 geometry
- [references/qc-inspector.md](references/qc-inspector.md) — 品管人員 (closed lines + extra gates)
- [references/quality-checklist.md](references/quality-checklist.md) — pass/fail summary
- [references/examples-index.md](references/examples-index.md) — worked examples
- [references/style-memory.md](references/style-memory.md) — persist taste via `$memory-with-docs`

