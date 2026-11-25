# Podcast Host Personas

## What
Builds one machine-readable host persona per show. A persona is a profile that defines how a fictional host sounds, speaks, and behaves across six emotional states. The transcript skill reads the profile to cast voices and render audio.

## Why Use It
When you need consistent, distinct host voices for podcast scripts. Ensures hosts sound different from each other and match your show's tone without voice cloning or real-person impersonation. Generated personas can be reused by `podcast-script` for script generation with consistent character voices.

## How (Brief)

Invoke as a skill: `/podcast-host-personas`. Tell it the host you need. Example:

```
/podcast-host-personas mid-range EIQ female host with British accent for tech podcast
```

The generated persona can be used by `podcast-script` to cast voices and generate scripts.

## Profile Structure

Twenty-eight fields in fixed order across seven sections:

- **Identity** (7): id, version, display_name, nationality, sex, describing_words, field_of_expertise
- **Sound** (3): vocal_fingerprint, tick_inventory, tick_density
- **Body and room** (3): recording_context, breath_profile, non_speech_sound
- **Word choice** (4): lexical_register, exemplar_lines, calibration_line, pronunciation_lexicon
- **Emotion** (4): eiq, eiq_justification, emotion_behaviour, recovery_behaviour
- **Show** (4): standing_dynamic, handoff_protocol, mode_behaviour, cue_scopes
- **Close** (3): voice_note, provenance, canon_status

## Store Layout

Two directories:

- `examples/` — guidance only: blank template and three worked examples
- `personas/` — the store: generated profiles only, gitignored

Each profile saves to `personas/<id>.md` with one index line in `personas/index.jsonl`. The distinctness gate reads this index.

## Workflow Summary

1. Resolve the brief into twenty-eight fields using reference files
2. Build the fingerprint across seven distinctness axes plus timbre and laugh shape
3. Write six emotional states and recovery behaviour from emotion-engine.md
4. Set word choice, body, room, and show behaviour from craft references
5. Run the distinctness gate against all stored personas
6. Pass GATE.md checks 1 to 29

## Reference Files

| File | Purpose |
|---|---|
| `GATE.md` | Twenty-nine checks, step map, nineteen failure modes |
| `references/persona-schema.md` | All twenty-eight fields with types, defaults, rules V1-V33 |
| `references/describing-words.md` | Forty-word vocabulary and contradiction matrix |
| `references/tick-library.md` | Seventy-two ticks, eight types, density and selection rules |
| `references/emotion-engine.md` | EIQ bands, six invariants, six states, co-host rules |
| `references/voice-craft.md` | Lexical register, exemplars, calibration line, lexicon |
| `references/studio-craft.md` | Room, breath, object sound |
| `references/show-craft.md` | Modes, handoff, standing dynamic |
| `references/phonetic-distinctness.md` | The distinctness gate: seven axes and match limits |

## Hard Rules

- Invent the person; do not copy real people.
- Three describing words maximum from closed vocabulary, no contradiction pairs.
- EIQ is one float and one sentence naming observable behaviour.
- Distinctness is decided by reading two profiles side by side, never listening.
- Every surviving axis match goes into accepted_matches with a reason.

## Handoff Contract

A transcript skill reading this persona can rely on: stable field names; tick ids mapping to literal strings in tick-library.md; six states present; recovery_behaviour giving the way out of each state; cue_scopes giving precedence line over segment over episode; mode_behaviour giving deviation for each segment type.

## Attribution

Original concept by Marcubus. This implementation provides a machine-readable persona system for podcast script generation and voice casting.
