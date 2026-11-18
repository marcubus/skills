# Gate

A check that names a command is settled by running it from the repository root, with NNNN-slug.md replaced by the record's own filename.

## Contents

- Brought-in work
- Mechanical checks
- Judgement checks
- Step map

## Brought-in work

A review of a record this skill did not write skips C8 and says so in the report. That check tests the shape this skill produces. Every other check applies unchanged.

The report names every place the repo's shape differs from `FORMAT.md`, since C5 and C8 accept the repo's own answer.

## Mechanical checks

**C1 Filename.** The path is docs/adr/NNNN-slug.md: four digits, then a hyphenated lowercase slug.

```bash
printf '%s\n' docs/adr/NNNN-slug.md | grep -vE '/[0-9]{4}-[a-z0-9]+(-[a-z0-9]+)*\.md$'
```

Done when the command prints nothing.

**C2 Number.** The number is unused, and it is one past the highest in the directory.

```bash
ls docs/adr | grep -oE '^[0-9]{4}' | sort -n | uniq -d
ls docs/adr | grep -oE '^[0-9]{4}' | sort -n | tail -1
```

Done when the first command prints nothing and the second prints the record's number.

**C3 Status.** `**Status:**` holds one of the four values in `FORMAT.md`.

```bash
grep -E '^\*\*Status:\*\* (proposed|accepted|superseded by ADR-[0-9]{4}|rejected)$' \
  docs/adr/NNNN-slug.md
```

Done when the command prints one line. An `accepted` status also matches the evidence: the change is present in the repo, read from the diff or the git log.

**C4 Status block.** `Status`, `Date` and `Author` are present, in that order, under the title, and `Date` is ISO 8601.

```bash
sed -n '1,12p' docs/adr/NNNN-slug.md | grep -E '^\*\*(Status|Date|Author):\*\*'
```

Done when the three appear in that order and `Date` matches `YYYY-MM-DD`, and any `Deciders`, `Revisit by` or `Refs` line sits in the same block.

**C5 Core sections.** `Context`, `Decision`, `Considered options` and `Consequences` are present as `## ` headings, in that order.

```bash
grep -oE '^## (Context|Decision|Considered options|Alternatives considered|Consequences)$' docs/adr/NNNN-slug.md \
  | sed 's/Alternatives considered/Considered options/' | tr '\n' ' '; echo
```

Done when it prints the four in that order, under the repo's own name for the options section where that differs. A repo using a third name is judged by this line, not the command.

**C6 Links resolve.** Every relative link target exists, and every `ADR-NNNN` names a file in the directory.

```bash
grep -oE '\]\([^)]+\)' docs/adr/NNNN-slug.md \
  | sed -e 's/^](//' -e 's/)$//' \
  | grep -vE '^(#|[a-z][a-z0-9+.-]*:)' \
  | while read -r f; do [ -e "docs/adr/$f" ] || echo "broken: $f"; done
grep -oE 'ADR-[0-9]{4}' docs/adr/NNNN-slug.md | sort -u \
  | while read -r a; do ls docs/adr/"${a#ADR-}"-*.md >/dev/null 2>&1 || echo "missing: $a"; done
```

Done when both commands print nothing.

**C7 Index row.** When docs/adr/README.md exists, it holds exactly one row for this number, and the row's title and status cell match the record's.

```bash
if [ -e docs/adr/README.md ]; then
  n=$(basename docs/adr/NNNN-slug.md | cut -c1-4)
  grep "\[$n\](" docs/adr/README.md
fi
```

Done when the command prints one such row.

**C8 Implemented shape.** A record with status `accepted` carries `**Implemented:**` after `Author` and an `## Implementation` section.

```bash
grep -cE '^\*\*Implemented:\*\* [0-9]{4}-[0-9]{2}-[0-9]{2}$' docs/adr/NNNN-slug.md
grep -cE '^## Implementation$' docs/adr/NNNN-slug.md
```

Done when both print `1` for an accepted record, or the record is not accepted and the check is marked not applicable, or the repo marks implementation another way and the record carries that marker, which is the heading its accepted records share.

**C9 No secret.** No line quotes a password, token or key value. The record names the variable instead.

```bash
grep -niE '[A-Za-z0-9_]*(password|token|key|secret)[A-Za-z0-9_]* *= *[^ ]' docs/adr/NNNN-slug.md
```

Done when every hit is a name with no value beside it. A bare value with no name is a read, not a match.

## Judgement checks

**C10 Title states the decision.** The title names what was chosen, as a phrase with a verb, not a topic noun. "Store the queue in Postgres" passes; "Queue storage" fails. Done when the title holds a verb and names the choice.

**C11 Context names the trigger.** The section names the event or constraint that forced a decision now, not only the background. Done when that event or constraint is present.

**C12 Every option lost for a reason.** Each alternative carries the reason it was rejected. Done when at least two options appear and each carries its reason.

**C13 A cost is named.** `Consequences` names at least one thing the choice gives up, not only what it buys. Done when one cost is present.

**C14 Every claim has proof.** Each measurement, path and external fact names the file, command or source that proves it. Done when every figure and path carries its proof.

**C15 One decision.** The record does not bundle a second, unrelated choice. Done when the title, the `## Decision` rules and the `## Consequences` all speak to one choice.

**C16 Unknowns are labelled.** Every open unknown sits under `## Open questions`, and none of them changes the decision. Done when each unknown is under that heading, and one that would change the decision leaves the record `proposed`.

**C17 No padding.** Every optional section earns its place, by a row in `FORMAT.md`'s optional ladder or by the repo already using it, and none restates a core section. Done when each optional section has its place and repeats no core section.

**C18 No duplicate decision.** No other record decides the same thing. A change to an existing decision is an amendment or a successor, and an amendment heading reads `## Amendment — YYYY-MM-DD: <title>`. Done when no other record decides the same thing, and any change to an accepted record appears as an amendment section or a successor rather than as edited decision text.

**C19 Triage.** The decision holds all three triage conditions in `FORMAT.md`. Done when all three hold, or the reply names the lighter home.

## Step map

A step maps to the checks that catch its omission.

| Step | Checks |
|---|---|
| Write 1, house shape and corpus | C2, C3, C4, C5, C18 |
| Write 2, triage | C19 |
| Write 3, interview | C11, C16 |
| Write 4, resolve | C10, C12, C13, C14, C15 |
| Write 5, write the file | C1, C2, C3, C4, C5, C6, C8, C9, C17, C18 |
| Write 6, index | C7 |
| Write 7, gate | C1 to C19 |
| Review 1, read | C6 |
| Review 2, gate | C1 to C19, minus C8 for brought-in work |
| Review 3, editorial | C1, C2, C4, C5, C6, C7, C9 |
| Review 4, route | C3, C8, C10 to C19 |
| Review 5, report | C1 to C19 |
