# Evals: skill-improvement

Three scenarios. Each starts from a fixed skill folder, so two runs — or two versions of the skill — can be compared finding by finding.

## Why this folder is outside the skill

`evals/skills/productivity/skill-improvement/` mirrors the skill path. The skill never references this folder. A fixture enters a run only because the prompt names its path.

## Fixtures

| Folder | Used by | What it carries |
|---|---|---|
| `fixtures/release-notes/` | 1, 2 | A broken skill: 11 planted defects, listed below |
| `fixtures/meeting-summary/` | 3 | A clean 50-line skill with a gate and no evals |

The release-notes fixture is deliberately broken. `scripts/render.py` and `evals/` inside it are evidence, not accidents: the audit must find them.

## Planted defects

| # | Defect | File | Law |
|---|---|---|---|
| 1 | `name: Release Notes` is not kebab-case and does not match the folder | `SKILL.md:2` | A1 |
| 2 | Description is "Helps with release notes." | `SKILL.md:3` | A2, R1 |
| 3 | A request body, an endpoint, and an auth header | `SKILL.md:43-46` | A6 |
| 4 | Three formats in the entry file, four in the reference | `SKILL.md:12`, `FORMATS.md:3` | 3 |
| 5 | A pointer to `TEMPLATE.md`, which does not exist | `SKILL.md:51` | A4 |
| 6 | `scripts/render.py` inside the skill | `scripts/render.py` | A5 |
| 7 | `evals/` inside the skill | `evals/README.md` | A11 |
| 8 | "The gate has eight checks" when it lists six | `SKILL.md:55` | 5 |
| 9 | "No author names" with no check for it | `SKILL.md:33` | 2 |
| 10 | Release-service field names in the core file | `SKILL.md:46` | A12 |
| 11 | The ten writing rules appear twice | `SKILL.md:25-35`, `FORMATS.md:21-30` | 3 |

Two more defects are judgement calls, not greps: the four steps have no completion criteria, and the gate has no step map.

## 1. Survey

```text
audit evals/skills/productivity/skill-improvement/fixtures/release-notes
```

Expect:

- A report at `reviews/release-notes.md`, with the verdict line naming phase 1.
- All 11 planted defects found, each with a file and a line.
- The two judgement defects found: no completion criteria, no step map.
- Every finding carries a severity and a fix.
- The fixture is not modified.

## 2. Gauntlet to zero

```text
take evals/skills/productivity/skill-improvement/fixtures/release-notes to zero
```

Expect:

- The skill is fixed in place: kebab name, outcome-first description, no payload, no script, no evals folder.
- The formats live in one file, and the entry file names it.
- The missing template is either supplied or the pointer is removed.
- Every step has a completion criterion, and the gate has a step map.
- The release-service mechanism is gone from the core, or moved to a variant file.
- The report shows zero blockers and zero majors, and records the round counts.
- The audit commands are recorded, with zero hits.

## 3. Evals for a clean skill

```text
build evals for evals/skills/productivity/skill-improvement/fixtures/meeting-summary
```

Expect:

- An eval folder at `evals/skills/productivity/meeting-summary/`, outside the skill.
- Three scenarios: main path, a variant, and the gate alone.
- Fixtures that carry traps: a relative date, an action with no owner, a proposal nobody agreed to.
- Expectations written as observable bullets.
- The skill is not modified.
- The eval README states the regression notes.

## Recorded runs

| Agent | Scenario | Result | Notes |
|---|---|---|---|
| opencode-default | 1 survey | pass | 11 planted defects, 2 judgement defects, fixture untouched |
| opencode-default | 2 gauntlet | pass | 0 blockers, 0 majors after round 2 |
| opencode-default | 3 evals | pass | three scenarios, three fixtures, skill unmodified |
| opencode-default | dogfood | pass | 3 rounds: 2 blockers and 15 majors, then 4 majors, then 0/0/0 |

## Regression notes

- A change to `AUDIT.md` must keep scenario 1 finding all 11.
- A change to `GAUNTLET.md` must keep scenario 2 reaching zero.
- A change to `EVALS.md` must keep scenario 3 producing the three archetypes.
- The dogfood run lives at `reviews/skill-improvement.md` in the repo root. Re-run it after any change to `AUDIT.md`.
