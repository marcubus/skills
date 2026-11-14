# Report

Write the report where `Where things go` in `SKILL.md` says. The report is the deliverable for a review, and the record for a fix.

## Contents

- Template
- Writing a finding
- Decisions
- Verdict lines

## Template

```markdown
# Review: <skill>

## Verdict

<one line>

## Contract

<the one sentence from SURVEY.md>

## Inventory

| File | Lines | Role | Points at | Pointed at by |
|---|---|---|---|---|

## Fact table

| Fact | Where it appears | Single source |
|---|---|---|

## Findings

| id | severity | file:line | what | why | fix | status |
|---|---|---|---|---|---|---|

## Rounds

| Round | Blockers | Majors | Minors | Exit |
|---|---|---|---|---|

## Evals

| Scenario | Result | Evidence |
|---|---|---|

## Audit

| Check | Command | Hits |
|---|---|---|

## Decisions

<every transform and what it dropped>

## State

| Item | Value |
|---|---|
| Blockers | |
| Majors | |
| Minors | |
| Mode | |
| Phase reached | |
| Done | yes or no |
```

## Writing a finding

- `what` quotes the text or names the missing thing.
- `why` names the law or the check it breaks.
- `fix` is the smallest change that removes the class of problem, not just this instance.
- `status` is `open` or `fixed`, so the report shows what remains without re-reading the rounds.

A finding without a file and a line is not a finding. A finding without a fix is a complaint.

## Decisions

Record every transform: a file deleted, a step dropped, a mechanism moved, a rule retired. Name what was lost and why. This is where law 4 lands.

The State counts are computed from the findings table, not remembered.

## Verdict lines

- `Phase 2, stopped: 3 blockers, 4 majors.`
- `Phase 5, done: 0 blockers, 0 majors, 2 minors.`

The verdict states the current state. Round 1 counts belong in Rounds, not the verdict.
