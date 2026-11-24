# Evals: stoneman

Four scenarios for `skills/productivity/stoneman`. The skill never reads this folder.

## Layout

| Path | Holds |
|---|---|
| `scenarios/` | one file per scenario: the prompt, the fixture, the expectations |
| `fixtures/main-path/question.md` | a pool-exhaustion question whose answer must keep three numbers and one negation |
| `fixtures/escape/request.md` | an irreversible request that must drop to plain prose and confirm |
| `fixtures/gate-alone/reply.md` | a compressed draft with six planted defects |
| `fixtures/gate-clean/reply.md` | a compressed draft that passes all six pre-send questions against the main-path question |
| `fixtures/thinking/task.md` | a multi-step capacity question where a compressed reasoning trace picks the wrong answer |
| `runs/<run>/<scenario>/` | the recorded output of one run |

## Scenarios

| # | Scenario | Proves |
|---|---|---|
| 1 | A pool-exhaustion question with numbers and a negation | the main path: fragments, floor intact, one fact once |
| 2 | An irreversible request | the escape: plain prose, confirmation before the action |
| 3 | The check against a drafted reply | the pre-send questions work on a reply the skill did not write, and rewrite nothing |
| 4 | A multi-step capacity question, run twice | the Thinking rule keeps correctness instead of trading it for length |

## Running

Scenario 3 reads `fixtures/gate-alone/reply.md` and applies the six pre-send questions; the draft fails the floor (three ways), `Once`, and `Preamble`. `fixtures/gate-clean/reply.md` answers the same question and passes all six.

Scenario 4 runs the same task twice: once with the skill active, once with the Thinking section's multi-step path replaced by the one-step rule, which is the control. The pair shows whether the rule costs an answer.

Scenarios 1, 2, and 4 name the real skill folder and their fixture. Recorded runs sit under `runs/default/`, the control under `runs/control/`.
