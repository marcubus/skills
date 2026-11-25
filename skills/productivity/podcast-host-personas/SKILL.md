---
name: "podcast-host-personas"
description: "Use when a podcast needs a host persona: a first host, a second host that must not sound like the first, or a revision that adds a strained state, a mode set or a room. Saves one machine-readable profile per host and gates it against the store."
---

# Podcast host personas

A persona is a machine-readable description of a fictional host, written for two consumers: a script writer who needs to know how this person talks, and a speech synthesiser that needs to know how this person sounds. Every field constrains either words on the page or delivery.

This skill ends at a saved profile. A transcript skill reads it, casts a voice, and renders audio.

## Contents

- When to use
- When not to use
- The profile in one view
- Store layout
- Overrides
- Workflow
- Hard rules
- The distinctness gate
- Non-goals
- Files
- Handoff contract

## When to use

- A new show needs a host who sounds like a specific person rather than a narrator.
- A second host joins a show and the two must be separable on the page, not only in voice.
- An existing persona needs a strained state, a recovery, a mode set, or a room.
- An EIQ rating needs setting, or a co-host exchange needs the persona's response defined.

## When not to use

- Real people. Personas are invented.
- Voice casting, voice cloning, vendor voice IDs, audio rendering. The transcript skill owns those.
- Languages other than English. The seven axes are English-specific.
- Panels of three or more, and shows that consist only of ad reads. Out of scope for v1.

## The profile in one view

Twenty-eight fields in fixed order: identity, sound, body, word choice, emotion, show, close.

Identity (7): `id`, `version`, `display_name`, `nationality`, `sex`, `describing_words`, `field_of_expertise`.

Sound (3): `vocal_fingerprint`, `tick_inventory`, `tick_density`.

Body and room (3): `recording_context`, `breath_profile`, `non_speech_sound`.

Word choice (4): `lexical_register`, `exemplar_lines`, `calibration_line`, `pronunciation_lexicon`.

Emotion (4): `eiq`, `eiq_justification`, `emotion_behaviour`, `recovery_behaviour`.

Show (4): `standing_dynamic`, `handoff_protocol`, `mode_behaviour`, `cue_scopes`.

Close (3): `voice_note`, `provenance` (which carries `accepted_matches`), `canon_status`.

Eleven fields resolve from a default when the brief is silent: `nationality`, `sex`, `tick_density`, `cue_scopes`, `version`, `recording_context`, `breath_profile`, `non_speech_sound`, `mode_behaviour`, `handoff_protocol` and `canon_status`. The defaults table in `references/persona-schema.md` owns their values. Each default applied is named in `provenance.assumptions_applied`.

Types, enumerations and rules V1 to V33: `references/persona-schema.md`.

## Store layout

Two directories, never mixed. `examples/` holds guidance: the blank template and three worked examples, each with a banner saying so. `personas/` is the store: only profiles the operator generated, each with one line in `personas/index.jsonl`.

The store is local and gitignored. `personas/` ships with a README and nothing else. A generated profile never enters the repository and never blocks an update to the skill. The folder and its index are created on the first build.

Examples carry no index line and the distinctness gate never reads them. A persona built from an example takes a new id, is saved to `personas/`, and is compared against its source example at gate step 1, because a copy of a shipped example with a new name is a duplicate the index cannot see.

A brief that names another store replaces `personas/` for that build: the profile and its index line are written there, and the distinctness gate reads that index instead. A store outside the skill folder is the way to keep personas across a reinstall.

## Overrides

The brief is the operator's. Anything it states wins over a table, a default, or a derived value: the name, the field, the describing words, the room, the EIQ, a fingerprint value, a mode. The skill's job is to make the result consistent and to record what it changed. It does not overrule the person who asked.

