# Gate

Run every check with the agent's file and search tools, using the table below. When the host has a POSIX shell, the command under each mechanical check is an equivalent route, run from the repository root with ADR-NNNN-slug.md replaced by the record's own filename. The agent route is primary; the command is the fallback. A check passes only when its result is observed, by either route.

| Check | Agent route | Pass when |
|---|---|---|
| C1 | List `docs/adrs/`, open the record path, match the basename against `^ADR-[0-9]{4}-[a-z0-9]+(-[a-z0-9]+)*\.md$` | The name matches |
| C2 | List the `docs/adrs/` filenames, read the four digits after `ADR-` in each, and compare them | No number repeats, and a new record's number is one past the highest |
| C3 | Read the record, find the `**Status:**` line, compare its value with the four in `FORMAT.md` | One of the four values is present |
| C4 | Read the first 12 lines and find `**Status:**`, `**Date:**`, `**Author:**` | The three appear in that order and `Date` is `YYYY-MM-DD` |
| C5 | Read every `## ` heading in order | `Context`, `Decision`, the options heading, and `Consequences` appear in order |
| C6 | For every relative link target and every `ADR-NNNN`, list the target path or the matching `ADR-NNNN-*.md` file | Every target exists |
| C7 | If docs/adrs/README.md exists, search it for `[ADR-NNNN](` | Exactly one row, with matching title and status |
| C8 | Read the record and count `**Implemented:** YYYY-MM-DD` and `## Implementation` | Each appears once for an accepted record, or the check is not applicable |
| C9 | Search the record for `(password\|token\|key\|secret) *= *\S` | Every hit is a name with no value beside it |
| C21 | Read the ticket IDs in `Refs:` and list `docs/tickets/` | Every ticket ID names one file, and no ID repeats |

## Contents

- Brought-in work
- Mechanical checks
- Judgement checks
- Step map

## Brought-in work

A review of a record this skill did not write skips C8 and says so in the report. That check tests the shape this skill produces. Every other check applies unchanged.

The report names every place the repo's shape differs from `FORMAT.md`, since C5 and C8 accept the repo's own answer.

## Mechanical checks

**C1 Filename.** The path is docs/adrs/ADR-NNNN-slug.md: the `ADR-` prefix, four digits, then a hyphenated lowercase slug.

```bash
printf '%s\n' docs/adrs/ADR-NNNN-slug.md | grep -vE '^docs/adrs/ADR-[0-9]{4}-[a-z0-9]+(-[a-z0-9]+)*\.md$'
```

Done when the check finds nothing.

**C2 Number.** No other file shares the number, and a new record takes one past the highest in the directory.

```bash
ls docs/adrs | grep -oE '^ADR-[0-9]{4}' | sort -n | uniq -d
ls docs/adrs | grep -oE '^ADR-[0-9]{4}' | sort -n | tail -1
```

Done when the first check finds nothing and, for a record being created, the second returns the record's number.

**C3 Status.** `**Status:**` holds one of the four values in `FORMAT.md`.

```bash
grep -E '^\*\*Status:\*\* (proposed|accepted|superseded by ADR-[0-9]{4}|rejected)$' \
  docs/adrs/ADR-NNNN-slug.md
```

Done when the check returns one line. An `accepted` status also matches the evidence: the change is present in the repo, read from the diff or the git log.

**C4 Status block.** `Status`, `Date` and `Author` are present, in that order, under the title, and `Date` is ISO 8601.

```bash
sed -n '1,12p' docs/adrs/ADR-NNNN-slug.md | grep -E '^\*\*(Status|Date|Author):\*\*'
```

Done when the three appear in that order and `Date` matches `YYYY-MM-DD`, and any `Deciders`, `Revisit by` or `Refs` line sits in the same block.

**C5 Core sections.** `Context`, `Decision`, `Considered options` and `Consequences` are present as `## ` headings, in that order.

```bash
grep -oE '^## (Context|Decision|Considered options|Alternatives considered|Consequences)$' docs/adrs/ADR-NNNN-slug.md \
  | sed 's/Alternatives considered/Considered options/' | tr '\n' ' '; echo
```

Done when it returns the four in that order, under the repo's own name for the options section where that differs. A repo using a third name is judged by this line, not by the command.

