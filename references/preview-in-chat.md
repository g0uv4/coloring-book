# Preview in chat

The plate must appear **as an image in the conversation**. A file path, a PDF, or a keep/omit list is not a preview.

## Required this turn (after generate + QC)

1. Call the **host image tool** so the UI actually renders a picture (Antigravity = Nano Banana; Grok = Imagine; Codex = image_gen).
2. Save `plate-raw.png` → cleanup → `plate-clean.png`.
3. **Attach / insert `plate-clean.png` again** in the reply so the cleaned line art is visible even if the raw model image was filled or cropped.
4. List 圖片元素.
5. Ask `要輸出成 A4 PDF 嗎？還是繼續修改？`
6. Stop. No PDF.

## Antigravity

- You must invoke Nano Banana (or the session Gemini image tool) on the uploaded photo. Text-only replies are a bug.
- After cleanup, attach `plate-clean.png` as an image, not a markdown path the UI will not render.
- Do not tell the user to open a folder or a PDF to see the plate.

## What not to do

- Do not stop at the inventory card when the photo is a pet / portrait / single object.
- Do not run `vectorize_plate.py` / `compose_a4_pdf.py` / `pipeline.py --pdf` on this turn.
- Do not hide a filled poster inside a PDF.
