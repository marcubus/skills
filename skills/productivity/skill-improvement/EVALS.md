# Evals

Phase 4. An eval proves the skill works on a fixed input. It lives outside the skill.

## Contents

- Placement
- Mirroring
- Three scenarios
- Fixtures
- Expectations
- Runs
- Regression
- When an eval fails

## Placement

Evals sit outside every skill folder, because a skill can read its own folder. The skill never sees the test, and never references it. This is law 1.

The only way a fixture enters a run is the prompt naming its path.

## Mirroring

Mirror whatever path the skill has: `skills/productivity/<skill>/` maps to `evals/skills/productivity/<skill>/`. The rule is `evals/` plus the skill's own path, so a skill under any other folder keeps the same shape.

## Three scenarios

| # | Scenario | Proves |
|---|---|---|
| 1 | The main path | The skill produces its deliverable from a realistic input |
| 2 | A second branch | The same skill through a second target, a second mode, or a hostile input |
| 3 | The gate alone | The skill checks work it did not produce, and does not rewrite it |

Scenario 2 is a branch, not necessarily a variant. A skill with one target still has a branch: an edge case, a malformed input, or a mode the main path never reaches. When no branch exists, the skill has one path and scenario 2 is a second input on it.

Three is the floor. Add a scenario when a new branch appears in the skill.

## Fixtures

- Frozen: a fixture never changes to make a run pass.
- Traps: a fixture carries the exact cases the skill must handle. A name that needs a route, a number that must not be invented, a rule that must fire.
- Self-contained: copy the fixture into the run folder, so the run can be re-read later.
- Named by the skill's own convention. A fixture carries a variant suffix only when the deliverable does.

## Expectations

Write expectations as observable bullets. "A cold open of 30 to 50 words", not "a strong opening".

Each bullet names the file it applies to.

## Runs

```text
runs/<run>/<scenario>/
```

One folder per agent per scenario, holding the fixture, the outputs, and any report. A second agent model gets its own folder, because the expectations describe the output, not the model.

## Regression

Run the regression list at phase 5, before the report:

- A change to the gate keeps every scenario passing.
- A change to a variant file changes only that scenario.
- A change to the entry file keeps the file names and the deliverables stable.

## When an eval fails

Fix the file that should have prevented the failure. A wrong output is a symptom; a missing rule or a missing check is the cause. This is law 7.

Then add the check that would have caught it, and record the addition in the report. The suite gets stronger every time it fails.
