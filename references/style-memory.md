# Style memory — coordinator writes, user never invokes it

Open-Line Plate is the house style. User memory stores defaults on top of it. Never store the photograph, faces, or third-party coloring pages.

## Who writes

The **coloring-book coordinator** (this skill) writes memory. The user must **never** be told to type `/memory-with-docs`, `$memory-with-docs`, or `memory-edit`.

Internally:

1. Use `$memory-with-docs` if that skill exists.
2. Else use `memory-edit` / Grok user memory.
3. Do not invent a local JSON cache.

After a successful write, one short user-facing line with **no tool name**:

`已記住你的著色本設定。`

or, if intensity changed:

`已記住：以後預設 {simple|中等|高階}。`

## When to read

At intensity pick (workflow 2b), recall `$coloring-book` silently. One clause if a default is applied: `套用你記住的高階預設`.

## Layer A — standing locks (coordinator may write without asking)

If no coloring-book profile exists after the first QC SHIP, the coordinator writes house locks only (not a new default intensity):

- closed continuous lines, white interiors
- no cartoon clip-art fire
- textures as large closed slabs
- preview plate, PDF only after confirm

Refresh locks when they give a standing rule (`以後都不要卡通火`).

## Layer B — default intensity (explicit words only)

Change default intensity only when they say:

- `記住這個風格` / `remember this style`
- `以後都這樣` / `以後都用高階` / `以後都用中等` / `以後都用簡單`
- `不要再用X當預設`

Do **not** write default intensity on `輸出 PDF` / `可以` / `OK`.

## Delete

`忘記著色本設定` → coordinator deletes the coloring-book profile only. Do not ask them to run a slash command.

## Payload (internal — do not show this block to the user)

```text
Replace the user's coloring-book style profile.
Title: coloring-book style profile
Section: Preferences
Source: $coloring-book skill, confirmed {YYYY-MM-DD}

- Uses Super Grok skill `$coloring-book` (repo github.com/g0uv4/coloring-book).
- House style: Open-Line Plate — medium-thick closed black outlines, white interiors, cartoon of the real photo, never grayscale or edge-detect.
- Default intensity when unspecified: {simple|medium|advanced}.
- Advanced means more named parts from the photo, never denser or thinner lines.
- Extra standing locks: {no cartoon flames; textures as slabs; preview then PDF}.
- Language for prompts to the user: {zh-TW|en}.
- Last confirmed: {kind} photo, intensity {…}, {YYYY-MM-DD}.
```
