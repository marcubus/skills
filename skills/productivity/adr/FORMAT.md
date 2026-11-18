# The shape of a record

The default house shape. A target repo that already keeps records wins on section naming and on how it marks implementation; the four core sections and the status enum are this skill's standard.

## Contents

- Where records live
- Triage
- The status block
- The core sections
- The optional ladder
- The lifecycle
- Amending and superseding
- The index row

## Where records live

docs/adr/ at the repository root. Create it on the first record. The filename is NNNN-slug.md: four digits, zero-padded, one past the highest existing number, and a hyphenated lowercase slug that names the choice.

## Triage

Write a record when all three hold:

1. **Hard to reverse.** Changing your mind later costs real work.
2. **Surprising without context.** A reader of the code would ask why.
3. **A real trade-off.** A genuine alternative lost for a stated reason.

When one fails, name the lighter home: a commit message, a README line, a comment at the code, or MEMORY.md.

## The status block

The block under the title, before the first section:

```markdown
**Status:** <status>
**Date:** YYYY-MM-DD
**Author:** <author>
**Deciders:** <names>
**Revisit by:** YYYY-MM-DD
**Refs:** ADR-NNNN, <path>
```

`Status`, `Date` and `Author` are required. `Deciders` names everyone who agreed, when that is more than the author. `Revisit by` names the date the decision should be re-examined. `Refs` lists the records and files the decision leans on. An accepted record adds `**Implemented:** YYYY-MM-DD` after `Author`.

`Status` holds one of the four values in the lifecycle table. `Date` is the day the decision was made, in ISO 8601, and it stays fixed. `Author` is the identity that made the decision: the git user for a change already committed, otherwise the person who asked for the record.

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
| `## Acceptance criteria` | the work is handed to someone else |
| `## Implementation` | the record has been implemented |
| `## Open questions` | an unknown survived the interview |
| `## Residual risk` | a risk is accepted and tracked elsewhere |
| `## References` | the proof is a list of files rather than a sentence |
| `## Amendment — YYYY-MM-DD: <title>` | a detail of an accepted decision changed |

`## Implementation` names the files and commands that carried the decision out, taken from the change itself: the diff or the git log.

## The lifecycle

| Status | Means |
|---|---|
| `proposed` | decided, not yet built |
| `accepted` | implemented |
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

A decision that touches facts cited by more than one record names each of them in `Refs` and links it.

## The index row

When docs/adr/README.md exists, append one row per record:

```markdown
| [NNNN](NNNN-slug.md) | <title> | <status> |
```

The title is written as the record writes it. The row is appended, never reordered.
