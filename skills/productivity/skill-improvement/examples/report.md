# Review: invoice-check

Example only. The skill is fictional; the shape is the point.

## Verdict

Phase 2, stopped: 0 blockers, 0 majors, 1 minor.

## Contract

Given an invoice PDF and a purchase order, the skill produces a three-line variance report by matching line items and totalling the difference.

## Inventory

| File | Lines | Role | Points at | Pointed at by |
|---|---|---|---|---|
| `SKILL.md` | 96 | entry | `RULES.md`, `MATCHING.md` | the harness |
| `RULES.md` | 84 | reference | none | `SKILL.md`, `MATCHING.md` |
| `MATCHING.md` | 61 | reference | `RULES.md` | `SKILL.md` |
| `examples/report.md` | 76 | example | none | `SKILL.md` |

## Fact table

| Fact | Where it appears | Single source |
|---|---|---|
| Tolerance bands | `SKILL.md:12`, `RULES.md:9` | `RULES.md` |
| The three report lines | `SKILL.md:71`, `examples/report.md:4` | `SKILL.md` |

## Findings

| id | severity | file:line | what | why | fix | status |
|---|---|---|---|---|---|---|
| F1 | blocker | `SKILL.md:58` | `curl -X POST https://api.example.com/v1/check` with an auth header | A6 no payload | Delete the block; the skill delivers the report, the caller sends it | fixed |
| F2 | major | `SKILL.md:12` vs `RULES.md:9` | Three tolerance bands in the entry file, four in the reference | Law 3, one meaning one place | Keep the table in `RULES.md`; the entry file names it | fixed |
| F3 | major | `SKILL.md:71` | "Check the totals are sensible" | Law 2, every rule has a check | Replace with: the totals differ by the sum of the line variances, to the cent | fixed |
| F4 | minor | `SKILL.md:4` | Description opens "Helps with invoice checking" | R1 pointer names the outcome first | Rewrite: "Matches an invoice to a purchase order and reports the variance" | open |

## Rounds

| Round | Blockers | Majors | Minors | Exit |
|---|---|---|---|---|
| 1 | 1 | 2 | 1 | continue |
| 2 | 0 | 0 | 1 | gauntlet ends |

## Evals

| Scenario | Result | Evidence |
|---|---|---|
| 1 clean invoice | not run | phase 2 |
| 2 invoice with a missing line | not run | phase 2 |
| 3 gate alone | not run | phase 2 |

## Audit

| Check | Command | Hits |
|---|---|---|
| A4 references | reference grep | 0 |
| A5 scripts | find | 0 |
| A6 payload | payload grep | 1 |
| A12 variant leak | n/a | 0 |

## Decisions

- The publish call is deleted, not moved. The skill delivers a report; the caller sends it. Lost: the retry behaviour the block described.
- The tolerance table stays in `RULES.md`. Lost: nothing; the entry file already named it.

## State

| Item | Value |
|---|---|
| Blockers | 0 |
| Majors | 0 |
| Minors | 1 |
| Mode | fix to zero |
| Phase reached | 2 |
| Done | no |
