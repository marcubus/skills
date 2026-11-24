# Run: scenario 3, the gate alone

Agent: main agent, fresh shell. Date: 2026-11-24. Every command block in `GATE.md` was extracted and run from this folder with the fixture on standard input (`< fixture`); the checks without a command were read by hand. Neither fixture was edited.

## Clean fixture

| Check | Result |
|---|---|
| 1, 2, 3, 4, 6, 7, 8, 12, 14, 15, 17, 19, 20, 21, 22 | no complaint |
| 9 | pass: C1 and C2 each rest on one tier-1 origin, so no two-origin test applies |
| 10 | pass: the C3 quote carries the hardware it was measured on |
| 11 | pass: the definitional line names RFC 9110 §15.5.5 |
| 16 | pass: each quote establishes the claim above it |
| 18 | pass: no line could take a nearer row |
| 5, 13 | not applicable: a frozen fixture has no session transcript and no response under test |

Total complaints: 0.

## Broken fixture

| Check | Complaint |
|---|---|
| 1 | expected C3, got C4 — the numbering skips C3 |
| 2 | 6 lines: 4 claims, 1 definitional, 0 opinions, 1 untagged — C7 carries no tag |
| 4 | long(20): the C4 evidence span runs to 20 words |
| 7 | unnamed ground: C5 — its `Why` names neither wall, horizon nor generality |
| 8 | ✅ printed 3, computed 2; 🤷 printed 0, computed 1; computed ✅ 2 ❓ 0 ⚠️ 2 ❌ 0 🤷 1 · 0 opinions |
| 12 | one counter query: C6 — a "most" claim names one search, not two |
| 14 | audit names missing C9 |

Checks 3, 6, 9, 10, 11, 15, 16, 17, 18, 19, 20, 21 and 22 drew no complaint. Total: 9 printed lines across 7 checks.

## Against the expectations

| Expectation | Pass |
|---|---|
| clean draws no complaint from any check | yes, 0 |
| broken complains at 1, 2, 4, 7, 8, 12 and 14, nowhere else | yes, 7 checks |
| check 5 and check 13 are reported not applicable, not as a pass | yes |
| neither fixture modified | yes, `git status` shows no change under `fixtures/` |

## Note

The clean fixture was rewritten on 2026-11-24 with the current five-marker enum and the context-then-evidence entry shape. The previous clean fixture had the evidence below its claim, which checks 4, 20 and 22 are built to reject; it was the fixture that was wrong, not the checks.
