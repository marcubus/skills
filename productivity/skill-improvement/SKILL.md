---
name: skill-improvement
description: Reviews an existing agent skill and takes it to a fixed bar: contract, executability, contradiction, boundary, compression, a numbered gate, and an eval suite. Use when a skill needs a review, a gauntlet, a release gate, or evals before it ships.
disable-model-invocation: true
---

# Skill improvement

A skill is a procedure a model runs without you. Improve it by proving three things: it can be run, it cannot contradict itself, and it earns its length. Everything else is bookkeeping.

This skill reviews a skill that already exists. For a skill that does not, write a draft first and come back.

## Precondition

The target is a folder containing `SKILL.md`. Read it, and every file it points at, before judging anything.

## Phases

| Phase | Question | Exit |
|---|---|---|
| 1 Survey | What does it promise? | One contract sentence, an inventory, and a fact table |
| 2 Gauntlet | Does it run, read, and audit clean? | Zero blockers, zero majors |
| 3 Gate | Can it check itself? | Numbered checks, every step mapped |
| 4 Evals | Does a real run pass? | Three scenarios, fixtures, recorded runs |
| 5 Prove | Is it done? | Audit zero, dry run, report |

Stop after any phase. The report records where you stopped, so a survey is a complete deliverable.

Read `SURVEY.md` at phase 1, `GAUNTLET.md` at phase 2, `GATE.md` at phase 3, `EVALS.md` at phase 4, and `REPORT.md` at phase 5. Read `CRAFT.md` before the Reads review and `AUDIT.md` before any audit. Read `VARIANTS.md` when the skill has more than one external target. When you need the shape of a report, a gate, or an eval README, read `examples/report.md`, `examples/gate.md`, and `examples/eval-readme.md`.

## The gauntlet

Three reviewers per round, in parallel, each in a fresh context. Re-read from disk: the reviewer who wrote the fix is not the reviewer who checks it.

- **Runs** walks the skill as a fresh agent. Every step needs an input, an action, and a completion criterion. Every promise needs a rule. Every rule needs a check.
- **Reads** applies `CRAFT.md`: pointers, loads, hierarchy, completion criteria, leading words, pruning.
- **Audit** runs `AUDIT.md`. Mechanical, no judgement.

A round returns findings, you fix them, the next round starts clean. The loop exits when a round returns zero blockers and zero majors. A round of only minors ends it.

## Severity

| Severity | Means | Examples |
|---|---|---|
| Blocker | The skill cannot be run, or it does harm | a step with no input; a leaked secret; a destructive action with no confirmation |
| Major | Two parts disagree, or a promise has no rule | enum drift; a rule with no check; a broken reference; an eval that cannot run |
| Minor | It runs, but it reads badly | duplication; a stale count; two names for one thing |

Blockers and majors reach zero before the next round. Minors batch into one pass.

## The laws

Each law names its check in `AUDIT.md`. Five are mechanical; three need a read, and the law map says which.

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
- `description` states the outcome and the branches that trigger it.
- `SKILL.md` is under 500 lines.
- Every step has an input, an action, and a completion criterion.
- Every rule has a numbered check, and every check names a step.
- One meaning has one home.
- Every external target has a variant file with a capability table.
- No script, payload, endpoint, key, or response field lives in the skill.
- Evals live outside the skill, mirror the skill path, and hold three scenarios, their fixtures, and one recorded run each.
- The audit returns zero.
- A fresh agent can run the skill start to finish without asking a question.

## Report

Write `reviews/<skill>.md` outside every skill folder, from `REPORT.md`. State the phase you stopped at.

## Lineage

The loop is the gauntlet: repeated adversarial rounds, each gated on severity. The writing doctrine is Matt Pocock's `writing-for-agents`, summarised in `CRAFT.md`. The review split — judgement on two axes, mechanics kept separate — is the shape used by `code-review`.
