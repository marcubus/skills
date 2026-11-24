# The shape of a record

The default house shape. A target repo that already keeps records wins on section naming and on how it marks implementation; the four core sections and the status enum are this skill's standard.

## Contents

- Where records live
- Triage
- Records and tickets
- The status block
- The core sections
- The optional ladder
- The lifecycle
- Amending and superseding
- The index row

## Where records live

docs/adrs/ at the repository root. Create it on the first record. The filename is ADR-NNNN-slug.md: the prefix `ADR-`, four digits zero-padded, one past the highest existing record number, and a hyphenated lowercase slug that names the choice.

## Triage

Write a record when all three hold:

1. **Hard to reverse.** Changing your mind later costs real work.
2. **Surprising without context.** A reader of the code would ask why.
3. **A real trade-off.** A genuine alternative lost for a stated reason.

When one fails, name the lighter home: a ticket first, then a commit message, a README line, a comment at the code, or the session log.

**Ticket** means wherever the repository already keeps work items: an issue tracker, a wiki page, a project board, a backlog file. The record references a ticket by its ID or URL. When the repository keeps no tracker and the delivery needs tickets, the default is a folder of files beside the records, `docs/tickets/`, one file per item, and the skill writes the stub.

A file ticket is named `<TYPE>-<NNNN>-<slug>.md`, where `TYPE` is `BUG`, `FEAT` or `TASK`, `NNNN` is four digits one past the highest of that type in docs/tickets/, and the slug is hyphenated lowercase. The stub carries:

```markdown
# <title>

**Type:** BUG | FEAT | TASK
**Status:** open
**Record:** ADR-NNNN, or none

## Scope

One sentence naming the part of the decision this ticket delivers.
```

The link runs both ways and is optional in both: a record may name no ticket, and a ticket may name no record. The three conditions decide, on consequence rather than category. The table below lists only the cases that most often trip them:

| The content is | It belongs in |
|---|---|
| a procedure someone follows: runbook, upgrade drill, release steps | the procedure's own document, linked from the ticket |
| an install: a download, a pinned asset set, a model or a tool added to a host | the ticket |
| a one-off migration or refactor whose contract is already fixed | the ticket |
| a checklist, an acceptance test, a phase status | the ticket |
| a convention whose alternatives are written beside the artefact it governs | the artefact's own README, linked from the ticket |

A choice still earns a record when it shapes what other choices are possible: where state lives, who may hold a credential, what the ingress model is, which contract other services code against. A model install is a ticket even when the reasoning behind it is long; a two-line ownership rule is a record when every future dataset inherits it.

## Records and tickets

A record decides; a ticket executes. One decision delivered by a suite of tickets is the normal case for anything that spans a repository boundary or needs an admin step.

- **The ticket's home is the repository's own.** An external tracker or wiki is the item's home; with neither, the files live in docs/tickets/.
- **The record carries the decision, the alternatives and the cost.** It names the suite in `Refs:` and stops there.
- **The ticket carries the work items, the acceptance checks and the progress.** The stub the skill writes is a placeholder for that content, not the content itself. The ticket links back to the record for the reason.
- **A record carries no work in flight**: no checklist, status marker or progress section. That content moves to the ticket the record names.
- **The suite is named when the decision is made**, not when the first commit lands. When the repo keeps files, the skill opens a stub for each ticket the suite needs and names them in `Refs:`. A record may name no ticket at all, and a ticket may stand alone with no record.
- **The direction is one-way.** A record may name ten tickets; no ticket amends the record. A ticket that finds the decision wrong comes back as an amendment or a successor.
- **When the change lands**, the implementer flips the record to `accepted` and writes `## Implementation` once.

## The status block

The block under the title, before the first section:

```markdown
**Status:** <status>
**Date:** YYYY-MM-DD
**Author:** <author>
**Deciders:** <names>
**Revisit by:** YYYY-MM-DD
**Refs:** ADR-0000, <path>, <TASK-0000>
```

A line that does not apply is omitted, not left empty.

`Status`, `Date` and `Author` are required. `Deciders` names everyone who agreed, by name, when that is more than the author and the names are known. `Revisit by` names the date the decision should be re-examined, and appears whenever the decision rests on a condition that can change: a vendor, a version, a load figure, a price. `Refs` lists the records, files and tickets the decision leans on or is delivered by, each ticket by its ID or URL. An accepted record adds `**Implemented:** YYYY-MM-DD` after `Author`.

`Status` holds one of the four values in the lifecycle table. `Date` is the day the decision was made, in ISO 8601, and it stays fixed. `Author` is the identity that made the decision: the repository's configured git user for a change already committed, otherwise the person who asked for the record.

A one-paragraph preamble may sit between the status block and `Context`, stating what the record applies to and which record it complements.

## The core sections

Four, in this order, each an `## ` heading:

- `## Context`: the trigger that forced a decision now, and enough of the situation for a reader who was not there.
- `## Decision`: numbered rules, each one a sentence that can be checked. The first rule is the choice itself.
- `## Considered options`, or the repo's own name for it: every alternative, each with the reason it lost. Two at minimum.
- `## Consequences`: what follows, including at least one cost.

## The optional ladder

Add a section only when it carries weight no other section can:

| Section | Earns its place when |
|---|---|
| `## Design` | the mechanism is not obvious from the decision |
| `## Verification` | a command proves the decision holds |
| `## Rollback` | undoing it has steps worth writing down |
| `## Implementation` | the record has been implemented |
| `## Open questions` | an unknown survived the interview |
| `## Residual risk` | a risk is accepted and tracked elsewhere |
| `## References` | the proof is a list of files rather than a sentence |
| `## Amendment — YYYY-MM-DD: <title>` | a detail of an accepted decision changed |

`## Implementation` names the files and commands that carried the decision out, taken from the change itself: the diff or the git log. It is written once, at the flip.

## The lifecycle

| Status | Means |
|---|---|
| `proposed` | decided, not yet built |
| `accepted` | decided and in force; the change is in the repo |
| `superseded by ADR-NNNN` | replaced; the successor is named |
| `rejected` | considered and declined; the reason stays |

The status a written record takes follows from the evidence:

| The change is in the repo | Status | Implemented lines |
|---|---|---|
| no | `proposed` | added by the implementer at the flip |
| yes | `accepted` | written now |

The evidence in the repo decides, not the tense of the request. A change that has only partly landed is `proposed`. When the evidence is missing, the interview asks for it; a premise the user cannot settle becomes a line under `## Open questions`, and the record stays `proposed` until the evidence lands.

## Amending and superseding

- **The record is still `proposed`.** Edit it in place. The amendment rule below starts at `accepted`.
- **The decision stands, a detail moved.** Append the amendment section the ladder names. State what changed, why, and what it replaces. Do not edit the text above it.
- **The decision itself changed.** Write a new record. Set the old record's status to `superseded by ADR-NNNN`, which is the only edit the old record takes. Link both ways.
- **The implementation changed, the decision did not.** That is the flip, recorded by the implementer, and neither an amendment nor a successor.

A decision that touches facts cited by more than one record names each of them in `Refs` and links it. A record the decision depends on but the repository does not hold is not named by its ID anywhere in the record, because a bare `ADR-NNNN` fails the link check. The reply names the gap, and the record describes the dependency in prose without the ID.

A record that is superseded leaves its ticket stubs alone: they close or transfer on their own tracker, and the successor names the stubs that remain open.

## The index row

When docs/adrs/README.md exists, append one row per record:

```markdown
| [ADR-NNNN](ADR-NNNN-slug.md) | <title> | <status> |
```

The row is appended, never reordered.
