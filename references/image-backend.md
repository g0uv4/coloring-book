# Image backend router

Same Open-Line Plate prompt ([prompt-templates.md](prompt-templates.md)). Only the **host image tool** changes.

Do **not** invent HTTP endpoints. Do **not** ask the user for an API key. Use a tool this session already attached. Detect **tools first**, then product name.

## Detect once, then stay

First matching row wins. Do not hop vendors mid-job.

| Host | How you know | Call this | Ask for |
|---|---|---|---|
| **Grok / SuperGrok / Grok Build** | `imagine` / `imagine_image` / `imagine_image_to_image` | `imagine_image_to_image` on `USER_PHOTO` | Grok Imagine |
| **OpenAI harness / Codex / ChatGPT** | `image_gen`, `$imagegen`, `CODEX_HOME` | built-in `image_gen` **edit** the photo. CLI fallback only if they ask | ChatGPT Images / `gpt-image-2` (or host GPT Image default) |
| **Google Antigravity** | product is Antigravity, or tools mention Nano Banana | host generate/edit-image with the photo as reference | Nano Banana Pro, else Nano Banana 2 |
| **Gemini CLI / Gemini Code Assist** | Gemini CLI / `GEMINI.md` workspace | Gemini native image generate/edit | Nano Banana 2 / Pro if offered |
| **Kimi / Kimi Agent / Kimi Code / OK Computer** | product is Kimi, or tool `generate_image` | `generate_image` (and any crop/edit sibling) with the photo as reference if the tool accepts one | host default image tool — do not invent a Moonshot URL |
| **Claude Code** | `~/.claude` / Claude Code CLI | **whatever image skill or MCP this session already has** (`image_gen`, `$imagegen`, Nano Banana skill, `generate_image`) | that tool's default. Claude Code has **no first-party raster model** |
| **Cursor** | Cursor agent / Composer | host image-edit or attached MCP image tool | host default |
| **GitHub Copilot coding agent** | Copilot agent session | Copilot image tool if present, else any attached MCP image tool | host default |
| **OpenCode / Cline / Aider / Windsurf / Qwen Code** | that product name | that host's image-edit tool or attached MCP/skill | host default |
| **Anything else** | none of the above | the first tool whose name or docs say generate/edit image | whatever it ships |

If the chosen tool is missing, **stop and say so**. Do not silently call another vendor.

## Claude Code and other “no native image” hosts

Claude Code, and some CLI-only harnesses, do not ship a raster generator. That is fine:

1. Use an image skill or MCP **already loaded** in this session.
2. If none exists, tell the user this harness cannot draw the plate here. Do not ask them to paste an API key into chat. Do not curl a random images API.

Kimi Code CLI may only have `ReadMediaFile` (vision). Drawing still needs `generate_image` from Kimi Agent / OK Computer, or another attached image tool.

## Contract (every backend)

1. **Image-to-image** the uploaded photograph. Text-to-image only if the host cannot take a reference — then describe the photo from the inventory, do not invent extra subjects.
2. Same lock + intensity + inventory. Add: interiors stay white; no solid-black fills.
3. Save `plate-raw.png` → cleanup → QC → **show PNG in chat** → wait. No PDF this turn.
4. Aspect: tall/square → 2:3, wide → 3:2.
5. Local redraw uses the **same** backend as the first plate.

## What not to do

- Do not call OpenAI Images from a Grok session.
- Do not call Imagine from Antigravity or Kimi.
- Do not tell the user to install extra image CLIs just to run this skill.
- Do not mention `/memory-with-docs`.
