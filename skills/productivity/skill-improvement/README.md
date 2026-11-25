# Skill Improvement

## What
Reviews an existing agent skill and takes it to a fixed bar: contract, executability, numbered gate, and eval suite. Three modes: review (report only), fix to zero (edit in place), or build evals (suite from scratch).

## Why Use It
When you need to ensure a skill is production-ready with no contradictions, clear gates, and verified test scenarios. Improves reliability without rewriting from scratch.

## How (Brief)

Invoke as a skill: `/skill-improvement`. Tell it your mode and target folder. Example:

```
/skill-improvement review path/to/skill/
# or /skill-improvement fix-to-zero to edit the skill in place
```

## Modes

| Mode | Phases | Target Edited? | Deliverable |
|---|---|---|---|
| **Review** | 1, 5 | No | Report only |
| **Fix to zero** | All five | Yes | Edited skill + report |
| **Build evals** | 1, 4, 5 | No | Eval suite + report |

## Where Things Go

| Artifact | Path |
|---|---|
| The gate | `<skill>/GATE.md` or section in entry file |
| The report | `reviews/<skill>.md` relative to working root |
| The evals | `evals/<skill path>/` mirroring skill's own path |
| A run | `evals/<skill path>/runs/<run>/<scenario>/` |

## Phases

| Phase | Question | Exit |
|---|---|---|
| **1 Survey** | What does it promise? | Contract sentence, complete inventory, fact table with repeated facts |
| **2 Gauntlet** | Does it run, read, and audit clean? | Zero blockers, zero majors |
| **3 Gate** | Can it check itself? | Numbered checks in GATE.md, every step mapped |
| **4 Evals** | Does a real run pass? | Three scenarios, fixtures, recorded runs |
| **5 Prove** | Is it done? | Audit zero, lens pass, dry run asking no question, report |

Stop after any phase; the report records where you stopped.

## Severity Levels

| Severity | Means | Examples |
|---|---|---|
| **Blocker** | Skill cannot be run or does harm | Step with no input; leaked secret; destructive action without confirmation |
| **Major** | Two parts disagree or promise has no rule | Enum drift; rule with no check; broken reference; eval that cannot run |
| **Minor** | Runs but reads badly | Duplication; stale count; two names for one thing |

Blockers and majors reach zero before next round. Minors batch into one pass.

## The Gauntlet

Four reviewers per round in parallel, each in fresh context:

- **Runs** — walks skill as fresh agent; every step needs input, action, completion criterion
- **Reads** — applies checks R1-R9 from CRAFT.md: pointer, two loads, hierarchy, completion criteria, pruning
- **Voice** — applies checks R10-R14 from CRAFT.md: stale lines, no-ops, positive phrasing, example values, leading words
- **Audit** — runs AUDIT.md; mechanical checks use file/search tools first

A round returns findings; you fix them; next round starts clean. Loop exits when zero blockers and majors remain. A cap reached without clean round ends it too, then one lens pass runs with doctrine the four reviewers do not share.

## The Laws

Ten laws each naming a check in AUDIT.md:

1. Placement is the mechanism — what skill must not see lives outside its folder
2. Every rule has a check; every check names a step
3. One meaning, one place
4. State the loss — every transform records what it drops
5. Recompute every number — counts come from artifact, never memory
6. Delete before you add
7. Fix file that should have prevented it
8. Say target, not ban
9. A claim names its proof
10. The target proves itself

## Done When

- name is lowercase kebab-case and matches folder
- description states outcome and modes a person can pick
- SKILL.md under 500 lines
- Every step has input, action, completion criterion
- Every rule has numbered check; every check names a step
- One meaning has one home
- Every external target has variant file with capability table
- Skill delivers text and instructions only
- Evals live outside skill, mirror path, hold three scenarios with fixtures and recorded runs
- Audit returns zero
- Lens pass recorded with lens named
- Dry run finishes: fresh agent runs skill on input and asks no question

## Files

| File | Purpose |
|---|---|
| `SKILL.md` | Full workflow, modes, phases, laws |
| `GATE.md` | Checks for the skill itself |
| `SURVEY.md` | Phase 1: contract extraction and fact inventory |
| `GAUNTLET.md` | Phase 2: execution and readability checks |
| `EVALS.md` | Phase 4: eval design and regression list |
| `REPORT.md` | Phase 5: completion criteria and audit |
| `CRAFT.md` | Writing doctrine for skills (Matt Pocock's writing-for-agents) |
| `AUDIT.md` | Mechanical checks for the skill text |

## Attribution

Original concept by Marcubus. This implementation provides a structured skill improvement loop with adversarial gauntlet rounds and automated quality gates.
