# Evals: adr

Four scenarios, five fixtures, one recorded run each. The skill never references this folder and cannot read it, because it sits outside the skill directory.

## Fixtures

| File | Used by | What it carries |
|---|---|---|
| `fixtures/scenario-1-decision-brief.md` | 1 | A decision that passes triage, with every fact supplied and no `docs/adr` yet |
| `fixtures/scenario-2-reversible-choice.md` | 2 | A decision that fails all three triage conditions |
| `fixtures/scenario-3-change-brief.md` | 3 | A decision an accepted record already holds, with the decision itself changed |
| `fixtures/scenario-3-repo/` | 3 | `docs/adr/0007-cache-in-postgres.md` (accepted, implemented) and an index with one row |
| `fixtures/scenario-4-repo/` | 4 | `docs/adr/0004-session-storage.md` with eight planted defects |

## 1. Main path

```text
Read evals/skills/productivity/adr/fixtures/scenario-1-decision-brief.md and write the record in runs/default/1-write/.
```

Expect:

- One file at `docs/adr/0001-<slug>.md` under the run folder, slug three to five hyphenated words.
- `**Status:** proposed`, and `Date`, `Author` present.
- `Context`, `Decision`, `Considered options`, `Consequences` as `## ` headings, in that order.
- The JSON-files alternative is named, with the reason it lost.
- At least one cost is named: the hand-editable cache file, or the version column and rebuild path.
- The 40-second rebuild and Python 3.12 appear as given, and no figure appears that the brief does not contain.
- No `docs/adr/README.md` is created.

## 2. Triage refusal

```text
Read evals/skills/productivity/adr/fixtures/scenario-2-reversible-choice.md and act on it, in runs/default/2-refusal/.
```

Expect:

- No file is written anywhere.
- The reply names the three conditions and says which ones fail.
- A lighter home is named, such as the commit message or `MEMORY.md`.
- At most three questions are asked, and none of them asks for a fact the brief already supplies.

## 3. Supersede

```text
Copy evals/skills/productivity/adr/fixtures/scenario-3-repo/ into runs/default/3-supersede/, read evals/skills/productivity/adr/fixtures/scenario-3-change-brief.md, and act on it.
```

Expect:

- A new record at `docs/adr/0008-<slug>.md`, status `proposed`.
- `0007-cache-in-postgres.md` carries `**Status:** superseded by ADR-0008`.
- Every line of 0007 above the status line is unchanged, compared against the fixture.
- The new record names Redis, the contention trigger, the Postgres option with its rejection reason, and the cost of the move.
- The index holds two rows, the new one appended second, and the 0007 row's status cell matches its new status.
- No amendment section is added to 0007.

## 4. Gate alone

```text
Copy evals/skills/productivity/adr/fixtures/scenario-4-repo/ into runs/default/4-review/ and review the record there.
```

Expect:

- Findings name at least C5, C6, C9, C10, C11, C12 and C13, each with a file and a line. C8 is skipped for a record this skill did not write, and C3 is reported in its place.
- C5 (heading order) and C6 (broken link) are fixed in place and reported as diffs, and C9 and C17 clear with the off-ladder section that held the value.
- C10, C11, C12 and C13 are reported and routed to write mode, not applied.
- The `**Status:**` line still reads `accepted`.
- The quoted value under `## Configuration` is removed or replaced by the variable name, and C9 is reported.
- No decision text is rewritten.

## Regression notes

- A change to `FORMAT.md` keeps scenario 1 passing.
- A change to `GATE.md` keeps scenario 4 passing.
- A change to the entry file keeps the four deliverables stable.
