# Generator procedure

Numbered, imperative, no interpretation required. Run in order. Steps 2, 3, 4, 8 and 22 can refuse the brief or stop the build; the rest complete or fail the checklist. A step is done when its named output is written into the profile.

## Contents

- Procedure
- Decision tables for steps 5 to 8, and table E for step 13
- Worked example A: free text brief to finished profile
- Worked example B: a strained brief with a co-host state
- What example B shows about the twelve craft fields

## Procedure

Nothing is written to `examples/`. The two worked examples below are guidance copies kept there, each with a banner and no index line; a real build saves to `personas/` and appends one line to `personas/index.jsonl`.

1. **Read the brief.** Copy a structured brief verbatim into `provenance.brief`. A free-text brief is condensed to these nine items: name, field, nationality, sex, describing words, EIQ target or behaviour hint, show shape, strained state, room. Write "unspecified" for anything absent. The result must satisfy V18, which is what a rebuild reads.
2. **Refuse impersonation.** Stop if the brief asks for a real living person's identity, voice or words, or for a character reproduced line for line. A name that coincides with a public or fictional figure is allowed under the override rule in `SKILL.md` when the field, the traits and the voice are invented, and `provenance` records the choice.
3. **Resolve defaults.** For each field the brief leaves silent, apply the default from the table in `references/persona-schema.md` and add a line to `assumptions_applied` in the form `room: default dry studio applied`. This covers `nationality`, `sex`, `tick_density`, `cue_scopes`, `version`, all five `recording_context` values, all five `breath_profile` values, `non_speech_sound`, `mode_behaviour`, `handoff_protocol` and `canon_status`. Stop if `display_name`, `field_of_expertise` or `describing_words` is unspecified; those have no defaults.
4. **Resolve describing words.** Run the five steps in `references/describing-words.md`. Record the mapping as `brief words -> resolved words`. A word the vocabulary cannot carry is kept in `provenance.brief` as the operator wrote it, and the nearest vocabulary word is used for the field; both are recorded. Three maximum, no cluster duplicates.
5. **Set the accent frame.** Map nationality to a starting vowel colour and stress pattern using table A. Then adjust by at most one step using the describing words: `theatrical` and `earthy` push toward broad or rounded, `precise` and `clinical` push toward neutral or fronted. Record the adjustment in `assumptions_applied`, because a rebuild that follows table A alone would land on a different vowel colour.
6. **Set register and pace.** Choose `pitch_register` from sex and field, not from personality. Female personas start at `mid_mixed`, male at `low_mixed`. Move one step up for `excitable`, `bubbly`, `urgent`, or a comedy field; one step down for `measured`, `mournful`, `avuncular`, or an authority field. Choose `pace_band` from the describing words: `brisk` or `impatient` gives `brisk`, `ponderous` or `mournful` gives `slow`, `urgent` or `excitable` gives `fast`, everything else gives `measured`. Set `pace_wpm_estimate` to the midpoint of the band window, rounded down to a whole number: 128, 145, 159, 176.
7. **Complete the fingerprint.** Set consonant crispness (`crisp` unless `folksy` or `earthy`, which take `soft`; `clipped` for `blunt` or `impatient`), sentence mix (`short_led` for `blunt`, `impatient`, `urgent`; `long_led` for `cerebral`, `ponderous`; otherwise `balanced`), timbre (table B), laugh shape and placement (table C), and the signature interjection at step 8.
8. **Select ticks.** Choose 6 to 8 ids from `references/tick-library.md`, at most 2 per type, and at most 3 shared with any one stored persona. Apply the selection rules at the end of that file. Nominate one tick as the signature, and not a laugh, breath or sign-off. Check its accent compatibility. Stop if fewer than 6 compatible ticks exist for the accent; the library has a gap that should be reported, not papered over.
9. **Set density** from the density table in `references/tick-library.md`, taking the fast list variant when the show reads items back to back. Write the three values into the profile.
10. **Set EIQ.** Convert the brief's behaviour hint to a float using table D. Write one sentence of justification naming the observable behaviour. Never write a band name alone, never write a personality adjective outside the vocabulary.
11. **Write the six states.** For each of angry, frustrated, tired, intense, curious and happy, write all five sub-fields from `references/emotion-engine.md`, then make three changes so the state belongs to this persona: (a) place one of this persona's own ticks in `ticks_under_load`; (b) express the state through this persona's declared anger shape, hot or cold; (c) write the `ceiling` using this persona's own levers, in words. Stop if any state lacks a sub-field.
12. **Write the recovery.** From `references/emotion-engine.md` Q1 to Q5: `shape`, `latency` (agrees with the band), `first_line` in baseline register with no state word, one physical `tell`, and one `does_not`. The first line must be sayable by this persona with this vocabulary.
13. **Write the lexical register.** From `references/voice-craft.md` L1 to L6. Derive openers from the persona's existing ticks and idiom, not from a generic list. Set `assertion` from table E, then check hedges against it with L1.
14. **Write the exemplars and the calibration line.** Four baseline lines of 8 to 30 words from E1 to E7, three `never_says` lines, then the calibration line from K1 to K6. Write the lines before the voice note, so the note describes language that already exists. Check the calibration duration by dividing words by `pace_wpm_estimate` and multiplying by 60.
15. **Write the pronunciation lexicon.** List only words in the exemplars or the field that a listener would hear mispronounced, 0 to 12 pairs, P1 to P5. Every acronym in the exemplars gets an entry. The voice note is written at step 21, so re-read the lexicon after it and add any word the note introduces.
16. **Write the breath profile.** From `references/studio-craft.md` B1 to B6, and reconcile it with the BRE ids: a soft or audible inhale needs a BRE tick, and no BRE tick means an inaudible inhale. Match `laugh_breath` to `laugh_shape`.
17. **Set the room and the objects.** From R1 to R7 and N1 to N5, using the brief's room mapped through R7, or the default. If a co-host is stored, copy its room and mic distance, and its object policy unless the difference is written into `assumptions_applied`.
18. **Write the standing dynamic.** From S1 to S8. For a two-host show, write the relation as a basis, the history in the first person plural, one to three owned subjects, one to three deferred subjects, and the running joke or `none`. For a single host, apply S2.
19. **Write the handoff.** From H1 to H6, with bridges that no other host on the show uses. Set `max_overlap_words` from `takes_floor`, then confirm that the angry state's `cohost_divergence` does not contradict it.
20. **Write the modes.** Enable the four required modes plus any the brief asks for, from M1 to M7. Give each one its own note of 6 to 30 words. Correction and sponsor read take no ticks. The outro names where the sign-off lands.
21. **Write the voice note.** One paragraph, 60 to 110 words, addressed to a script writer. It must name pace, register, one tick by its literal, and the laugh. No quotation of a real person; a tick literal appears unquoted. No real names, no units of loudness.
22. **Run the distinctness gate.** Follow `references/phonetic-distinctness.md` steps 1 to 8. Skip lines whose status is `retired`. Mutate the candidate only. Document every surviving match. Stop after three failed attempts and report.
23. **Validate.** Run every check in `GATE.md`, C1 to C28. Fix failures and re-run from step 22 if any axis changed.
24. **Save, index, report.** Create `personas/` and `personas/index.jsonl` if they are absent. Write `personas/<id>.md`. Append one JSON line to `personas/index.jsonl`. If the same id exists with a lower version, replace the line, do not append a second. Report the id, the EIQ band, the fingerprint, the matches accepted, and the file path. Nothing else.

