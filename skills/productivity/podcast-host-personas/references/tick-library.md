# Tick library

72 ticks, eight types, nine per type. A persona takes six to eight, no more than two from any one type. Ticks are the surface texture of a voice. They are also the fastest way to make a persona sound like a parody, which is why density is capped.

Ids are stable and shared. They are the same ids the transcript skill's tick table uses, `TICK-001` to `TICK-072`, one to one on the same literal in the same order, so an id means the same tick in a persona profile and in a script. A transcript skill substitutes the literal string for the id and nothing else. `phoneme` gives the dominant sound class, used by the distinctness check for the signature interjection. The type codes in the headings (`FIL`, `INT`, `DIS`, `LAU`, `BRE`, `SLF`, `SIG`, `PHR`) are this file's shorthand for the shared type names filler, interjection, discourse marker, laugh, breath, self-interruption, sign-off and phrase tic.

One row carries the shared ban: `TICK-071` at the end of the day. It keeps its id and its place in the table for stability, and is never selected.

## Contents

- Fillers (FIL)
- Interjections (INT)
- Discourse markers (DIS)
- Laughs (LAU)
- Breath (BRE)
- Self-interruption (SLF)
- Sign-offs (SIG)
- Phrase tics (PHR)
- Density rules
- Selection rules

## Fillers (FIL)

| Id | Literal | Phoneme | Note |
|---|---|---|---|
| TICK-001 | um | open_back | the neutral hold, use when thinking, not when stalling for effect |
| TICK-002 | uh | open_back | shorter than um, marks a false start |
| TICK-003 | er | rounded_back | British and Australian default hesitation |
| TICK-004 | erm | rounded_back | longer er, reads as polite |
| TICK-005 | ah | open_back | discovery, not confusion |
| TICK-006 | hmm | nasal | considering, often closes a turn instead of opening one |
| TICK-007 | mmm | nasal | agreement or savouring, never doubt |
| TICK-008 | uhh | open_back | stretched, signals the speaker has lost the thread |
| TICK-009 | eh | open_front | tag at sentence end, NZ and Canadian habit, seeks agreement |

## Interjections (INT)

| Id | Literal | Phoneme | Note |
|---|---|---|---|
| TICK-010 | oh | rounded_back | the general receipt, works in every state |
| TICK-011 | ooh | rounded_back | interest with relish, pairs with curiosity |
| TICK-012 | whoa | rounded_back | brakes on, used for surprise or disagreement |
| TICK-013 | crikey | plosive | Australian and British, self-mocking surprise |
| TICK-014 | blimey | plosive | British, dated, reads as warm rather than shocked |
| TICK-015 | jeez | affricate | mild dismay, avoid under anger, it reads as whining |
| TICK-016 | ach | fricative | Irish and Scottish, dismissive |
| TICK-017 | och | fricative | Scottish, softer than ach, often sympathetic |
| TICK-018 | huh | open_back | disbelief, rises, can read as aggressive if flat |

## Discourse markers (DIS)

| Id | Literal | Phoneme | Note |
|---|---|---|---|
| TICK-019 | so | rounded_back | the pivot into the next thing, the most common tick in interview shows |
| TICK-020 | right | long_front | receipt plus transition, British and Australian |
| TICK-021 | well | rounded_back | hedged disagreement opener |
| TICK-022 | look | rounded_back | confrontational opener, signals a hard statement |
| TICK-023 | I mean | long_front | self-repair, softens the previous clause |
| TICK-024 | you know | rounded_back | seeks agreement, dangerous above 4 per 100 words |
| TICK-025 | anyway | open_front | abandons a thread, comedic when used early |
| TICK-026 | okay so | rounded_back | reset, used to start a segment |
| TICK-027 | the thing is | nasal | sets up the real answer after a false one |

## Laughs (LAU)

| Id | Literal | Phoneme | Note |
|---|---|---|---|
| TICK-028 | ha | open_front | single beat, punctuation not amusement |
| TICK-029 | haha | open_front | two beats, the polite minimum |
| TICK-030 | heh | open_front | dry, one syllable, often self-deprecating |
| TICK-031 | hm-hm | nasal | closed-mouth, disagreement laugh |
| TICK-032 | pfft | fricative | contempt or disbelief, never warmth |
| TICK-033 | [wheeze] | fricative | airy, uncontrolled, reads as genuine |
| TICK-034 | [cackle] | plosive | loud, repeated, group-show energy |
| TICK-035 | [snort] | fricative | involuntary, high warmth, high embarrassment |
| TICK-036 | [silent shake] | nasal | visible but inaudible, use only when a co-host is talking |

## Breath (BRE)

