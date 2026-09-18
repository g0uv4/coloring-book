# Style memory — persist what this user likes

Open-Line Plate is the locked house style. **User memory** stores *their* defaults on top of it (intensity, extra omit rules, language). Never store the photograph, faces of people in the photo, or third-party coloring pages.

Persist with **`$memory-with-docs`** (slash `/memory-with-docs`). That skill writes documented facts into **this user's** Grok memory. Do not invent a local JSON cache and do not edit the skill pack to “save” a taste.

## When to read

At intensity pick (workflow 2b), recall Grok memory for `$coloring-book`.

| If memory has… | Do |
|---|---|
| a `$coloring-book` profile | use it as **defaults** |
| nothing | skill defaults (`medium`, Open-Line Plate law) |
| this-turn words that conflict | **this turn wins** |

Tell the user in one clause when a remembered default is applied, e.g. `套用你記住的高階預設`.

## When to write

Only after a **durable** signal — not after the first generate.

Write when **any** of these happen:

- they confirm the plate (`可以` / `輸出 PDF` / `喜歡這張` / `記住這個風格`)
- they give a standing rule (`以後都用高階`, `臉再簡一點當預設`)
- they correct a remembered default (`不要再用高階當預設`)

Do **not** write:

- a one-off (`這張給小孩，簡單就好`) unless they say 以後
- who is in the photo
- file paths, overlay JSON, QC numbers
- other people's coloring pages

Replace the previous `$coloring-book` profile. Do not stack five versions.

## Payload for `/memory-with-docs`

Invoke `$memory-with-docs` with this exact shape. Fill `{…}` from the confirmed run. Keep it one profile, not a diary.

```text
/memory-with-docs

Replace the user's coloring-book style profile. This is a standing Super Grok preference, not a one-off.

Title: coloring-book style profile
Section: Preferences
Source: $coloring-book skill, confirmed {YYYY-MM-DD}

Write (replace any older coloring-book / Open-Line Plate preference):

- Uses Super Grok skill `$coloring-book` (repo github.com/g0uv4/coloring-book).
- House style: Open-Line Plate — medium-thick closed black outlines, pure white interiors, cartoon of the real photo, never grayscale or edge-detect.
- Default intensity when unspecified: {simple|medium|advanced}.
- Advanced means more named parts from the photo, never denser or thinner lines; omit any line that would break.
- Extra standing locks: {e.g. no cartoon flames; vest/floor as large closed shapes not texture; preview plate then PDF only after confirm}.
- Language for prompts to the user: {zh-TW|en}.
- Last confirmed: {kind} photo, intensity {…}, {YYYY-MM-DD}.
```

If they only confirmed a plate and did not state a new default intensity, set **Default intensity** to the intensity of that confirmed plate.

If they said `忘記著色本設定` / `forget coloring-book style`, call `$memory-with-docs` to **delete** the coloring-book profile only.

## What “style” is allowed to mean

Remember these knobs, nothing else:

| Knob | Example |
|---|---|
| default intensity | advanced |
| extra omit rules | no knit texture, no wood grain, no clip-art fire |
| face tightness | even simpler than the portrait recipe |
| confirm-before-PDF | always wait |
| UI language | 繁體中文 |

Do not remember a favorite *subject* (always kitchens, always selfies) unless they explicitly say so.

## After a successful write

One short line to the user, then continue (PDF if they also asked for it):

`已用 /memory-with-docs 記住：預設 {intensity}，{one extra lock}。`
