# Gate

The skill checking its own output. Twenty-nine checks, a step map from the workflow to the checks that close it, the failure modes, and the sanity read.

Run every check before saving. Each check names the file that owns its rule, so a failure is fixed in the rule file, not in the profile. Record failures and fix them; do not save with an open failure.

## Contents

- How to run
- Step map
- Checks C1 to C29
- Commands
- Failure modes
- The five-question sanity read

## How to run

C1 to C24 and C26 to C28 run against the candidate profile before it is saved. C25 runs after the save and the index append, because it tests the path. C29 runs when a reference file changes, because it audits the skill rather than the profile.

A check that needs judgement says so and says what to compare. A check that can be a command gives the command, run from the skill folder with the profile path substituted.

## Step map

The nine workflow steps in `SKILL.md` are the steps. The twenty-four steps in `references/generator-procedure.md` expand them in order, and the column here gives the correspondence.

| Step | Generator steps | Checks |
|---|---|---|
| 1. Resolve the brief | 1 to 4 | C1, C2, C10 |
| 2. Resolve describing words | 4 | C3 |
| 3. Build the fingerprint | 5 to 10 | C4, C5, C6, C27 |
| 4. Write the states and the recovery | 11 to 12 | C7, C8, C17 |
| 5. Write the word choice | 13 to 15 | C11, C13, C14, C15, C16 |
| 6. Set the body and the room | 16 to 17 | C21, C22, C23 |
| 7. Write the show behaviour | 18 to 20 | C18, C19, C20 |
| 8. Run the distinctness gate | 22 | C9 |
| 9. Run the gate, save, index | 21, 23 to 24 | C12, C24, C25, C26, C28 |
| Reference maintenance | none | C29 |

## Checks C1 to C29

C1 to C12 test structure and sound. C13 to C27 test word choice, body, show, store and sources.