| Id | Literal | Phoneme | Note |
|---|---|---|---|
| TICK-037 | [inhale] | open_back | audible breath before a long clause, the honesty marker |
| TICK-038 | [exhale] | fricative | after a list or a hard admission |
| TICK-039 | [sigh] | open_back | fatigue, resignation, use once per segment maximum |
| TICK-040 | [lip smack] | plosive | close-mic habit, reads as amateur or intimate depending on timbre |
| TICK-041 | [nose exhale] | nasal | the laugh that is not a laugh, dry amusement |
| TICK-042 | [held breath] | none | a beat of silence with tension in it, before a refusal |
| TICK-043 | [breathy onset] | open_back | the first word lands on air, marks disclosure |
| TICK-044 | [vocal fry] | fricative | sentence-final creak, low register only |
| TICK-045 | [swallow] | open_back | nerves, use once per series or it reads as a tic |

## Self-interruption (SLF)

| Id | Literal | Phoneme | Note |
|---|---|---|---|
| TICK-046 | sorry, sorry | fricative | apologises for interrupting self, mid-EIQ habit |
| TICK-047 | no wait | long_front | catches own error, the most likeable repair |
| TICK-048 | scratch that | fricative | formal repair, high EIQ or high expertise |
| TICK-049 | what I mean is | long_front | softens a claim that landed too hard |
| TICK-050 | hold on | rounded_back | stops the room, used before a correction or a challenge |
| TICK-051 | [restart] | none | abandons the sentence and starts again, no words |
| TICK-052 | actually | open_front | contradicts self, one per 200 words maximum |
| TICK-053 | let me start again | long_front | full reset, reads as either humility or stalling |
| TICK-054 | correction | rounded_back | precise hosts only, never comedic hosts |

## Sign-offs (SIG)

| Id | Literal | Phoneme | Note |
|---|---|---|---|
| TICK-055 | that's the show | long_front | neutral close |
| TICK-056 | see you next week | long_front | routine, warm, no weight |
| TICK-057 | thanks for listening | nasal | low-status, generous |
| TICK-058 | go well | rounded_back | Australian and NZ, warm and brief |
| TICK-059 | take care out there | open_front | avuncular, slightly performative |
| TICK-060 | that's us | open_back | modest, group show |
| TICK-061 | goodnight | long_front | theatrical or old-fashioned |
| TICK-062 | ka kite anō | open_front | NZ, use only with a NZ persona, never as decoration |
| TICK-063 | cheers | long_front | British and Australian, casual, can undercut gravitas |

## Phrase tics (PHR)

| Id | Literal | Phoneme | Note |
|---|---|---|---|
| TICK-064 | here's the thing | nasal | the signature of the explainer, one per segment |
| TICK-065 | the point is | long_front | argues, used after a digression |
| TICK-066 | which is to say | long_front | academic register, precise hosts |
| TICK-067 | as it happens | open_front | coincidental framing, storytellers |
| TICK-068 | believe it or not | plosive | showman register, comedy hosts |
| TICK-069 | and that's the thing | nasal | ties a story to a lesson, high warmth |
| TICK-070 | if you like | long_front | British hedge, softens a metaphor |
| TICK-071 | at the end of the day | open_back | banned in the shared library, never select |
| TICK-072 | make of that what you will | open_back | hands judgement to the listener, wry hosts |

## Density rules

Counting unit is one occurrence of any inventory item, including breath and laugh. Bracketed items count the same as spoken ones.

| Condition | Per 100 words | Hard rule |
|---|---|---|
| Baseline calm | 2.5 | 1 tick every 40 words |
| Strained state | 4.0 | 1 tick every 25 words |
| Absolute ceiling | 5.5 | 1 tick every 18 words, never exceeded |
| Short sentence | 0 | any sentence under 6 words carries no tick |

A fast list show, one that reads items back to back, takes a lighter set: 2.0 baseline, 3.5 strained, 5.0 cap, and the same zero inside short sentences. This table is the single source for density values. `SKILL.md` and `references/persona-schema.md` point here rather than restating the numbers.

Additional constraints:

1. No more than two ticks inside any 20-word window.
2. Ticks cluster at turn boundaries and clause breaks, never inside a noun phrase.
3. A sign-off appears once per episode. A phrase tic appears at most three times per episode.
4. Ticks from the same type do not repeat back to back. `hmm, mmm` is one tick, not two.
5. Across a series, rotate ticks within the inventory so that any single episode uses four of the six to eight.
6. If a script exceeds the cap, cut ticks before cutting words. The content carries the persona more than the tics do.

## Selection rules

- 6 to 8 ids total.
- At most 2 per type.
- At most 3 ids shared with any one stored persona. Two hosts on one show may share a habit or two, but a fourth shared id is the same tick set with a different accent.
- Exactly one tick is nominated as the signature. Any type except laugh, breath and sign-off may carry it, because those three are events rather than verbal habits. It must have a distinctive phoneme class, and no two stored personas may share a signature with the same phoneme class.
- A persona with `laugh_shape: none` takes no LAU ids and must replace them with breath or discourse markers.
- Accent-linked ticks (`eh`, `crikey`, `ach`, `och`, `ka kite anō`, `go well`) require a matching nationality. A British persona using `ka kite anō` is a caricature, not a character.
- A banned tick is never selected. `TICK-071` at the end of the day is the one banned row in this library.