- A field the brief states is used as stated. A field it leaves silent takes the default.
- A value that departs from a generator table is recorded in `provenance.assumptions_applied` in the `override:` shape from V35, which names the value, the table value it replaced and the reason. A default applied and a value the brief states have their own shapes there too.
- A trait outside the closed vocabulary is kept in `provenance.brief` as the operator wrote it, and mapped to the nearest vocabulary word for `describing_words`. Both are recorded. The vocabulary stays closed for the field, because that is what makes the contradiction and cluster checks possible.
- A name the operator chose is kept, including a name that coincides with a public or fictional figure, provided the field, the traits and the voice are invented and `provenance` records the choice.
- Two things still stop the build: a brief that asks for a real living person's identity, voice or words. And an override that makes the profile contradict itself, such as a contradiction pair, a banned tick, or a ceiling in decibels. Report the conflict and the two ways out. Do not silently pick one.

## Workflow

1. **Resolve the brief** into the twenty-eight fields using `references/persona-schema.md`. Done when every field holds a value or is named as a default in `provenance.assumptions_applied`.
2. **Resolve describing words** against `references/describing-words.md`. Done when one to three words survive, each in the vocabulary, with no contradiction pair between any two.
3. **Build the fingerprint** across the seven distinctness axes plus timbre, laugh shape and placement, and the signature interjection, drawing ticks from `references/tick-library.md`. Done when all ten axes hold an enumerated value, the interjection's phoneme class matches its library entry, and the tick set passes the selection rules in `references/tick-library.md`.
4. **Write the six states and the recovery** from `references/emotion-engine.md`. Done when each of the six carries all five sub-fields, the tick list is empty only for `intense` where `on_cue` says so, each ceiling is written in words, and all five recovery sub-fields are filled with a latency that suits the band.
5. **Write the word choice** from `references/voice-craft.md`: `lexical_register`, four exemplar lines plus three negatives, the calibration line, the pronunciation lexicon. Done when every rule in `references/voice-craft.md` holds and the calibration line passes K5 at the declared pace.
6. **Set the body and the room** from `references/studio-craft.md`. Done when the room passes R1 to R7, the breath claims agree with the BRE ids in the inventory, and the object lists pass N1 to N5.
7. **Write the show behaviour** from `references/show-craft.md`. Done when `standing_dynamic`, `handoff_protocol` and `mode_behaviour` pass S1 to S8, H1 to H6 and M1 to M7, and no bridge phrase appears in another host on the show. When the co-host is already stored, read its profile first: it fixes the shared room and objects, the bridges, and which host opens and closes (S8, H3, L5, R5, N4).
8. **Run the distinctness gate** in `references/phonetic-distinctness.md` against every line in `personas/index.jsonl` whose status is not `retired`, and against the example the brief derives from if there is one. Done when every match is inside the limits or is written into `accepted_matches` with a reason, and the side-by-side reading test is recorded.
9. **Run the gate** in `GATE.md`, write the voice note, save to `personas/<id>.md`, append one index line. Done when C1 to C28 pass, the file exists, the index holds exactly one line for that id, and nothing was written to `examples/`.

Numbered generator steps with two worked examples: `references/generator-procedure.md`. Those twenty-four steps expand the nine above in order. The step map in `GATE.md` gives the correspondence.

## Hard rules

1. Invent the person, or take the person the operator specified. Every persona has a name and a field, and its voice and traits are invented rather than copied from a real person. The id is the display name lowercased with underscores between words, and matches the filename stem.
2. Every claim about a real broadcaster carries a source URL in `references/vocal-research.md`. Every estimate carries the word estimate and its derivation.
3. Three describing words maximum, drawn from the closed vocabulary, with no contradiction pair.
4. EIQ is one float and one sentence naming observable behaviour.
5. EIQ holds six invariants, listed in `references/emotion-engine.md`. Two profiles differing only in EIQ read as the same person.
6. Tick density follows `references/tick-library.md`. Its ceiling is absolute.
7. Distinctness is decided by reading two profiles side by side, never by listening.
8. Every surviving axis match is written into `accepted_matches` with a reason. A lexical difference is context there, never a substitute for an axis difference.
9. Delivery guidance names a capability class, not a product. See `references/tts-capability-guide.md`.
10. Ceilings are behavioural: volume moves at most one step above baseline, profanity and personal abuse stay off the table. Abuse is the one event that resets a persona: an apology or a walk-out, once, and the state resolves.
11. Every profile rebuilds from its own file, with no reference to the conversation that produced it.
12. Every check is run by reading. A script that automates one lives outside the skill folder, because the skill reads its own folder.
13. Baseline artifacts stay baseline: exemplars, calibration line, register, room and modes carry no strained state, so a reader can tell the resting voice from the working one.
14. A profile is edited by version bump, never in place under the same version. A replacement takes a new id and sets `supersedes`.
15. Guidance stays in `examples/`, generated profiles in `personas/`. Nothing in `examples/` is indexed, and every generated profile is.