| # | Check | Rule file | Conditions | Done when |
|---|---|---|---|---|
| C1 | Required fields present | `references/persona-schema.md` | all twenty-eight fields present, correct types, no empty strings, and every counted field inside its stated range (V4) | the profile reads field for field against the schema shape block |
| C2 | Defaults and deviations logged | `references/persona-schema.md` | every line in `assumptions_applied` matches one of the four shapes in V35, `pace_wpm_estimate` sits inside its band window (V6), and every `override` line names the table value it replaced | each line starts with `default:`, `stated:`, `override:` or `history:`, and every override names a table value |
| C3 | Describing words | `references/describing-words.md` | 1 to 3 words, all in vocabulary, no contradiction pair, no cluster duplicate | every pair in the resolved list is absent from the contradiction table and from one cluster |
| C4 | Tick count and overlap | `references/tick-library.md` | 6 to 8 ids, at most 2 per type, at most 3 shared with any one stored persona | the per-type tally and the shared-id tally against `personas/index.jsonl` both pass |
| C5 | Tick density | `references/tick-library.md` | count ticks across the four exemplar lines and the calibration line, then scale to 100 words; the rate sits between baseline and strained, never above the cap, and no sentence under 6 words carries one, except the laugh line and the calibration line's opener, where E3 and K3 put the tick there by design; a bracketed laugh counts whether or not it is in the inventory | the scaled rate is inside the declared band |
| C6 | EIQ | `references/emotion-engine.md` | float in 0.0 to 1.0, one sentence of 40 words or fewer, no personality prose, no diagnosis, and no state vocabulary in the four baseline artifacts | the float, the sentence and the baseline read all pass |
| C7 | Six states complete | `references/emotion-engine.md` | six states, five sub-fields each; only `intense` may hold an empty `ticks_under_load`, and then `on_cue` says so; every `ticks_under_load` entry is in `tick_inventory` (V13); a single-host show sets `cohost_divergence` to `not_applicable` | the sub-field tally is 30 of 30 |
| C8 | Ceilings in words | `references/emotion-engine.md` | no digits, percent signs, dB, the word decibel, or angle brackets; the angry ceiling states profanity zero and personal abuse zero | command 8 returns nothing |
| C9 | Distinctness | `references/phonetic-distinctness.md` | core matches at most 1, total matches at most 3, every match documented, and the side-by-side reading test recorded | the gate passes and `accepted_matches` carries one line per surviving match |
| C10 | No impersonation | `references/persona-schema.md` | no living person is impersonated: no real broadcaster's identity, no quotation of a real person, no character reproduced. A name the operator chose that coincides with a figure is allowed when the field, traits and voice are invented and `assumptions_applied` records the choice (V34) | the profile names nobody real and copies nobody |
| C11 | Acronyms | `references/voice-craft.md` | every acronym has a spoken form, none written as separated letters | command 11 returns nothing |
| C12 | Reproducible | `references/persona-schema.md` | a reader with no context can rebuild the voice from the file alone | the reader answers the five sanity questions from the file |
| C13 | Lexical register | `references/voice-craft.md` | all eight sub-fields filled, assertion and hedges agree, banned words clear of vocabulary and ticks, openers unique on the show | L1 to L6 hold |
| C14 | Exemplars | `references/voice-craft.md` | four lines of 8 to 30 words at baseline, one tick maximum each, laugh written as a sound, three `never_says` lines, disagreement matches `assertion` | E1 to E7 hold |
| C15 | Calibration line | `references/voice-craft.md` | 18 to 26 words, signature interjection once, opener once, no state vocabulary, 6 to 13 seconds at the declared pace | K1 to K6 hold |
| C16 | Pronunciation lexicon | `references/voice-craft.md` | 0 to 12 pairs, spoken forms in plain syllables, no dotted letters, written form appears elsewhere in the profile, no entry the stack already reads correctly | P1 to P5 hold |
| C17 | Recovery | `references/emotion-engine.md` | all five sub-fields filled, latency suits the band, first line carries no state word, tell is physical, `does_not` names one behaviour | Q1 to Q5 hold |
| C18 | Modes | `references/show-craft.md` | the four required modes present, every entry present has all four values, deltas inside range, correction and sponsor read carry no ticks, outro names where the sign-off lands | M1 to M7 hold |
| C19 | Handoff | `references/show-craft.md` | overlap count agrees with `takes_floor`, 2 to 4 bridges each for a two-host show and `["not_applicable"]` for a single host (H6), no bridge shared with another host on the show, `yields_when` is observable | H1 to H6 hold |
| C20 | Standing dynamic | `references/show-craft.md` | `show_shape` governs the not-applicable fields, owns and defers do not overlap, relation states a basis, one host opens and one closes | S1 to S8 hold |
| C21 | Room | `references/studio-craft.md` | enums only, no numbers, distance and room tone agree, hosts on one show share room and distance | R1 to R7 hold |
| C22 | Breath | `references/studio-craft.md` | audible claim matches a BRE id, no BRE id with an inaudible inhale, sigh habit matches the inventory, laugh breath matches laugh shape | B1 to B6 hold |
| C23 | Object sound | `references/studio-craft.md` | disjoint lists, 0 to 4 each, `none` only alone, keyboard or buzz only in a room that has one, hosts on one show agree | N1 to N5 hold |
| C24 | Lifecycle | `references/persona-schema.md` | status is draft, approved or retired; `supersedes` is null or a retired id; `version` incremented if any field changed | V32 and V20 hold |
| C25 | Storage split | `references/persona-schema.md` | the profile sits in `personas/` as `<id>.md` with exactly one index line, nothing was written to `examples/`, a derived example is named in `accepted_matches` | V1 and V33 hold |
| C26 | No vendor in the profile | `references/tts-capability-guide.md` | no vendor name, product name, model name, voice identifier or prosody tag in any field; delivery guidance names a capability class | command 26 returns nothing |
| C27 | Signature interjection | `references/tick-library.md` | `signature_interjection.tick_id` appears in `tick_inventory`, and its `phoneme_class` matches that id's row in the library (V8) | the id and the class both read from the library |
| C28 | Voice note | `references/persona-schema.md` | one paragraph of 60 to 110 words naming pace, register, one tick by its literal, and the laugh; no real person quoted (V16) | the word count and the four named elements all pass |
| C29 | Sources carry URLs | `references/vocal-research.md` | every claim about a real broadcaster carries a source URL, and every pace figure carries the word estimate and its derivation | each row of the source table resolves, and no coded observation is written as a measurement |

## Commands

Run from the skill folder with the profile path substituted for `<id>`.

```bash
# C8: ceilings written in numbers or units
grep -nE 'ceiling:.*([0-9]|%|dB|decibel|<)' personas/<id>.md

# C11: acronyms written as separated letters
grep -nE '\b[A-Z]\.[A-Z]\.|[A-Z]-[A-Z]-' personas/<id>.md

# C26: vendor, model or voice identifiers
grep -niE '(voice[_-]?id *:|[^_a-z]voice *:|model *:|vendor *:|<prosody|\[break\])' personas/<id>.md
```

