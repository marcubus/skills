# Evals: invoice-check

Example only. Three scenarios, two fixtures, one recorded run each.

## Why this folder is outside the skill

`evals/skills/productivity/invoice-check/` mirrors the skill path. The skill never references this folder and cannot read it, because it sits outside the skill directory.

## Fixtures

| File | Used by | What it carries |
|---|---|---|
| `fixtures/clean-invoice.md` | 1 | Two documents, four lines, one tolerance breach |
| `fixtures/missing-line.md` | 2 | An invoice line with no order line, and a total that hides it |
| `fixtures/clean-invoice.md` | 3 | The same input, checked rather than produced |

## 1. Main path

```text
check evals/skills/productivity/invoice-check/fixtures/clean-invoice.md
```

Expect:

- `clean-invoice-report.md` beside the source.
- Exactly three lines.
- The total equals the sum of the line variances, to the cent.
- The largest variance is named with its line.
- No figure that is not in the fixture or a sum of them.

## 2. Variant

```text
check evals/skills/productivity/invoice-check/fixtures/missing-line.md
```

Expect:

- The unmatched line is listed with the reason.
- The total excludes the unmatched line and says so.
- The report does not invent an order line to close the gap.

## 3. Gate alone

```text
check evals/skills/productivity/invoice-check/runs/default/1-main/clean-invoice-report.md
```

Expect:

- The skill does not rewrite the report.
- It reports failures by check number.
- It stops before sending anything.

## Regression notes

- A change to `RULES.md` keeps scenario 1 passing.
- A change to the gate keeps all three passing.
