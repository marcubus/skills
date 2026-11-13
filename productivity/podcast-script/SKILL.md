---
name: Podcast Script
description: Turn a report or raw notes into a podcast script and a kokoro-tone speech request. Use when the user asks for a solo, two-host, or panel podcast script, a spoken version of a report, or a script prepared for a self-hosted Kokoro gateway.
---

# Podcast Script

A script is a performance, not a document. This skill turns a source file into spoken prose and the exact kokoro-tone request that renders it. It stops at the request. Research, rendering, mastering, and publishing belong elsewhere.

## When to use

- A report, document, or raw notes already exist and the user wants a podcast script.
- The user wants a solo narration, a two-host episode, or a panel.
- The user wants voice casting, pacing, emotion, ticks, pronunciation, or a pre-render check.
- The user wants the script prepared for the kokoro-tone gateway.

Use this for script generation only. Research, audio publishing, voice cloning, and real-person impersonation belong to other skills.

## Inputs

Read the source from disk. Accept a report, raw notes, or a document. If the user pastes text, save it next to the deliverables as `<source-stem>-source.md` and read it back.

Ask for the format, audience, and runtime. Default to solo. Ask for host profiles when the user has them. If there is no profile, build one with `PROFILE.md`.

Declare the target before writing. Default 8 to 12 minutes. Long form up to about 45 minutes when the source is rich. Count spoken words, not tags.

## Write the script

Use the default baseline and `[emotion:neutral]` to clear any override. The default deployment renders only the baseline. Every preset, including `warm` and `bright`, is disabled until the deployment is tuned. Build variety from rate, pause, sentence length, and word choice.

1. Read the source. Done when the source is on disk and its path is recorded.
2. Load or build the host profile. Done when the profile passes the gate in `PROFILE.md`.
3. Map the content beats. Done when every major beat has a function, a pace band, a preset, and a performance move.
4. Build the pacing sheet. Done when the segments sum to the target and every segment has words, effective wpm, and a pause budget.
5. Write the script. Done when the prose matches the beat map and the pacing sheet, and speaks the content, not the process.
6. Add performance tags. Done when every tag traces to a beat, every same-speaker change has a pause, and every logical section boundary has a section-break pause.
7. Handle pronunciation. Done when names, acronyms, and heteronyms have a route.
8. Build the request. Done when the request input matches the script body.
9. Verify. Done when every check in `VERIFY.md` passes.

Run the matching check in `VERIFY.md` as each step closes.

## Hosts

Solo: use the main path. Two-host: read `MULTIHOST.md`. Three or more: read `PANEL.md` and write a panel plan before drafting.

## Handoff

Write the script next to the source:

- `<source-stem>-podcast-script.md`
- `<source-stem>-request.json`
- `<source-stem>-script-notes.md`

Give the curl command from `REQUEST.md`. State the word count, runtime, voices, and unresolved guesses. Report the script and the request as the deliverables. The render is the next step, so the handoff ends before audio exists.

## Reference

- `PROFILE.md`: typed host profile and gate.
- `PERFORMANCE.md`: pacing, emotion, emphasis, and performance moves.
- `TICKS.md`: tick library, density, and banlist.
- `REQUEST.md`: kokoro-tone contract, request shapes, limits, curl.
- `SCRIPT-CRAFT.md`: structure, prose, punctuation, attribution.
- `VOICE.md`: casting, presets, rate, pause.
- `MULTIHOST.md`: two-host relationship and handoffs.
- `PANEL.md`: three or more hosts.
- `VERIFY.md`: the release gate.
- `examples/`: a host profile, a beat map, a solo script, a two-host script, and a panel script.