**C6 Links resolve.** Every relative link target exists, and every `ADR-NNNN` names a file in the directory.

```bash
grep -oE '\]\([^)]+\)' docs/adrs/ADR-NNNN-slug.md \
  | sed -e 's/^](//' -e 's/)$//' \
  | grep -vE '^(#|[a-z][a-z0-9+.-]*:)' \
  | while read -r f; do [ -e "docs/adrs/$f" ] || echo "broken: $f"; done
grep -oE 'ADR-[0-9]{4}' docs/adrs/ADR-NNNN-slug.md | sort -u \
  | while read -r a; do ls docs/adrs/"$a"-*.md >/dev/null 2>&1 || echo "missing: $a"; done
```

Done when both checks find nothing.

**C7 Index row.** When docs/adrs/README.md exists, it holds exactly one row for this number, and the row's title and status cell match the record's.

```bash
if [ -e docs/adrs/README.md ]; then
  n=$(basename docs/adrs/ADR-NNNN-slug.md | cut -c5-8)
  grep "\[ADR-$n\](" docs/adrs/README.md
fi
```

Done when the check returns one such row, and the agent read its title and status cells against the record.

**C8 Implemented shape.** A record with status `accepted` carries `**Implemented:**` after `Author` and an `## Implementation` section.

```bash
grep -cE '^\*\*Implemented:\*\* [0-9]{4}-[0-9]{2}-[0-9]{2}$' docs/adrs/ADR-NNNN-slug.md
grep -cE '^## Implementation$' docs/adrs/ADR-NNNN-slug.md
```

Done when both return `1` for an accepted record, or the record is not accepted and the check is marked not applicable, or the repo marks implementation another way and the record carries that marker, named in the reply.

**C9 No secret.** No line quotes a password, token or key value. The record names the variable instead.

```bash
grep -niE '[A-Za-z0-9_]*(password|token|key|secret)[A-Za-z0-9_]* *[:=] *[^ ]' docs/adrs/ADR-NNNN-slug.md
```

Done when every hit is a name with no value beside it. A bare value with no name is a read, not a match.

**C21 Ticket stubs resolve.** Every ticket ID in the record names one file in docs/tickets/, and no two files share an ID. A ticket may name this record, another record, or none.

```bash
grep -oE '(BUG|FEAT|TASK)-[0-9]{4}' docs/adrs/ADR-NNNN-slug.md | sort -u \
  | while read -r t; do
      ls docs/tickets/"$t"-*.md >/dev/null 2>&1 || echo "missing: $t"
    done
ls docs/tickets 2>/dev/null | grep -oE '^(BUG|FEAT|TASK)-[0-9]{4}' | sort | uniq -d
```

Done when both checks find nothing. When the repo keeps no file tickets, the record's tickets are external IDs, and the check is marked not applicable.

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

**C19 Triage.** The decision holds all three triage conditions in `FORMAT.md`. Done when all three hold, or the reply names the lighter home, per the examples in *Triage*.

**C20 No work in flight.** The record carries no work in flight; outstanding work lives on the ticket the record names.

```bash
grep -nE '^- \[[ x]\]|^## (Progress|Status|Next steps)$|\b(still running|in progress|remaining work)\b' docs/adrs/ADR-NNNN-slug.md
```

Done when the command finds nothing, and every suite the record is delivered by is named in `Refs:`. A record that names no ticket passes.

## Step map

A step maps to the checks that catch its omission.

| Step | Checks |
|---|---|
| Write 1, house shape and corpus | C2, C3, C4, C5, C18 |
| Write 2, triage | C19 |
| Write 3, interview | C11, C16 |
| Write 4, resolve and name the suite | C10, C12, C13, C14, C15, C20 |
| Write 5, write the file | C1, C2, C3, C4, C5, C6, C8, C9, C17, C18 |
| Write 6, open the ticket stubs | C21 |
| Write 7, index | C7 |
| Write 8, gate | C1 to C21 |
| Review 1, read | C6 |
| Review 2, gate | C1 to C21, minus C8 for brought-in work |
| Review 3, editorial | C1, C2, C4, C5, C6, C7, C9 |
| Review 4, route | C3, C8, C10 to C18, C20, C21; C19 to a lighter home |
| Review 5, report | C1 to C21 |
