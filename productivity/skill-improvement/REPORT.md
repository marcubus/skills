# Report

Write `reviews/<skill>.md` outside every skill folder. The report is the deliverable when the work stops before phase 5.

## Contents

- Template
- Writing a finding
- Verdict lines

## Template

```markdown
# Review: <skill>

## Verdict

<one line>

## Contract

<the one sentence from SURVEY.md>

## Inventory

| File | Lines | Role | Points at |
|---|---|---|---|

## Findings

| id | severity | file:line | what | why | fix |
|---|---|---|---|---|---|

## Rounds

| Round | Blockers | Majors | Minors | Exit |
|---|---|---|---|---|

## Evals

| Scenario | Result | Evidence |
|---|---|---|

## Audit

| Check | Command | Hits |
|---|---|---|

## State

| Item | Value |
|---|---|
| Blockers | |
| Majors | |
| Minors | |
| Phase reached | |
| Done | yes or no |
```

## Writing a finding

- `what` quotes the text or names the missing thing.
- `why` names the law or the check it breaks.
- `fix` is the smallest change that removes the class of problem, not just this instance.

A finding without a file and a line is not a finding. A finding without a fix is a complaint.

## Verdict lines

- `Phase 2, stopped: 3 blockers, 4 majors.`
- `Phase 5, done: 0 blockers, 0 majors, 2 minors.`