## The distinctness gate

The seven-axis comparison in `references/phonetic-distinctness.md`, which owns its rules. It is the last step that can refuse a brief.

## Non-goals

- Transcript generation, markup authoring, audio rendering.
- Voice selection and vendor parameter tuning.
- Real-person impersonation.
- Accent authenticity claims. An accent field sets vowel colour and stress.

## Files

| Path | Contents | Read when |
|---|---|---|
| `GATE.md` | twenty-nine checks, step map, nineteen failure modes, sanity read | every build |
| `references/persona-schema.md` | twenty-eight fields, types, defaults, rules V1 to V33, lifecycle, index line | every build |
| `references/describing-words.md` | 40-word vocabulary, contradiction matrix, redundancy clusters | every build |
| `references/tick-library.md` | 72 ticks, eight types, density and selection rules | every build |
| `references/emotion-engine.md` | EIQ bands, six invariants, six states, co-host rules, abuse reset, recovery | every build |
| `references/voice-craft.md` | lexical register, exemplars, calibration line, lexicon | every build |
| `references/studio-craft.md` | room, breath, object sound | every build |
| `references/show-craft.md` | modes, handoff, standing dynamic | every build |
| `references/phonetic-distinctness.md` | the distinctness gate: seven axes, match limits, collision order | every build |
| `references/generator-procedure.md` | twenty-four steps, four decision tables, two worked examples | every build |
| `references/vocal-levers.md` | Table 1 property to lever, Table 2 the six states | building a fingerprint or a state |
| `references/tts-capability-guide.md` | capability classes A to E, acronym respelling, pause mapping | auditing a delivery instruction, or briefing the transcript skill |
| `references/vocal-research.md` | ten podcasters, sources, strained-state readings | auditing a source or adding a host |
| `references/verification-2026-10-21.md` | Phase 4 test output, baseline fields | audit only |
| `references/verification-craft-additions.md` | test output for the twelve craft fields | audit only |
| `references/verification-revalidation.md` | template revalidation, version 3 profiles, store split | audit only |
| `examples/_template.md` | blank profile, guidance only | every build |
| `examples/des_larkin.md`, `examples/harriet_voss.md`, `examples/noor_haddad.md` | worked examples at low, mid and high EIQ, guidance only | building a first persona, or reading a completed one |
| `personas/index.jsonl` | one line per stored persona, read by the distinctness gate | every build |
| `personas/README.md` | the local store, gitignored, created on first build | reading the store rules |

## Handoff contract

A transcript skill reading a persona can rely on stable field names. Tick ids map to literal strings in `references/tick-library.md`. This shares its id namespace with the transcript skill's tick table. Six states are present. `recovery_behaviour` gives the way out of each one. `cue_scopes` gives precedence line over segment over episode. `mode_behaviour` gives the deviation for each segment type. `exemplar_lines` and `calibration_line` give the rhythm to write against. `recording_context`, `breath_profile`, and `non_speech_sound` give the body. `standing_dynamic` gives what the two hosts owe each other.

It supplies everything about sound in a specific engine: voice choice, prosody tags, pauses, non-verbal rendering. Those decisions are made against the capability classes. They are stored outside the persona.
