# Voice craft: word choice

Four fields decide what a persona says: `lexical_register`, `exemplar_lines`, `calibration_line`, `pronunciation_lexicon`.

The fingerprint stops two hosts sounding alike. These four stop two hosts writing alike. A profile with a distinct fingerprint and no lexical register yields scripts that read as one narrator in different costumes, which is the fault listeners notice before any acoustic detail.

All four describe the persona at rest. They do not move with `eiq`, with a cued state, or with a co-host's mood. A persona that gets wittier when regulated has had its personality moved by a number.

## Contents

- lexical_register
- exemplar_lines
- calibration_line
- pronunciation_lexicon
- How a transcript skill uses these four
- What these fields do not do

## lexical_register

Eight values, no prose. This is the field a script writer reads first, and the field that decides whether two personas with different accents still argue the same way.

```yaml
lexical_register:
  contractions: always
  openers: ["Look,", "The thing is,", "Right."]
  hedges: none
  assertion: states
  jargon_policy: explain
  address_cohost: "Harriet"
  address_listener: "you"
  banned_words: [utilise, journey, space]
```

| Sub-field | Values | What it controls |
|---|---|---|
| contractions | always, sometimes, never | how spoken the syntax is. `never` reads as written prose performed aloud, useful only where formality is the character. |
| openers | 3 to 5 strings, 1 to 4 words each | the sentence openings the persona reuses. Cheapest strong tell in the file. |
| hedges | none, soft, heavy | `none` gives bare assertion ("that's wrong"). `soft` gives "I think", "probably". `heavy` stacks qualifiers. |
| assertion | states, qualifies, asks | the default sentence mode. `states` is declarative, `qualifies` adds a condition, `asks` turns claims into questions. |
| jargon_policy | explain, assume, avoid | `explain` defines a term in plain words on first use, `assume` uses it and moves on, `avoid` describes the thing instead of naming it. |
| address_cohost | first name, surname, nickname, you, none | how the persona speaks to the other host, written as the literal it uses. |
| address_listener | you, you lot, everyone, listeners, none | the second-person form for the audience. |
| banned_words | 0 to 10 words | words this persona never says. |

### Lexical contradiction rules

L1. `assertion: states` takes `hedges: none`. `qualifies` takes `soft` or `heavy`. `asks` takes any. States with heavy hedging is a contradiction and fails the check.
L2. `banned_words` may not contain a describing word, a tick literal, the field name, or an entry from `pronunciation_lexicon`.
L3. `jargon_policy: avoid` is legal in a technical field only when `banned_words` names the terms being avoided. Otherwise the persona cannot discuss its own subject.
L4. `address_cohost` is `none` only for a single-host show. A two-hander whose hosts never use each other's names is not a relationship.
L5. Openers may not repeat across two stored personas in the same show. One host who opens with "Look," and another who opens with "Look," are the same person on the page.
L6. Openers must be literal strings a synthesiser can read, with no markup and no brackets.

### Failure mode

A register written as adjectives ("formal but warm, dry but generous") instead of these nine values. If a sub-field needs a sentence to explain it, the detail belongs in `exemplar_lines`. Adjectives in a field are unfalsifiable, and an unfalsifiable field is not a constraint.

## exemplar_lines

Four lines of the persona at baseline, and three lines the persona would never say. This is the field an LLM writer imitates best, because it constrains syntax rather than describing it. A voice note constrains adjectives. An exemplar constrains grammar.

```yaml
exemplar_lines:
  claim: "The bridge was signed off on a model that assumed nobody would ever walk on it."
  question: "Who signed the drawing, and did they read the second page?"
  disagreement: "I don't think that holds. The load case changes once the market moves in."
  laugh: "Heh. Right. And the staircase is still there."
  never_says: ["That's a really great point.", "Let's unpack that.", "Absolutely, one hundred percent."]
```

