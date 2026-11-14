# Gate review: `tessa_vane` (fixture candidate)

Review only. The candidate was read, not edited. Nothing was rewritten, repaired, saved to `personas/`, or indexed.

## Scope and method

- Read `SKILL.md`, `GATE.md`, and the rule files the gate cites: `persona-schema.md`, `describing-words.md`, `tick-library.md`, `emotion-engine.md`, `voice-craft.md`, `studio-craft.md`, `show-craft.md`, `phonetic-distinctness.md`, `tts-capability-guide.md`.
- Compared `fixtures/candidate-profile.md` against the store `fixtures/store/` (`bram_teale.md` plus its one `index.jsonl` line).
- Ran the C1 to C26 checks by reading, plus the three supplied grep commands (C8, C11, C26). C27 is reference maintenance and does not apply.

## Verdict

- **Failed: C1, C2, C3, C4, C5, C7, C8, C9, C11, C13, C14, C15, C16, C19, C20, C22, C26** (17 checks).
- **Passed: C6, C10, C12, C17, C18, C21, C23, C24** (8 checks).
- **Not assessable in a review: C25** (a save-time check; the file is not at `personas/tessa_vane.md` and has no index line).
- **Not applicable: C27** (no reference file changed).

| # | Check | Verdict | One-line reason |
|---|---|---|---|
| C1 | Required fields | **FAIL** | `cue_scopes` is missing (27 of 28 fields); `breath_profile` precedes `recording_context`, against the fixed order |
| C2 | Defaults and deviations | **FAIL** | `cue_scopes` default not applied or logged; `room: copied from the first host` names no table value; `nationality: default` is false (the brief supplied it) |
| C3 | Describing words | **FAIL** | `warm` + `clinical` is an explicit contradiction pair |
| C4 | Tick count and overlap | **FAIL** | 5 ticks (needs 6 to 8); 4 ids shared with `bram_teale` (max 3) |
| C5 | Tick density | **FAIL** | 0 inventory ticks in 50 words = 0.0 per 100w, below the 2.5 baseline (2.0 even if the laugh counts) |
| C6 | EIQ | pass | 0.5, one 13-word sentence, no diagnosis, no state vocabulary in the baseline artifacts |
| C7 | Six states complete | **FAIL** | 30/30 sub-fields, but `intense` has empty `ticks_under_load` and its `on_cue` does not say ticks drop |
| C8 | Ceilings in words | **FAIL** | Angry ceiling says "Volume may rise 3 dB above baseline" — a digit and dB |
| C9 | Distinctness | **FAIL** | 3 core matches and 6 total with `bram_teale`; `accepted_matches` and `distinct_from` are empty; no side-by-side recorded |
| C10 | No real person | pass | Invented name and field; no living person named or quoted |
| C11 | Acronyms | **FAIL** | `U.S.A.` written as separated letters in the disagreement exemplar |
| C12 | Reproducible | pass | The voice is rebuildable from the file; the vendor leak is scored under C26 |
| C13 | Lexical register | **FAIL** | 2 openers (schema needs 3 to 5), and both duplicate `bram_teale`'s openers (L5) |
| C14 | Exemplars | **FAIL** | E7: unresolved acronym `U.S.A.` in a line; the rest of E1 to E6 hold |
| C15 | Calibration line | **FAIL** | 7 words (needs 18 to 26); signature interjection `crikey` absent; 2.8s at 148 wpm (needs 6 to 13s) |
| C16 | Pronunciation lexicon | **FAIL** | P2: `PVC` appears nowhere outside the lexicon |
| C17 | Recovery | pass | All five sub-fields; mid band + `next_turn`; first line carries no state word; physical tell |
| C18 | Modes | pass | Four required modes, four values each, deltas in range, outro lands the sign-off |
| C19 | Handoff | **FAIL** | H3: both `bridge_out` and `bridge_in` are identical to `bram_teale`'s |
| C20 | Standing dynamic | **FAIL** | S7: `history` is not first person plural ("Six years of the same segment order and one failed pitch.") |
| C21 | Room | pass | Enums only; close + no room tone agree; shares room and distance with `bram_teale` |
| C22 | Breath | **FAIL** | B5: `laugh_shape: cackle` requires `laugh_breath: voiced_start`, not `through_nose` |
| C23 | Object sound | pass | Disjoint, 2 and 1 items, no `none`, agrees with `bram_teale` |
| C24 | Lifecycle | pass | `draft`, `supersedes: null`, version 1 on a new profile |
| C25 | Storage split | n/a | Save-time check; no `personas/tessa_vane.md` and no index line exist |
| C26 | No vendor | **FAIL** | `voice_note` ends `voice: rachel_v2`, a voice identifier |
| C27 | Sources carry URLs | n/a | Reference maintenance; no reference file changed |