## Decision tables for steps 5 to 8, and table E for step 13

Table A, accent frame:

| Nationality | Starting vowel_colour | Starting stress_pattern |
|---|---|---|
| british | neutral | even |
| australian | broad | punch_first |
| new_zealand | fronted | terminal_rise |
| scottish | rounded | punch_first |
| irish | fronted | terminal_rise |
| spanish_accented_english | fronted | even |
| us | neutral | punch_first |

Table B, timbre prior:

| Field of expertise | Timbre prior |
|---|---|
| design, architecture, literature | warm |
| science, mathematics, medicine | bright |
| economics, law, politics | flat |
| comedy, performance, sport | bright |
| psychology, health, social affairs | warm |
| history, arts, humanities | warm |
| technology, engineering | flat or nasal |

A row offering two values takes the first, unless a describing word points to the second: `nasal` for `conspiratorial` or `sardonic`. A field with no row takes `warm` and records the choice in `assumptions_applied`.

Table C, laugh:

| Describing word | Laugh shape |
|---|---|
| wry, dry, sardonic | single_beat |
| bubbly, excitable, sunny | staccato_run |
| warm, gentle, generous | descending_wheeze |
| deadpan, guarded, understated | silent_shake or none |
| blunt, confrontational, impatient | bark |
| theatrical, mischievous, playful | cackle |

Where two rows fire, the word that appears first in the resolved describing list decides. A persona with `warm` and `impatient` laughs a descending wheeze, because `warm` comes first.

Table D, EIQ anchor:

| EIQ anchor | Value |
|---|---|
| mirrors the room, never names feelings | 0.00 to 0.25, default 0.10 |
| feels it, notices late, de-escalates after the peak | 0.26 to 0.74, default 0.45 |
| names it, holds position, defuses others | 0.75 to 1.00, default 0.85 |