## Failure modes

| Failure | Symptom on the page | Cause | Fix |
|---|---|---|---|
| Tick overload | every second sentence has a filler, a laugh or a breath | density above 5.5, or ticks used as personality | cut to 2.5 per 100 words, keep one interjection and one discourse marker, delete the rest |
| Accent caricature | vowel spelling used to signal nationality ("wee" for "we", "aboot") | accent written as spelling rather than as vowel colour and stress | strip the spellings, carry the accent in vowel colour and stress pattern only |
| Two profiles that sound alike | same register and pace, different names | distinctness check skipped or matches undocumented | re-run the gate, mutate in the documented order, or refuse the brief |
| Contradictory describing words | "warm and clinical", "bubbly and mournful" | vocabulary used as free text | re-resolve against the contradiction matrix, keep the word closest to the brief |
| Persona drift | episode four does not sound like episode one | ticks rotated without a fixed inventory, or EIQ changed mid-series | restore the saved inventory, version-bump any change, never edit a persona in place |
| Emotion performed rather than felt | the state is announced before it is audible | state written as an adjective, not as lever deltas | rewrite `on_cue` as behaviour: rate, pauses, sentence length, which tick changes |
| Low EIQ reads as spineless | the persona agrees with everyone and has no position | contagion written as compliance | give it a position it holds badly; it mirrors the emotion, not the argument |
| High EIQ reads as therapist | the persona narrates everyone's feelings and stops hosting | naming uncapped, offers about the relationship | one naming line per exchange, offer about the work, no reflective listening |
| Anger crosses into abuse | profanity, personal attack, sustained shouting | no ceiling, or a ceiling written in adjectives | enforce the ceiling: volume one step, no profanity, no personal attack, two segments, then the reset |
| Strained state never resolves | tired or angry for a whole episode | no recovery beat in the profile | add the ceiling and `recovery_behaviour`; one segment at full strain, then a partial recovery |
| Unpronounceable script | letters read aloud, numbers spelled out oddly, markup spoken | class assumed rather than tested | run the tag test, respell acronyms, strip markup the stack reads aloud |
| Mode collapse | cold open, link and outro all delivered the same way | modes never filled, or filled with the same values | give each mode its own deltas and note; the cold open is content, the outro is a landing |
| Exemplar drift | scripts are written from the voice note and read generic | exemplars missing, or present and ignored | write all four lines, hand them to the writer as rhythm models, check the draft against `never_says` |
| Floating voice | the host could be anywhere, in any room, with no body | `recording_context` left at defaults nobody checked, no breath, no object sound | state the room and the mic distance, give the persona one breath habit and one forbidden sound |
| Breath contradiction | audible breaths with no breath tick, or a sigh habit with no sigh | `breath_profile` written without reading `tick_inventory` | align the two; if the profile needs audible breath, a BRE id goes in the inventory |
| Relationship void | two hosts who never reference a shared history, a deference pattern or a joke | `standing_dynamic` left at defaults | write the relation, the history, one owned subject and one deferred subject per host |
| Lexicon bloat | twelve respellings, most for words the stack already says correctly | the lexicon used as a script instruction | keep only words a listener would hear mispronounced, and cut to the ones the persona actually says |
| Calibration drift | the one sentence meant to be frozen changes between series | the line edited during a revision | restore it, or bump `version` and record that the comparison restarts |
| Governance leak | a retired persona still blocking new builds, or a superseded profile edited in place | `canon_status` set and then ignored by the gate | retired profiles skip the gate but keep their id; a replacement takes a new id and sets `supersedes` |
| Example promoted | the store holds a voice the index never saw, because it is an example with a new name | a worked example copied into `personas/` instead of built | compare the candidate against the example at gate step 1, then mutate or refuse; guidance stays in `examples/` |

## The five-question sanity read

Before saving, read the profile as if you were the script writer. Answer these without looking anything up.

1. What does this person do with a pause? (If the answer is "nothing", the fingerprint is incomplete.)
2. What is the one sound a listener would imitate? (If there is no answer, the signature is wrong.)
3. What does this person do when the co-host is angry? (If the answer is the same for every EIQ value, EIQ was not used.)
4. Which two axes would I change to make a second host? (If the answer is "the name", the profile is not a persona, it is a label.)
5. Could I rebuild this voice from this file next year? (If any answer requires context outside the file, C12 fails.)

A profile that passes twenty-nine checks and fails this read is still a bad profile. The checks catch structural faults; the read catches a persona with no behaviour.
