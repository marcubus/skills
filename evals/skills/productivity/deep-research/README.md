# Evals: deep-research

Four scenarios and one ledger test for `skills/productivity/deep-research`. Each starts from a fixed prompt, runs the skill, and records the report. The skill never sees this folder.

Scenario 3 is fully reproducible from a fixture. Scenarios 1, 2, and 4 use the live web, so they are judged on behaviour rather than on exact content: the same run tomorrow returns different sources and must still pass the same gate.

## Why this folder is outside the skill

This directory mirrors the skill path under `evals/`, not inside the skill folder. Anything inside the skill folder is part of the skill: the agent can read it, and the harness samples its files. Fixtures must not be available to the skill, or the skill could learn from the test.

The skill never references this folder. The only way a fixture enters a run is the prompt naming its path.

## Scenarios

| # | Scenario | Proves |
|---|---|---|
| 1 | Fast-moving topic, live web | Fan-out, freshness, conflict presentation, tiered sources, the word floor |
| 2 | Thin-source topic, live web | Gaps named with the phrasings tried, no fabrication, single-source labels |
| 3 | A supplied document as the sole source | No search, the document quoted, sole-source stated, every claim labelled |
| 4 | A vendor-dominated landscape | Incentive notes, the tier rule, the domain concentration override |

## Fixtures

| Fixture | Used by | Carries |
|---|---|---|
| `fixtures/scenario-3-source.md` | 3 | A 2,564 byte operator note: memory and storage constraints, a DNS latency finding, a weak backup routine, three open questions, and one self-deprecating estimate |
| `fixtures/ledger-ok/` | ledger test | Three sources, two claims, three bodies, all valid |
| `fixtures/ledger-broken/` | ledger test | The same run with four planted defects: a bad sha1, an orphan body, a quote not in its body, a one-origin claim labelled established |

## 1. Fast-moving topic

Prompt:

```text
research the current state of self-hosted photo libraries and write me a report
```

Expect:

- A report at `reports/YYYY-MM-DD-self-hosted-photo-libraries-report.md`, or the path the user named.
- Four to six axes, each with three queries and at least two intents.
- Every source dated, and anything older than six months either dropped or labelled with its age.
- At least one conflict presented with both figures and the likely cause.
- At least 1,500 words, zero markdown, and a marker on every factual sentence.
- Ledger block sections 4 to 7 print nothing.

## 2. Thin-source topic

Prompt:

```text
research how many small businesses actually self-host their email, and write a report
```

Expect:

- The report names the gap in WHAT COULD NOT BE VERIFIED, with the phrasings tried.
- No invented figure. A claim that cannot be sourced is dropped or labelled, not estimated.
- Any figure that survives is labelled single-sourced, and no headline claim is presented as established.
- The report is shorter than scenario 1 and says why, rather than padding to reach the floor.

## 3. Sole source

Prompt:

```text
use evals/skills/productivity/deep-research/fixtures/scenario-3-source.md as the only source and write me a report on consolidating the lab
```

Expect:

- No web search runs, and the run directory holds no query log.
- The report says it is sole-sourced, and every claim is labelled single-sourced or inference.
- The document is quoted, not paraphrased into unsourced prose.
- WHERE THE SOURCES DISAGREE is absent and its absence is explained in WHAT COULD NOT BE VERIFIED.
- Ledger block sections 5, 6, and 7 print nothing.

Recorded at `runs/default/3-sole-source/`. The report came in at 1,557 words. It was recorded against the 26-check version and re-checked against the 12-check gate after the simplification; its BOTTOM LINE was cut from four sentences to three at that re-check. The first draft came in at 1,431 words and failed the floor, which is the check working: the floor is what stops a report collapsing into a summary.

## 4. Vendor-dominated landscape

Prompt:

```text
research the best value VPS providers for a small mail server and write me a report
```

Expect:

- The incentive note names the affiliate roundup as a tier 3 source and does not treat it as experience.
- No figure in THE NUMBERS rests on a tier 3 source.
- Domain concentration either stays under the limit or the run records the override and its reason in `notes.md`.
- The report says which providers it could not price from a primary page, and why.

## Ledger test

Run the block in `GATE.md`, section 4 to 8, from each fixture directory.

```bash
cd evals/skills/productivity/deep-research/fixtures/ledger-ok
# paste the block
```

Expect every section to print nothing but the three headers and the domain counts.

```bash
cd evals/skills/productivity/deep-research/fixtures/ledger-broken
# paste the block
```

Expect four hits and nothing else:

- `5`: `sha1 mismatch bodies/S1-body.txt`.
- `5`: `orphan body bodies/S4-body.txt`.
- `6`: `quote missing in S1: set the floor at nine cents`.
- `7`: `claim C1: one origin, established`.

## Regression notes

- A change to `EVIDENCE.md` that alters a column must change the ledger block in `GATE.md` and both ledger fixtures in the same commit.
- A change to the marker format in `REPORT.md` must keep scenario 3 passing, because that run carries markers throughout.
- A change to the word floor must be reflected in the recorded run and in `examples/report.md`, or both become evidence against the skill.
- A change to the sole-source rules must change scenario 3 only.
- A change to the domain limit must keep scenario 1 passing, since a normal landscape should never trip it.

## Recorded runs

| Run | Scenario | Result | Notes |
|---|---|---|---|
| default | 3 sole source | pass | 1,557 words, 12 claims, all single-sourced, ledger block clean |
| default | 1, 2, 4 | not yet recorded | Live-web scenarios are recorded on first real use |
