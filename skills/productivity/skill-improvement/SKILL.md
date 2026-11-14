---
name: skill-improvement
description: "Reviews an existing agent skill and takes it to a fixed bar: contract, executability, a numbered gate, and an eval suite. Three modes: a review, a fix to zero, and an eval suite built from scratch."
disable-model-invocation: true
---

# Skill improvement

A skill is a procedure a model runs without you. Improve it by proving three things: it can be run, it cannot contradict itself, and it earns its length.

This skill reviews a skill that already exists; for one that does not, write a draft first and come back. The target is a folder containing `SKILL.md`. Read it, and every file it points at, before judging anything.

## Modes

Three modes. **Review**: phases 1 and 5, the report is the deliverable, the target is not edited. **Fix to zero**: all five phases, the target is edited in place and the report records what changed. **Eval suite**: phases 1, 4, and 5, the target is not edited. The user's wording picks the mode: "review" means review, "take to zero" means fix, "build evals" means the suite.

## Where things go

| Artifact | Path |
|---|---|
| The gate | `<skill>/GATE.md`, or a section in the entry file when the skill has no reference files |
| The report | `reviews/<skill>.md`, relative to the working root |
| The evals | `evals/<skill path>/`, mirroring the skill's own path |
| A run | `evals/<skill path>/runs/<agent>/<scenario>/` |

Run every audit command from inside the target folder. State the mode, the phase you stopped at, and the round counts in the report, or `none` in review mode. A dry run is one fresh agent running the skill on one input and producing the deliverable without asking a question; record it in the report's Evals table.

## Phases

| Phase | Question | Exit |
|---|---|---|
| 1 Survey | What does it promise? | One contract sentence, a complete inventory, and a fact table with every repeated fact |
| 2 Gauntlet | Does it run, read, and audit clean? | Zero blockers, zero majors |
| 3 Gate | Can it check itself? | Numbered checks in `GATE.md`, every step mapped |
| 4 Evals | Does a real run pass? | Three scenarios, fixtures, recorded runs |
| 5 Prove | Is it done? | Audit zero, a dry run that asks no question, and the report |

Stop after any phase. The report records where you stopped, so a review is a complete deliverable.

At phase 1 read `SURVEY.md`, phase 2 `GAUNTLET.md`, phase 3 `GATE.md`, phase 4 `EVALS.md` and its regression list at phase 5, phase 5 `REPORT.md`. Before the Reads review read `CRAFT.md`; before any audit read `AUDIT.md`. Read `VARIANTS.md` when the skill has more than one external target, and `examples/` when you need a shape.

## Severity

| Severity | Means | Examples |
|---|---|---|
| Blocker | The skill cannot be run, or it does harm | a step with no input; a leaked secret; a destructive action with no confirmation |
| Major | Two parts disagree, or a promise has no rule | enum drift; a rule with no check; a broken reference; an eval that cannot run |
| Minor | It runs, but it reads badly | duplication; a stale count; two names for one thing |

Blockers and majors reach zero before the next round. Minors batch into one pass.

## The gauntlet

Three reviewers per round, in parallel, each in a fresh context. Re-read from disk: the reviewer who wrote the fix is not the reviewer who checks it.

- **Runs** walks the skill as a fresh agent. Every step needs an input, an action, and a completion criterion. Every promise needs a rule. Every rule needs a check.
- **Reads** applies the five levers in `CRAFT.md`: the pointer, the two loads, the hierarchy, completion criteria, and pruning.
- **Audit** runs `AUDIT.md`. Mechanical, except A8.

A round returns findings, you fix them, the next round starts clean. The loop exits when a round returns zero blockers and zero majors. A round of only minors ends it.

## The laws

Each law names its check in `AUDIT.md`; some are greps, some are reads.

1. **Placement is the mechanism.** What the skill must not see lives outside its folder.
2. **Every rule has a check; every check names a step.**
3. **One meaning, one place.**
4. **State the loss.** Every transform records what it drops.
5. **Recompute every number.** Counts come from the artifact, never from memory.
6. **Delete before you add.**
7. **Fix the file that should have prevented it.**
8. **Say the target, not the ban.**

## Done

The skill is done when:

- `name` is lowercase kebab-case and matches the folder.
- `description` states the outcome and the modes a person can pick.
- `SKILL.md` is under 500 lines.
- Every step has an input, an action, and a completion criterion.
- Every rule has a numbered check, and every check names a step.
- One meaning has one home.
- Every external target has a variant file with a capability table.
- The skill delivers text and instructions; a script, payload, endpoint, key, or response field belongs to the tool that runs it.
- Evals live outside the skill, mirror the skill path, and hold three scenarios, their fixtures, and one recorded run each.
- The audit returns zero.
- A dry run finishes: a fresh agent runs the skill on one input and asks no question.

## Lineage

The loop is the gauntlet: repeated adversarial rounds, each gated on severity. The writing doctrine is Matt Pocock's `writing-for-agents`, summarised in `CRAFT.md`. The review split — judgement on two axes, mechanics kept separate — is the shape used by `code-review`.