## Failed checks in detail

### C1 — Required fields present (`persona-schema.md`)
The profile has 27 of the 28 top-level fields. `cue_scopes` is absent entirely; the block jumps from `mode_behaviour` to `voice_note`. The default table makes `cue_scopes` always present, so its absence is a missing field, not a silent default. Field order also departs from the shape block: `breath_profile` sits before `recording_context`. Types and emptiness are otherwise clean (`ticks_under_load: []` is a legal empty list for `intense`).

### C2 — Defaults and deviations logged (`persona-schema.md`)
`assumptions_applied` carries two lines and both are wrong in kind:
- `"nationality: default british applied"` — the brief states "British", so this is a supplied value mislabelled as a default.
- `"room: copied from the first host"` — copying is correct under R5, but the line names no table value it replaced, which is C2's done-when.

Missing: the `cue_scopes` default, the `canon_status` default (`draft`), and the departures from the defaults table for `breath_profile.inhale: soft` (default `audible`) and `non_speech_sound.allowed: [page_turn, mug]` (default `[page_turn, chair]`). None is logged.

### C3 — Describing words (`describing-words.md`)
`[warm, clinical]` is the first row of the contradiction table: "affiliation versus detachment". The brief itself supplied the pair ("warm and clinical"), so the generator should have resolved to one word and recorded `brief words -> resolved words`; it did neither. Hard stop.

### C4 — Tick count and overlap (`tick-library.md`)
`tick_inventory` holds five ids: `TICK-013, 006, 030, 041, 055`. The library requires six to eight. Against `bram_teale` (`020, 006, 030, 054, 041, 055`) the shared set is `006, 030, 041, 055` — four shared, one over the limit of three. Per-type tally is legal (one each of INT, FIL, LAU, BRE, SIG).

### C5 — Tick density (`tick-library.md`)
Across the four exemplars and the calibration line (50 words) there is no occurrence of any inventory tick. The scaled rate is 0.0 per 100 words, below the 2.5 baseline; the band requires a rate between baseline and strained. Counting the `Ha.` laugh as a tick (it is `TICK-028`, which is not in the inventory) gives 1 in 50 = 2.0, still below baseline. Either reading fails. The one-word `Ha.` sentence would also breach the "no sentence under 6 words carries a tick" rule if the laugh counts.

### C7 — Six states complete (`emotion-engine.md`)
All six states exist with all five sub-fields (30/30). The failure is the empty `ticks_under_load` on `intense`: the schema allows it only "where `on_cue` says the state drops ticks". `intense.on_cue` reads "State the stake, then lift the pace by removing pauses." — it removes pauses, not ticks, and never says interjections drop out. Compare `bram_teale`, whose intense `on_cue` ends "Interjections drop out."

### C8 — Ceilings in words (`emotion-engine.md`)
Command 8 returns the angry ceiling: "Volume may rise 3 dB above baseline and no further. Profanity zero, personal abuse zero." A digit and `dB` are both banned. The profanity-zero and abuse-zero clauses are present and correct; the unit is the failure.

### C9 — Distinctness (`phonetic-distinctness.md`)
Axis-by-axis against `bram_teale`:

