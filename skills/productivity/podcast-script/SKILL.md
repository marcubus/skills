---
name: "podcast-script"
description: "Turns a report, raw notes, or a document into a spoken podcast script and the plain text a text-to-speech model reads. Use for solo narration, a two-host episode, a panel, a pre-render check, or retargeting an existing script. Targets kokoro-tone, kokoro-fastapi, kokoro-raw, and ElevenLabs."
---

# Podcast Script

A script is a performance, not a document. Turn a source into spoken prose and the plain text that renders it on the chosen model. The skill stops at the text: research, rendering, mastering, and publishing belong elsewhere. Script generation only; voice cloning and real-person impersonation belong to other skills.

The script is model-neutral. It marks intent with five markers, and a model file compiles them into one target's text dialect. The words retarget; the performance compiles to what the text can carry.

## Models

Read `MODELS.md` for the registry and the choosing rules. Pick one model per episode:

- `MODEL-KOKORO-TONE.md`
- `MODEL-KOKORO-FASTAPI.md`
- `MODEL-KOKORO-RAW.md`
- `MODEL-ELEVENLABS.md`

`MODELS.md` describes each dialect.

## Inputs

Read the source from disk. Accept a report, raw notes, or a document. If the user pastes text, save it next to the deliverables as `<topic>-source.md` and read it back.

Use the format, audience, and runtime the user gives. Default to solo. Choose the target model with `MODELS.md`. Ask for host profiles when the user has them; otherwise build one in `PROFILE.md`.

If the user brings a finished script, skip to step 8. Do not rewrite it. For a brought-in script, run checks 7 to 21, skip checks 1 to 4, report failures by check number, and change only the compiled text. A retarget keeps the original source stem.

Declare the target before writing. `SCRIPT-CRAFT.md` sets the runtime bands. Count spoken words, not tags.

## Write the script

Record the emotion the beat needs, from the eight in `PERFORMANCE.md`. The model file says what its text carries; the compiler drops the rest and records them. Where the text carries none, build variety from sentence length and word choice, plus rate and pause where the text carries them.

1. Read the source. Done when the source is on disk, its path is recorded, and every claim you will speak traces to a line in it.
2. Load or build one profile per host in `PROFILE.md`. Done when every profile passes the gate.
3. Choose the model in `MODELS.md`. Done when the model is named and its capability table is read.
4. Map the content beats with the taxonomy in `PERFORMANCE.md`. Done when every major beat has a function, a pace band, an emotion, a rate, and a performance move.
5. Build the pacing sheet in `PERFORMANCE.md`. Done when the segments sum to the target and every segment has a function, pace band, emotion, rate, effective wpm, words, duration, pause, handoff, emphasis, and move.
6. Write the script to the prose rules in `SCRIPT-CRAFT.md`. Done when the prose matches the beat map and the pacing sheet, and speaks the content, not the process.
7. Add markers and ticks from `TICKS.md`. Done when every marker traces to a beat, every same-speaker change has a pause, and every logical section boundary has a section-break pause.
8. Handle pronunciation in `HANDOFF.md`. Done when names, acronyms, and heteronyms have a route.
9. Compile the text with `HANDOFF.md`. Done when every marker is resolved and the text matches the model's dialect.
10. Verify against `VERIFY.md`. Done when every check passes.

Run the checks for the step you just closed, using the step map in `VERIFY.md`. Apply each check with the agent's file and search tools; a listed shell command is the equivalent route when one is available. A failed check means the step is unfinished: fix it and run the check again before moving on. When you need the shape of a profile, a beat map, or a script, read `examples/`.

## Hosts

Solo: use the main path. Two-host: read `MULTIHOST.md`. Three or more: read `PANEL.md` and write a panel plan before drafting. Cast voices from `VOICE.md`.

## Handoff

Write the script next to the source:

- `<source-stem>-podcast-script.md`
- `<source-stem>-tts-<model>.txt`, the compiled text
- `<source-stem>-script-notes.md`, or `<source-stem>-script-notes-<model>.md` for a retarget
- One host profile per host, solo included.
- `<source-stem>-panel-plan.md`, for three or more hosts.

Write the notes to the contract in `HANDOFF.md`. State the model, the word count, runtime, voices, every dropped marker, and unresolved guesses. Report the script and the compiled text as the deliverables. The render is the next step, so the handoff ends before audio exists.
