# Image backend router

The plate is always the same Open-Line Plate prompt ([prompt-templates.md](prompt-templates.md)). Only the **host image tool** changes. Do not call another vendor's API from this skill — use whatever image tool this harness already attached.

## Detect once, then stay

Pick the first row that matches. Do not hop mid-job.

| Host | How you know | Generate / edit tool | Model to ask for |
|---|---|---|---|
| **Grok** | tools named `imagine_image` or `imagine_image_to_image` exist | `imagine_image_to_image` on `USER_PHOTO` | Grok Imagine |
| **OpenAI harness / Codex / ChatGPT** | tool named `image_gen`, skill `$imagegen`, or env looks like Codex | built-in `image_gen` (edit the user photo). Fallback CLI `scripts/image_gen.py` only if they explicitly ask | ChatGPT Images / `gpt-image-2` (or the host default GPT Image) |
| **Google Antigravity** | product is Antigravity, or the agent is told to use Nano Banana | the host's generate/edit-image action with the user photo as reference | **Nano Banana Pro** (`gemini-3-pro-image`) if offered, else **Nano Banana 2** / Nano Banana |
| Anything else | none of the above | that host's native image-edit tool | whatever it ships |

Never invent a REST endpoint. If the matched tool is missing, say so and stop — do not silently switch vendors.

## Contract (every backend)

1. **Image-to-image** the uploaded photograph. Text-to-image only if the host cannot take a reference.
2. Same lock + intensity + inventory prompt. No style-reference coloring pages.
3. One plate per photo. Save as `plate-raw.png` then cleanup → QC → preview.
4. Aspect: tall/square → 2:3, wide → 3:2.
5. Local redraw: previous **clean plate** + original photo, not a third-party page.

## What not to do

- Do not call OpenAI Images from a Grok session (no key, wrong billing).
- Do not call Imagine from Antigravity.
- Do not tell the user to install extra image CLIs.
- Do not mention `/memory-with-docs`.