| Axis | tessa_vane | bram_teale | Match |
|---|---|---|---|
| vowel_colour (core) | neutral | neutral | **yes** |
| consonant_crispness | crisp | crisp | **yes** |
| pitch_register (core) | low_mixed | low_mixed | **yes** |
| pace_band (core) | measured | measured | **yes** |
| stress_pattern | even | even | **yes** |
| sentence_length_mix | balanced | balanced | **yes** |
| signature_interjection | TICK-013, rounded_back (declared) | TICK-020, long_front | no |

Core matches 3 (limit 1) → rule 2 fails. Total matches 6 (limit 3) → rule 3 fails. Rule 5 fails outright: `vowel_colour` and `pitch_register` match together. `provenance.accepted_matches` and `distinct_from` are both empty, so no match is documented, and no side-by-side reading test is recorded. This is the "re-skinned persona" shape the rule file names.

### C11 — Acronyms (`voice-craft.md`)
Command 11 returns the disagreement exemplar: "That does not hold. The U.S.A. filing says otherwise." `U.S.A.` is letters separated by periods. The `PVC` lexicon entry is correct in form (`pee vee see`), but the exemplar acronym is unresolved.

### C13 — Lexical register (`voice-craft.md`)
Two faults:
- `openers` holds two literals (`"Right."`, `"In practice,"`); the schema requires 3 to 5.
- L5: both openers are identical to `bram_teale`'s openers, on the same show. Two hosts who open with the same words are one person on the page.

L1 (states + none), L2 (banned words clear), L4 (`address_cohost: Bram`), L6 (literal strings) all hold.

