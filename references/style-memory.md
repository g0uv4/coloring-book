# Style memory — two layers

Open-Line Plate is the house style. User memory stores defaults on top of it. Never store the photograph, faces, or third-party coloring pages.

## Writer

1. Prefer `$memory-with-docs` (`/memory-with-docs`) if installed.
2. Otherwise `memory-edit` / Grok user memory.
3. Do not invent a local JSON cache.

## When to read

At intensity pick (workflow 2b), recall `$coloring-book`.

| If memory has | Do |
|---|---|
| a `$coloring-book` profile | use as defaults |
| nothing | skill defaults (`medium`) |
| this-turn words that conflict | **this turn wins** |

Say `套用你記住的高階預設` when a remembered default is applied.

## Layer A — standing locks (long-lived)

Always persist unless they cancel them:

- closed continuous lines, white interiors
- no cartoon clip-art fire
- textures (knit, wood, brick) as large closed slabs
- preview plate, PDF only after confirm

Refresh locks when they give a standing rule (`以後都不要卡通火`, `織紋當大塊`).

## Layer B — default intensity (explicit only)

Change default intensity only when they say:

- `記住這個風格` / `remember this style`
- `以後都這樣` / `以後都用高階` / `以後都用中等` / `以後都用簡單`
- `不要再用X當預設`

If they said `記住` without naming intensity, use the intensity of the plate just approved.

Do **not** write default intensity when they only say `可以` / `輸出 PDF` / `PDF` / `列印` / `OK` / `yes` / `ship`, or a one-off without `以後`.

## Delete

`忘記著色本設定` / `forget coloring-book style` → delete the coloring-book profile only.

Never store who is in the photo, file paths, QC numbers, or other people's plates. Replace the previous profile.

## Payload

```text
Replace the user's coloring-book style profile. Standing Super Grok preference.

Title: coloring-book style profile
Section: Preferences
Source: $coloring-book skill, confirmed {YYYY-MM-DD}

- Uses Super Grok skill `$coloring-book` (repo github.com/g0uv4/coloring-book).
- House style: Open-Line Plate — medium-thick closed black outlines, white interiors, cartoon of the real photo, never grayscale or edge-detect.
- Default intensity when unspecified: {simple|medium|advanced}.
- Advanced means more named parts from the photo, never denser or thinner lines; omit any line that would break.
- Extra standing locks: {no cartoon flames; vest/floor as large closed shapes; preview then PDF only after confirm}.
- Language for prompts to the user: {zh-TW|en}.
- Last confirmed: {kind} photo, intensity {…}, {YYYY-MM-DD}.
```

Prefix with `/memory-with-docs` when that skill exists. Otherwise use `memory-edit`.

## After a write

`已記住著色本設定：預設 {intensity}，{one extra lock}。`
Then PDF only if they also asked for it.
