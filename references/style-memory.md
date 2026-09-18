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

or, if a default or habit changed:

`已記住：以後預設高階。`
`已記住：以後少畫雲朵。`

## When to read

At intensity pick (workflow 2b), recall `$coloring-book` silently. One clause if a default is applied: `套用你記住的高階預設`.

## Layer A — standing locks (coordinator may write without asking)

If no coloring-book profile exists after the first QC SHIP, the coordinator writes house locks only (not a new default intensity):

- closed continuous lines, white interiors, **smooth ink (no stair-step aliasing)**
- no cartoon clip-art fire
- textures as large closed slabs
- preview plate, PDF only after confirm

Refresh locks when they give a standing rule (`以後都不要卡通火`) or a print-quality complaint (`銳齒`, `線條斷掉`).

## Layer B — default intensity

Write default intensity when they say:

- `記住這個風格` / `remember this style`
- `以後都這樣` / `以後都用高階` / `以後都用中等` / `以後都用簡單`
- `不要再用X當預設`

Also write default intensity when Layer C fires on intensity (they keep asking for the same level).

Do **not** write default intensity on `輸出 PDF` / `可以` / `OK` alone.

## Layer C — learned habits (repeated taste)

The skill watches how they **edit** plates. If the same kind of request appears **twice in this conversation** (or is already in memory and they do it again), the coordinator persists it as a standing habit.

Examples of a habit class:

| They keep saying | Persist |
|---|---|
| `高階` / `更多元件` (2+ times, not cancelled by `簡單`) | default intensity = advanced |
| `簡單` / `小孩` 2+ | default intensity = simple |
| `拿掉雲朵` / `雲少一點` 2+ | extra lock: omit extra clouds |
| `臉再簡` / `不要追臉` 2+ | extra lock: simpler faces |
| `銳齒` / `線不要階梯` / `斷線` | extra lock: print-smooth path; rerun cleanup+compose |
| `不要卡通火` | extra lock: no clip-art fire |

One-off edits (`這張拿掉雲朵`) stay one-off until the second same-class request.

Never store who is in the photo. Never ask them to type a memory command.

## Delete

`忘記著色本設定` → coordinator deletes the coloring-book profile only.

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
- Extra standing locks: {no cartoon flames; textures as slabs; preview then PDF; smooth ink no jaggies; …learned habits…}.
- Learned habits: {omit extra clouds | simpler faces | …}.
- Language for prompts to the user: {zh-TW|en}.
- Last confirmed: {kind} photo, intensity {…}, {YYYY-MM-DD}.
```