Table E, assertion:

| `assertion` | Describing words |
|---|---|
| states | blunt, brisk, precise, clinical, deadpan, dry, laconic, intense, urgent, confrontational, warm, sincere |
| qualifies | wry, measured, guarded, understated, sceptical, patient, ponderous, cerebral, avuncular, generous, earnest, mournful |
| asks | curious, playful, mischievous, conspiratorial, excitable, bubbly, sunny, breezy |

Read the resolved list in order; the first word that appears in this table decides. A word in no row leaves `states`. The table replaces a question to the operator, because assertion is derivable from the vocabulary the brief already resolved into.

## Worked example A: free text brief to finished profile

**Brief.** "A British woman in her forties who writes about buildings. Wry and measured. She should sound like she has been in the industry a long time and has opinions about staircases. Mid-level emotional control. Co-host show, she is the one who keeps it on the rails."

1. Extracted: name unspecified, field "urban design", nationality british, sex female, words wry and measured, EIQ mid, show shape two-host, strained state unspecified, room unspecified.
2. No real person named. Proceed.
3. `display_name` unspecified: stop for a name. The operator supplied "Harriet Voss". Room defaults to dry studio close mic, object policy to page turn and chair allowed with nothing forbidden, status to draft.
4. Words: wry, measured. Different clusters, no contradiction pair. Kept.
5. Accent frame: british gives neutral vowels and even stress. `wry` does not shift vowel colour.
6. Register: female starts `mid_mixed`; `measured` moves one step down to `low_mixed`. Pace: `measured` band, estimate 145.
7. Fingerprint: crisp consonants, balanced mix, warm timbre, single beat laugh at `self_deprecation`.
8. Ticks: TICK-003 er, TICK-014 blimey, TICK-020 right, TICK-030 heh, TICK-049 what I mean is, TICK-070 if you like, TICK-056 see you next week. Seven, no type repeated. Signature TICK-014, plosive.
9. Density 2.5 / 4.0 / 5.5.
10. EIQ: "mid-level emotional control" maps to 0.45.
11. Six states, cold anger shape, her own ticks, her ceilings.
12. Recovery: `subject_change` at `next_segment`, first line "Right. The second staircase, then.", tell "one dry laugh that does not reach the breath", does not explain that she has calmed down.
13. Lexical register: contractions sometimes, openers "The thing is,", "Right.", "I suppose", hedges soft, assertion qualifies, jargon explain, no co-host name, banned list of four management words.
14. Exemplars: four baseline lines, the disagreement qualified rather than flat, three lines she would never say. Calibration line 22 words, "blimey" once, opener once, 9.1 seconds at 145 wpm.
15. Lexicon: RIBA to "ree bah", because she says it in the question line.
16. Breath: no BRE id in the inventory, so the inhale is inaudible. Sigh rare, laugh breath voiceless, fry at sentence end.
17. Room: dry studio, close, controlled plosives, low breath audibility, and faint room tone recorded in `assumptions_applied` as a deviation from the default `none`, because the room is treated.
18. Standing dynamic: two-host, relation a shared planning inquiry, opens_show cohost, closes_show self, owned subjects design and planning law, deferred subject sports analytics, the staircase as the running joke.
19. Handoff: waits, zero overlap, two bridges each way, yields when the co-host leans back.
20. Modes: cold open, intro, link, correction, outro, each with its own note.
21. Voice note written, 103 words.
22. Gate: store held two other personas; matches on stress pattern and sentence mix with the food science host, no core match, both documented, pass.
23. Checklist: C1 to C28 pass.
24. Saved to `personas/` as harriet_voss with one index line. The skill author later copied it to `examples/harriet_voss.md` as guidance, where it carries no index line; a build writes nothing there.

The finished profile is in `examples/harriet_voss.md` and is the canonical example of a mid-EIQ build.

## Worked example B: a strained brief with a co-host state

**Brief.** "Second host for a two-hander about food science. Spanish accent, woman, warm and curious. The other host is the hot one and he gets angry on mic. I want this one to be the opposite: she should be tired in the back half of the show but still keep it moving. Don't make her a therapist."

