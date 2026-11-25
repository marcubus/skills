# Podcast Script

## What
Turns a report or raw notes into spoken prose and the plain text that renders on your chosen TTS model. Targets kokoro-tone, kokoro-fastapi, kokoro-raw, and ElevenLabs. The skill reads existing content and generates performance-ready scripts with markers for voice delivery.

## Why Use It
When you have written content (reports, meeting notes, research) that needs to become a spoken podcast script. Converts static text into performance-ready format with pacing, emotion, and handoff markers for TTS compilation. Works with host personas from `podcast-host-personas` for consistent voice casting.

## How (Brief)

Invoke as a skill: `/podcast-script`. Tell it the report or notes you want turned into spoken script. Example:

```
/podcast-script read this report and generate a two-host tech podcast script MODEL-KOKORO-TONE
```

You can optionally reference an existing persona from `podcast-host-personas` for consistent voice casting across episodes.

## Output Files

| File | Purpose |
|---|---|
| `<source-stem>-podcast-script.md` | The spoken prose script |
| `<source-stem>-tts-<model>.txt` | Compiled text for the target TTS |
| `<source-stem>-script-notes.md` | Notes on markers, drops, and guesses |
| One host profile per host | Solo included |
| `<source-stem>-panel-plan.md` | For three or more hosts |

## Models

Choose one model per episode:

- `MODEL-KOKORO-TONE.md` — Kokoro tone dialect with performance markers
- `MODEL-KOKORO-FASTAPI.md` — FastAPI-compatible kokoro format
- `MODEL-KOKORO-RAW.md` — Raw kokoro text without markers
- `MODEL-ELEVENLABS.md` — ElevenLabs compatible format

See `MODELS.md` for the registry and choosing rules.

## Workflow Summary

1. Read the source from disk, save as `<topic>-source.md` if pasted
2. Load or build one profile per host in `PROFILE.md`
3. Choose the model in `MODELS.md`
4. Map content beats with taxonomy in `PERFORMANCE.md`
5. Build pacing sheet with segments summing to target runtime
6. Write script to prose rules in `SCRIPT-CRAFT.md`
7. Add markers and ticks from `TICKS.md`
8. Handle pronunciation in `HANDOFF.md`
9. Compile text for the model dialect
10. Verify against `VERIFY.md`

## Hosts

- **Solo** — use main path
- **Two-host** — read `MULTIHOST.md`
- **Three or more** — read `PANEL.md`, write panel plan before drafting

Cast voices from `VOICE.md`.

## Files

| File | Purpose |
|---|---|
| `SKILL.md` | Full workflow and handoff contract |
| `MODELS.md` | Model registry and choosing rules |
| `PROFILE.md` | Host profile structure and gate |
| `PERFORMANCE.md` | Beat taxonomy, pacing sheet, emotion bands |
| `SCRIPT-CRAFT.md` | Prose rules for spoken text |
| `TICKS.md` | Performance markers and ticks |
| `HANDOFF.md` | Pronunciation handling and compilation |
| `VERIFY.md` | Verification checks |
| `MULTIHOST.md` | Two-host episode guidance |
| `PANEL.md` | Panel discussion guidance |

## Handoff

Write the script next to the source: `<source-stem>-podcast-script.md` and `<source-stem>-tts-<model>.txt`. State the model, word count, runtime, voices, every dropped marker, and unresolved guesses. The render is the next step; this handoff ends before audio exists.

## Attribution

Original concept by Marcubus. This implementation provides a model-neutral script generation system with five performance markers for TTS compilation.
