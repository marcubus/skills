# Vocal levers

The working half of the research, split out because every generation reads it. Table 1 maps a described vocal property to a lever an agent controls in a script or a delivery call. Table 2 gives the direction and magnitude of every lever for the six cued states, plus the physical correlates that make a state read as felt, and the failure mode that turns it into caricature.

Everything here is a coded observation or a design convention, never a measurement. Evidence, sources and how each claim is labelled: `references/vocal-research.md`.

## Contents

- Table 1: vocal property to lever
- Table 2: emotional shift table
- What the emotion table will not do

## Table 1: vocal property to lever

The bridge between a described voice and a script or a delivery instruction. "Script" means the agent can control it with words on the page. "Delivery" means it belongs to the synthesiser or the reader, and the script can only hint.

| Property | Lever | Control | Operational definition | Proxy a reader can check |
|---|---|---|---|---|
| Speed | pace | script and delivery | words per minute relative to the persona baseline | count words per minute of scripted speech |
| Pause length | pause length | script and delivery | beats of silence at clause, sentence and turn boundaries | count commas, full stops, paragraph breaks |
| Register | pitch register | delivery | band plus resonance site, fixed per persona | does the voice sit above or below the co-host |
| Expressiveness | pitch movement | delivery and script | range of pitch within a sentence, and direction at the end | rising, falling, or flat sentence endings |
| Loudness | volume dynamics | delivery | steps above or below baseline, plus whether it varies within a sentence | are stressed words marked, or is the line even |
| Clarity | articulation crispness | script and delivery | how separated consonants are, and whether word endings land | can the last consonant of each word be heard |
| Syntax | sentence length | script | distribution of words per sentence | words per sentence, and share under 10 words |
| Verbal texture | interjection inventory | script | which ticks appear, and how often | ticks per 100 words |
| Amusement | laugh | script | shape, placement, and whether it is voiced | where a laugh sits relative to the joke |
| Fluency | rate of self-interruption | script | repairs per 100 words and type of repair | count restarts and corrections |

Two rules follow from this table.

1. A lever that is delivery-only cannot be enforced by the script. If the target stack has no pitch control, pitch register must be carried by voice choice or by sentence shape, and the persona must say which.
2. Every emotional shift must move at least one script lever. A state expressed only in delivery levers cannot be cued in a plain transcript, and will vanish in a basic pipeline.

## Table 2: emotional shift table

Six cued states. Deltas are relative to that persona's calm baseline. Magnitudes are design conventions, not measurements: +/- one step is slight, two is clear, three is large. Physical correlates are what make the state read as felt rather than performed; the failure mode is what turns it into caricature.

### Angry

| Lever | Direction and magnitude |
|---|---|
| Pace | +2 steps (about +20 to 25 percent), or -1 for cold anger |
| Pause length | -2 (pauses shorten or vanish), except the deliberate pressure pause |
| Pitch register | 0, ceiling +2; register does not move, the top of the range does |
| Pitch movement | +2, narrower and more repetitive, less melodic |
| Volume | +1 to +2, never a shout |
| Articulation | +2 (consonants harden), degrading only at the extreme |
| Sentence length | -2 (short declaratives, 3 to 8 words) |
| Interjections | +1, but the inventory narrows to two items |
| Laugh | near zero; if present, one beat and contemptuous |
| Self-interruption | -1 (fewer repairs, more certainty) |

Physical correlates: breath taken high in the chest and held; jaw tight, which flattens vowels; the first word of a clause stressed harder than the rest; a hard attack on plosives; the pitch peak arriving early in the sentence and staying there. L5 and L7 support the direction for the hot profile: higher F0, faster rate, greater intensity.

Failure modes: shouting without articulation loss reads as acting; sustained volume with no breath reads as a machine; profanity or personal attack turns the host into the aggressor; growling on every line turns anger into a monster voice.

### Frustrated

| Lever | Direction and magnitude |
|---|---|
| Pace | +1, with stumbles rather than acceleration |
| Pause length | -1, plus one long exasperated pause per segment |
| Pitch register | 0, ceiling +1 |
| Pitch movement | +1, with repeated rise-fall on the same phrase |
| Volume | +1, then drop on the last word |
| Articulation | 0 to +1, endings start to blur at the peak |
| Sentence length | -1, with one run-on that does not resolve |
| Interjections | +2 (the state with the highest tick rate) |
| Laugh | one dry beat, usually self-directed |
| Self-interruption | +2 (restarts, "no wait", abandoned clauses) |