1. Extracted: field "food science", nationality spanish_accented_english, sex female, words warm and curious, EIQ unspecified, co-host state angry, own state tired, show shape two-host, room unspecified.
2. Proceed.
3. Name supplied by the operator: "Noor Haddad". Room copied from the first host at step 17, status default draft.
4. Words: warm, curious. Different clusters, no contradiction. Kept.
5. Accent frame: spanish_accented_english gives fronted vowels and even stress. `warm` does not shift it. Stress moves to `trailing_off` as a documented deviation, because the brief asks for a host who sounds like she is thinking aloud and that is where the cue lives.
6. Register: female starts `mid_mixed`; neither word moves it. Pace: `measured` at 145 by the table, later moved to `brisk` during collision resolution, recorded in `accepted_matches`.
7. Consonants soft, mix balanced, laugh descending wheeze at `guest_error`. Timbre `warm` overrides the science prior in table B, because the brief names warmth as the point of the persona, and the override is recorded in `assumptions_applied`.
8. Ticks: TICK-006 hmm, TICK-011 ooh, TICK-023 I mean, TICK-033 wheeze, TICK-043 breathy onset, TICK-064 here's the thing, TICK-057 thanks for listening. Seven. Signature TICK-006, nasal.
9. Density defaults.
10. EIQ: the brief rules out the low band, because a contagious host cannot hold a position against an angry co-host. It does not rule out the high band; it rules out the therapist failure, which is a behaviour inside that band. Both 0.55 and 0.85 satisfy the brief. Choose 0.85, because this host is the show's only de-escalation route and a mid-band host leaves the co-host's anger unnamed.

Then the band choice is tested against the brief's own requirement, at three values, before it is written:

| EIQ | Line she says when the co-host is angry and she is tired | Verdict against the brief |
|---|---|---|
| 0.10 | "You're right. Sorry. I'm just tired, I'm not thinking." | Fails: she becomes the co-host's state and stops moving the segment |
| 0.55 | "I'm running out of steam here. Give me the short version and I'll take it from there." | Passes the brief, but the co-host's anger goes unnamed, so the de-escalation is oblique and late |
| 0.85 | "You're angry, and I'm too tired to pretend otherwise. Give me the short version and I'll take it from there." | Passes: names both states in one line, and the offer is about the work, not the relationship, which is what keeps it out of therapist mode |

The therapist risk at 0.85 is handled in the profile by two constraints, not by lowering the band: one naming line per exchange, and every offer phrased as a question about the segment.

11. Six states with her ticks and her warm register. The tired state uses TICK-043 as the load marker and caps at one segment. Anger is cold, because her consonants are soft and rising volume would break the timbre.
12. Recovery: `apology` at `next_turn`, first line "That was too sharp. Say the objection again and I will hear it.", tell "one hand flat on the table, then a slow exhale", does not ask the co-host how they feel. `next_turn` is legal at 0.85 and illegal at 0.10, which is the point of Q1.
13. Lexical register: contractions always, openers "Here's the thing,", "I mean,", "So", hedges none, assertion states, jargon explain, co-host addressed by name, four banned food-marketing words.
14. Exemplars: the claim carries the pH strip, the disagreement is flat rather than qualified, the laugh is a written wheeze. Calibration line 22 words with "hmm" and the opener, 8.3 seconds at 160 wpm.
15. Lexicon: pH to "pee aitch", the only word in her lines a stack would mangle.
16. Breath: TICK-043 in the inventory, so the inhale is audible. Sigh rare, laugh breath through the nose, fry at sentence end.
17. Room: dry studio close, copied from the first host, plosives controlled because an audible inhale at a close mic pops otherwise. Object policy aligned, page turn forbidden for both.
18. Standing dynamic: two-host, relation built on distrust of each other's evidence, either host opens, owned subjects food science and food safety, deferred subjects sports analytics and betting markets.
19. Handoff: waits, zero overlap, bridges that the first host does not use, yields when the co-host takes a breath.
20. Modes: the four required plus the listener letter, each with its own note.
21. Voice note written, 88 words.
22. Distinctness: the derived fingerprint matched `harriet_voss` on pace band, stress pattern and sentence mix, three matches with one of them core. Inside the limits, but sitting on the total cap. One mutation: pace from `measured` to `brisk`, which clears the core match and gives the two hosts different tempos. Final state two non-core matches with `harriet_voss` and one pace match with `des_larkin`, all three written into `accepted_matches`.
23. Checklist passed after the pace change.
24. Saved to `personas/` as noor_haddad with one index line. The skill author later copied it to `examples/noor_haddad.md` as guidance, where it carries no index line; a build writes nothing there.

The point of example B: the brief constrained the EIQ band from both sides, and the band was chosen by testing candidate lines against the brief, not by picking a number that felt right.

## What example B shows about the twelve craft fields

The band changed four lines and no sound. At 0.10, 0.55 and 0.85 the profile keeps the same accent, the same ticks, the same four exemplar lines, the same calibration line, the same room and the same modes. What moves is when she names a feeling, how late she notices, and whether her offer arrives before or after the peak. Any draft where the 0.85 version reads calmer at rest has broken invariant 5 in `references/emotion-engine.md`.
