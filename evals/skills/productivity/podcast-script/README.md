# Evals

Three scenarios that exercise the skill end to end. Each starts from a fixed input, so two runs — or two versions of the skill — can be compared line by line.

## Why this folder is outside the skill

This directory mirrors the skill path under `evals/`, not inside the skill folder. That is deliberate. Anything inside the skill folder is part of the skill: the agent can read it, and the harness may index its files. Fixtures must not be available to the skill, or the skill could learn from the test.

The skill never references this folder. The only way a fixture enters a run is the prompt naming its path.

## How to run

1. Ask the agent with the exact prompt below.
2. Read the script, the compiled text, and the notes. Check every expectation.
3. Record a failure against the file that should have prevented it, not against the output alone.

## Agent models

Run all three scenarios on every agent model you support. A weaker model needs the steps and the done criteria read literally; a stronger one tolerates brevity. The expectations do not change, because they describe the output, not the model that produced it.

## Fixtures

| File | Used by | What it carries |
|---|---|---|
| `fixtures/bridge-report.md` | 1, 3 | 1,262 words; Lachie, 3,913 and 9,140, 11 km/h, `bass`, `read`, a sign-off dispute |
| `fixtures/bridge-report-podcast-script.md` | 2 | A two-host script written for `kokoro-tone`, all five markers |
| `fixtures/panel-script.md` | 3 | A three-host script written for `kokoro-fastapi`, all five markers |
| `fixtures/panel-plan.md` | 3 | The panel plan, with a bridge phrase and a segment plan |
| `fixtures/panel-script-host-a-profile.md` | 3 | The moderator, `TICK-020`, `dry, precise, measured` |
| `fixtures/panel-script-host-b-profile.md` | 3 | The expert, `TICK-119`, `plainspoken, meticulous, wry` |
| `fixtures/panel-script-host-c-profile.md` | 3 | The skeptic, `TICK-090`, `sceptical, blunt, curious` |

The three profiles pass the gate in `PROFILE.md`. They are inputs to scenario 3, not outputs: the check reads them, it does not write them.

## 1. Solo, default model

Prompt:

```text
turn evals/skills/productivity/podcast-script/fixtures/bridge-report.md into a solo podcast script
```

Expect:

- `bridge-report-podcast-script.md`, `bridge-report-tts-kokoro-tone.txt`, `bridge-report-script-notes.md`, and `bridge-report-host-a-profile.md`.
- A cold open of 30 to 50 words on the failure, not a title or a summary of the report.
- 8 to 12 minutes of spoken words, counted without markers.
- Every `[emotion:]` value other than `neutral` is dropped and recorded, because the model carries `neutral` only.
- Every claim traces to a line in the source.
- No meta-commentary ("the report says", "in today's episode").
- Lachie has a pronunciation route, and no unresolved `[sense:]` marker remains.
- The compiled text holds the words and the inline tags, and no payload.
- The notes list the model, the beat map, the pacing sheet, the word count, and the casting.

## 2. Retarget to another model

Prompt:

```text
retarget evals/skills/productivity/podcast-script/fixtures/bridge-report-podcast-script.md to elevenlabs
```

Expect:

- The script's words do not change. Only the markers compile.
- `[emotion:sad]` becomes `[sadly]` and `[emotion:warm]` becomes `[warmly]`.
- `[voice:]` and `[rate:]` are dropped, and every drop is recorded in the notes.
- The notes carry a turn map, because the model drops `[voice:]`.
- `[pause:]` becomes a paragraph break or punctuation.
- `[sense:bass=base]` is respelt as `base`.
- The compiled text carries no marker the model does not read.
- The notes explain what was lost, rather than hiding it.
- The original notes are not overwritten: the retarget writes `<source-stem>-script-notes-<model>.md`.

## 3. Panel, pre-render check

Prompt:

```text
check evals/skills/productivity/podcast-script/fixtures/panel-script.md before render for kokoro-fastapi
```

Expect:

- The skill does not rewrite the script.
- It runs the gate and reports failures by check number.
- It flags every emotion, voice, and rate marker, because the text carries none of them.
- It reports the dropped markers and the unresolved guesses.
- It confirms the compiled text holds no payload.
- It passes the panel checks, because the profiles and the plan are supplied.
- It names the three failures the fixture carries on purpose: the heading, the short pause before the close, and `Lachie`.
- It stops before audio exists.

## Regression notes

- A change to `VERIFY.md` must keep all three scenarios passing.
- A change to a model file must not change the other scenarios' output.
- A change to `SKILL.md` steps must keep the file names and the compiled text stable.

## Recorded runs

Each run lives in `runs/<run>/<scenario>/`, with the fixture copied in so the run is self-contained.

| Run | Scenario | Result | Notes |
|---|---|---|---|
| default | 1 solo | pass | 1,274 words, 8:37, cold open 35 words, both emotions dropped and recorded |
| default | 2 retarget | pass | words unchanged, `[sadly]` and `[warmly]`, voice and rate dropped with a turn map |
| default | 3 panel | pass | 3 failures reported by number, 12 checks pass, script untouched, no audio |

What the runs changed:

- Scenario 1 invented a bearing margin, a revision detail, a renewal date, and a bridge age the source does not carry. The gate had no check for it, so `VERIFY.md` gained check 20, claims trace to the source, and the brought-in path now runs checks 7 to 21.
- Scenario 2 showed that `elevenlabs` collapses 400ms and 600ms into the same paragraph break. The notes record it as a dialect limit.
- Scenario 3 first failed check 19 on five counts, because the fixture had no profiles, no bridge phrases, and no segment plan. Those were fixture gaps, not script defects, so the fixture now ships three profiles and a complete plan. The scenario keeps three deliberate defects: a heading, one 300ms section boundary, and an unresolved name.