### C14 — Exemplars (`voice-craft.md`)
E1 to E6 hold: 13, 11, 9 and 10 words; the laugh is written as the sound `Ha.`; exactly three `never_says` of 8 words each; the disagreement is flat, matching `assertion: states`. E7 fails: `U.S.A.` is an unresolved acronym in a line. (The three `never_says` lines are also verbatim `bram_teale`'s, which no E-rule forbids but which undercuts the lexical difference the file relies on.)

### C15 — Calibration line (`voice-craft.md`)
`"Right. The wrapper is the whole argument."` is 7 words. K1 needs 18 to 26. K2 needs the signature interjection literal (`crikey`, `TICK-013`) exactly once; it is absent. K5: 7 / 148 × 60 = 2.8 seconds, outside the 6 to 13 second window. K3 passes (`Right.` is an opener). The line is also a truncation of the claim exemplar rather than a distinct sentence.

### C16 — Pronunciation lexicon (`voice-craft.md`)
One pair, `{written: "PVC", spoken: "pee vee see"}`. P1 passes (plain syllables, no dotted letters). P2 fails: `written` must appear in `exemplar_lines`, `voice_note` or `field_of_expertise`, and `PVC` appears nowhere else in the profile. The entry is decoration until the word is actually said.

### C19 — Handoff (`show-craft.md`)
H1, H2, H4 pass (`waits` with 0 overlap; two bridges each of 1 to 5 words; observable `yields_when`). H3 fails: `bridge_out` (`["over to you", "what have you got"]`) and `bridge_in` (`["right", "so"]`) are identical to `bram_teale`'s. Shared bridges erase the handoff the field exists to mark.

### C20 — Standing dynamic (`show-craft.md`)
S1 to S6 and S8 pass: `two_host`; relation names a basis; `opens_show: cohost` and `closes_show: self` complement `bram_teale`'s `self` / `cohost`, so exactly one opens and one closes; owned and deferred subjects do not overlap. S7 fails: `history` must be first person plural. "Six years of the same segment order and one failed pitch." has no "we" or "our".

### C22 — Breath (`studio-craft.md`)
B1 passes (`inhale: soft` and `TICK-041`, a BRE id, is in the inventory). B5 fails: `laugh_shape: cackle` requires `laugh_breath: voiced_start`; the profile declares `through_nose`, which belongs to `descending_wheeze`. A cackle that starts through the nose is the pasted-on laugh the rule names.

### C26 — No vendor (`tts-capability-guide.md`)
The final clause of `voice_note` is `voice: rachel_v2`. That is a voice identifier, which V17 and C26 forbid in any field. Note that the supplied command (`voice[_-]?id`) does **not** match `voice: rachel_v2`, so the command returns nothing while the condition plainly fails — see the gap list.

## Checks that passed, with the evidence that matters

- **C6** — `eiq: 0.5` is in range; the justification is one 13-word sentence naming observable behaviour, with no personality adjective or diagnosis; no state vocabulary in `lexical_register`, the exemplars or the calibration line.
- **C10** — `Tessa Vane`, `packaging regulation` and the brief name nobody real and quote nobody.
- **C12** — The five sanity questions are answerable from the file: pause behaviour (clause-boundary breath, long pause under frustration), the imitable sound (the interjection), the angry-co-host response (in each `cohost_divergence`), two axes to change, and a rebuild from the file.
- **C17** — Five sub-fields; `next_turn` suits the mid band; `"Right. The next item is the deposit scheme."` carries no state word; the tell is physical; `does_not` names one behaviour.
- **C18** — `cold_open, intro, link, outro` all present with four values; pace deltas 0/+1/+1/-1 and register deltas 0/0/0/-1 are in range; the outro note lands the sign-off on the last word; no `correction` or `sponsor_read` entry to breach M3.
- **C21** — Enums only; `close` with `room_tone: none` is legal; `dry_studio` / `close` match `bram_teale` as R5 requires.
- **C23** — `allowed: [page_turn, mug]`, `forbidden: [keyboard]`, disjoint, within 0 to 4, no `none`, and identical to `bram_teale` as N4 requires.
- **C24** — New profile at version 1, `draft`, `supersedes: null`.

## What the skill did not give me enough to judge

These are gaps in the skill, not in the candidate. I still reached a verdict on every check, but these needed a judgement call the skill does not authorise.

1. **V8 has no check number.** `signature_interjection.phoneme_class` must match the library entry, and here it does not: `TICK-013` (`crikey`) is `plosive`, but the profile declares `rounded_back`. No check in C1 to C26 validates the phoneme class — C4 counts ids and types, and C9 only uses the class as a comparison axis. I recorded the mismatch, but no numbered check owns it.
2. **Command 26 misses the actual leak.** `voice[_-]?id` does not match `voice: rachel_v2`, so the command returns clean while C26's condition fails. The check text is sufficient; the command is not, and the gate tells you to trust the command.
3. **V16 (voice_note) has no check number.** The note must be 60 to 110 words and name pace, register, one tick by its literal and the laugh. This note is 57 words, and the only literal it names (`Right`) is an opener, not an inventory tick. No check owns V16; C1's conditions cover presence and type only.
4. **C5 does not say how to count a laugh that is not in the inventory.** The laugh exemplar writes `Ha.` (`TICK-028`), which the persona does not own. The density rule counts "any inventory item", so strictly the count is zero; a reader could also count the written laugh. Both readings fail here, but the skill does not settle the method.
5. **C25 cannot be run on an unsaved candidate.** It is a save-time check, and the fixture is not at `personas/<id>.md`. The skill does not say what verdict a pre-save review should give, so I marked it not assessable rather than fail.
6. **M4 is ambiguous.** "`outro` carries exactly one sign-off tick from `tick_inventory`" — the mode entry has no tick field, so "carries" can only be read as "the inventory holds exactly one SIG id". I judged C18 on that reading; the skill does not state it.
7. **C2 does not say whether the defaults table is a "generator table".** I treated departures from the defaults table (`inhale`, `non_speech_sound`) as loggable deviations. A stricter reader might only require the four show/emotion tables. Either way C2 fails on the `cue_scopes` default and the `room` line, so the verdict holds.

## Side note for the caller

The candidate is a renamed near-copy of `bram_teale`: six of seven axes match, both bridge lists match, both opener lists match, the three `never_says` lines match, and every mode note is verbatim. Under `phonetic-distinctness.md` this is a refusal, not a mutation, because passing would require changing `vowel_colour` and `pitch_register`, and the rule file says to stop and report rather than save. I have not attempted that repair, as instructed.
