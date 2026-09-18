# Image backends by host

Same Open-Line Plate prompt. Different **edit** tool. Always send `USER_PHOTO` as the source image. Never text-only when a photo exists. Never Pillow / Canny / CSS filters.

Pick the first row that matches **callable tools in this session**. Env names are hints only.

| Host | Detect | Call | Model hint |
|---|---|---|---|
| **Grok** | `imagine_image_to_image` exists, or runtime looks like Grok / SuperGrok | `imagine_image_to_image` on `USER_PHOTO` | `grok-imagine-image-2.0` or `grok-imagine-image-quality` |
| **OpenAI harness / Codex / ChatGPT** | built-in `image_gen` / `$imagegen` exists, or `OPENAI_API_KEY` + Images API | built-in **image_gen** (preferred). Else `POST /v1/images/edits` with the photo | ChatGPT Images: `gpt-image-2` (fallback `gpt-image-1.5`) |
| **Google Antigravity** | Antigravity / Gemini image tool exists (`generate_image`, Nano Banana MCP, Gemini image) | that native **image edit** tool with `USER_PHOTO` + the plate prompt | **Nano Banana Pro** `gemini-3-pro-image`. If Pro is not on this account, **Nano Banana** / Nano Banana 2 (`gemini-3.1-flash-image` or `gemini-2.5-flash-image`) |

If none of those tools exist, **stop**. Name the missing backend. Do not invent an HTTP endpoint and do not draw the plate in Python.

## Rules that do not change

- Prompt body stays [prompt-templates.md](prompt-templates.md).
- Aspect: source tall/square → `2:3` or `1024x1536`; wide → `3:2` or `1536x1024`.
- One photo in. One plate out. No third-party coloring pages as style refs.
- After the file lands, the rest of the skill is the same: cleanup → QC → preview → vector PDF.

## What you may tell the user

One short line is enough, e.g. `這次用 Grok Imagine 畫線稿` / `ChatGPT Images` / `Nano Banana Pro`. Do not dump API names unless they ask.