E1. Each of the four lines is 8 to 30 words, in the baseline state, with no strained-emotion vocabulary. A baseline exemplar that is already angry gives the writer nowhere to go.
E2. At most one tick per line. The point of the line is syntax, not decoration.
E3. The laugh line writes the laugh as a sound in the persona's own shape ("heh", "hah", a wheeze), never the word laugh and never a description of laughing.
E4. `never_says` holds exactly three lines of 4 to 20 words, each plausible in this field and wrong for this persona: the wrong register, the wrong stance, or the wrong vocabulary. Not nonsense, not offensive, not a strawman.
E5. No real person is named and no line quotes a real person.
E6. The disagreement line matches `assertion`: a `states` persona disagrees flatly, a `qualifies` persona disagrees with a condition, an `asks` persona disagrees by questioning the claim.
E7. No unresolved acronym appears in any line. Write the spoken form.

Why the negative lines earn their place: a prohibition is cheaper to check than a description. A writer who can see the wrong answer rarely produces it, and a reviewer can test a draft against three strings instead of against a paragraph of intent.

## calibration_line

One sentence, 18 to 26 words, that carries the whole fingerprint. It is the casting test, the drift test and the cheapest quality instrument in the file.

```yaml
calibration_line: >
  Blimey, the second staircase is the one that tells you whether anybody read the drawings,
  and I have been saying that for eleven years.
```

K1. 18 to 26 words.
K2. Contains the signature interjection literal exactly once.
K3. Contains at least one opener from `lexical_register`.
K4. Baseline state, and the sentence ends on a stressed content word rather than trailing away.
K5. Takes 6 to 13 seconds at the declared pace: words divided by `pace_wpm_estimate`, times 60. A line outside that window is the wrong length for the persona's tempo.
K6. Frozen. The line is rendered at the start of each series and compared against the stored take. Editing it retires the comparison, so any edit bumps `version` and is noted in `provenance.accepted_matches` as "calibration line changed".

Use: a transcript skill renders the calibration line before the first episode, keeps the take, and compares each new series against it. Drift shows up as a change in the one sentence that was never supposed to change.

## pronunciation_lexicon

Zero to twelve `written` to `spoken` pairs. Handles the words this persona says differently from the default reading: names, products, units, numbers, loanwords, and the acronyms that appear in its field.

```yaml
pronunciation_lexicon:
  - {written: "GDP", spoken: "gee dee pee"}
  - {written: "2026", spoken: "twenty twenty-six"}
  - {written: "Loughborough", spoken: "luff bruh"}
```

P1. `spoken` is syllables in plain letters. Never letters separated by dots, hyphens or slashes, which a synthesiser either spells with wrong stress or stutters.
P2. `written` is 1 to 3 words and must appear in `exemplar_lines`, `voice_note` or `field_of_expertise`. A lexicon entry for a word the persona never says is decoration.
P3. No entry for a word the stack already reads correctly. An over-full lexicon is a script instruction wearing a persona's clothes.
P4. `spoken` may not contain markup, brackets, or a prosody instruction. Delivery belongs in the fingerprint and the states.
P5. Two personas may respell the same word differently. That is a legitimate difference in idiolect and it is not an axis of distinctness, so it never counts toward the distinctness gate.

## How a transcript skill uses these four

In order: `exemplar_lines` for rhythm, `lexical_register` for stance and vocabulary, `calibration_line` as the register check on the finished script, `pronunciation_lexicon` as a replacement pass before rendering. A script that reads correctly against the exemplars and takes 40 percent longer than the calibration line to say the same kind of sentence has drifted, even if every field still matches.

## What these fields do not do

They do not set accent, which is `vocal_fingerprint.vowel_colour` and `stress_pattern`. They do not set emotion, which is `emotion_behaviour`. They do not set pace, which is `pace_band` and the state deltas. And they are not axes of the distinctness gate: a lexical difference never substitutes for a phonetic one, because two hosts who write differently and sound identical are still one voice.
