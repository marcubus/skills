# Review: invoice-check

Example only. The skill is fictional; the shape is the point.

## Verdict

Phase 2, stopped: 1 blocker, 2 majors, 1 minor.

## Contract

Given an invoice PDF and a purchase order, the skill produces a three-line variance report by matching line items and totalling the difference.

## Inventory

| File | Lines | Role | Points at |
|---|---|---|---|
| `SKILL.md` | 96 | entry | `RULES.md`, `MATCHING.md` |
| `RULES.md` | 84 | reference | none |
| `MATCHING.md` | 61 | reference | `RULES.md` |
| `examples/report.md` | 22 | example | none |

## Findings

| id | severity | file:line | what | why | fix |
|---|---|---|---|---|---|
| F1 | blocker | `SKILL.md:58` | `curl -X POST https://api.example.com/v1/check` with an auth header | A6 no payload | Delete the block; the skill delivers the report, the caller sends it |
| F2 | major | `SKILL.md:12` vs `RULES.md:9` | Three tolerance bands in the entry file, four in the reference | Law 3, one meaning one place | Keep the table in `RULES.md`; the entry file names it |
| F3 | major | `SKILL.md:71` | "Check the totals are sensible" | Law 2, every rule has a check | Replace with: the totals differ by the sum of the line variances, to the cent |
| F4 | minor | `SKILL.md:4` | Description opens "Helps with invoice checking" | R1 pointer names the outcome first | Rewrite: "Matches an invoice to a purchase order and reports the variance" |

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

## State

| Item | Value |
|---|---|
| Blockers | 0 |
| Majors | 0 |
| Minors | 1 |
| Phase reached | 2 |
| Done | no |