Physical correlates: audible exhale through the nose; a repeated phrase said twice because the first attempt did not land; tempo that starts fast and stalls; the sentence that begins as an answer and turns into a complaint.

Failure modes: whining (rising pitch on every clause) makes the host weak rather than frustrated; constant sighing turns it into tired; a frustration that never resolves across a segment reads as a stuck loop rather than a state.

### Tired

| Lever | Direction and magnitude |
|---|---|
| Pace | -2 (about -20 percent) |
| Pause length | +3, unfilled and mid-clause |
| Pitch register | 0, ceiling -2, range narrows |
| Pitch movement | -2, flattening toward monotone |
| Volume | -2 |
| Articulation | -2 (endings drop, consonants soften) |
| Sentence length | +1 at the start, then -2 as sentences are abandoned |
| Interjections | +1 (fillers replace content words) |
| Laugh | -1, breathy and late |
| Self-interruption | +1, but the repairs are abandoned mid-repair |

Physical correlates: breath audible before speech because support is low; vocal fry at sentence ends; a swallowed consonant at the start of a turn; the last word of a sentence trailing below the register floor.

Failure modes: slurring every word makes the host drunk, not tired; a monotone with no pitch movement at all reads as a broken synthesiser; tiredness that never lifts across an episode reads as a bad performance rather than a state. Ceiling: one segment at full tired, then a partial recovery beat.

### Intense

| Lever | Direction and magnitude |
|---|---|
| Pace | +1, with fewer pauses rather than faster words |
| Pause length | -2 |
| Pitch register | 0, ceiling +1 |
| Pitch movement | -1 (less melodic, more driven) |
| Volume | +1, steady rather than varying |
| Articulation | +2 (every consonant lands) |
| Sentence length | -1, short and declarative |
| Interjections | -2 (near zero, the state with the fewest ticks) |
| Laugh | zero |
| Self-interruption | -2 (no repairs, no hedging) |

Physical correlates: breath taken at clause boundaries only; a slight forward lean audible as closer mic proximity; stress on the verb rather than the noun; no rising terminals, so the listener gets no invitation to respond.

Failure modes: intensity played as volume becomes shouting; intensity with no pauses becomes a wall of sound; a host who is intense about everything has no baseline left to return to. Ceiling: two consecutive segments, then a break.

### Curious

| Lever | Direction and magnitude |
|---|---|
| Pace | +1 on the question, 0 on the answer |
| Pause length | -1 before the question, +1 after it (the interested pause) |
| Pitch register | 0, ceiling +1 on question endings |
| Pitch movement | +2, rising terminals on genuine questions |
| Volume | 0 |
| Articulation | +1 |
| Sentence length | -1 for questions, +1 for the follow-up |
| Interjections | +1 ("oh", "hmm", "right") |
| Laugh | 0 to +1, light |
| Self-interruption | +1 (the follow-up arrives before the first question finishes) |

Physical correlates: a quick inhale before the question; the pitch rise starting on the stressed word, not the last syllable; a short silence after the answer that is not a gap but attention; a follow-up that repeats one word from the answer.

Failure modes: every sentence rising turns curiosity into insecurity; question-stacking without listening reads as an interrogation; "interesting" as a response is a tell that the host is not curious at all.

### Happy

| Lever | Direction and magnitude |
|---|---|
| Pace | +1 to +2 |
| Pause length | -1 |
| Pitch register | 0, ceiling +2, floor +1 (the whole voice lifts) |
| Pitch movement | +3 (widest range of any state) |
| Volume | +1 |
| Articulation | +1, brighter rather than harder |
| Sentence length | -1 |
| Interjections | +2 |
| Laugh | +3, and laughter may interrupt a word |
| Self-interruption | +1, of the delighted kind |

Physical correlates: smile audible as a change in vowel colour (fronted, wider); breath released rather than held; laughter placed on the stressed syllable; the pitch peak arriving late and high.

Failure modes: constant high pitch with no rests reads as manic; laughter on every line is a laugh track; happiness with no dynamic variation reads as a continuity announcer rather than a person.

## What the emotion table will not do

It will not make a persona sound angry. It makes a persona sound like itself while angry. That distinction is the whole design: the levers are deltas on a baseline, so the fingerprint survives the state. A profile that sounds like a different person when angry has failed, even if the anger reads well.
