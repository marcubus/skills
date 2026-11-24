# Reply

Record written: `docs/adrs/ADR-0001-move-product-search-to-meilisearch.md`

## Shape

`docs/adrs/` was empty, so the record uses `FORMAT.md`'s default shape: the status block, then `## Context`, `## Decision`, `## Considered options`, `## Consequences`, with `## Open questions` as the one optional section. The repository keeps no index, so no `docs/adrs/README.md` row was added. Implementation is marked the `FORMAT.md` way, `**Implemented:**` after `Author` plus an `## Implementation` section at the flip; it is not present because nothing has landed.

No record in the corpus covers this decision. The corpus is empty, and the brief's ADR-0006 is not in this repository (see below).

## Triage

All three conditions hold. It is hard to reverse: moving search back means a second migration, a re-backfill and a restored Postgres path. It is surprising without context: a reader of the code would ask why product search leaves the database that holds the catalogue. It is a real trade-off: two alternatives lost for stated reasons. So the record is written, and the lighter home was not taken.

## Suite

The decision is delivered by CAT-812, CAT-813 and CAT-814, named in `Refs:` by ID. They stay in the external tracker. The record carries no checklist, phase status or progress note; that belongs to those tickets.

## Status

`proposed`, because nothing is implemented yet and the repository holds no change for it. `Date` is 2026-11-20, the day the platform team decided. `Author` is the platform team, the identity the brief names as deciding; no requester identity was supplied. `Revisit by` is 2027-05-20, since the decision rests on catalogue size and on the managed-service price.

## Two things the interview could not settle

1. **ADR-0006.** The brief says this decision depends on ADR-0006, which put the catalogue import on its own queue. No such file exists in this repository, so it is not cited in the record: a citation would be a claim the repository cannot support, and it would break the link check. If ADR-0006 exists elsewhere, add it to `Refs:` as `ADR-0006`. The record's rule 4 still stands on its own, but the queue that makes it work is not evidenced here.
2. **Evidence for the stall.** The four-hour stall and the stale prices come from the brief alone. No incident report or monitoring export was supplied, and the record says so in `Context` rather than presenting the figures as verified.

Neither changes the decision, so neither keeps the record open; the ownership unknown sits under `## Open questions`.

## Gate

| Check | Result | Evidence |
|---|---|---|
| C1 | pass | `ADR-0001-move-product-search-to-meilisearch.md` matches `^[0-9]{4}-[a-z0-9]+(-[a-z0-9]+)*\.md$` |
| C2 | pass | `docs/adrs/` holds one file; no repeated number; `0001` is one past the highest (none) |
| C3 | pass | `**Status:** proposed`, one of the four values; no implementation in the repository, so `proposed` matches the evidence |
| C4 | pass | `Status`, `Date`, `Author` on lines 3 to 5, in order; `Date` is `2026-11-20`; `Revisit by` and `Refs` in the same block |
| C5 | pass | headings read `Context`, `Decision`, `Considered options`, `Consequences` in order |
| C6 | pass | no relative links and no `ADR-NNNN` citation, so nothing to resolve (ADR-0006 deliberately left out, see above) |
| C7 | not applicable | no `docs/adrs/README.md`; the repository keeps no index |
| C8 | not applicable | status is `proposed`; no `**Implemented:**` line and no `## Implementation`, as the lifecycle requires |
| C9 | pass | the secret pattern returns no hits |
| C10 | pass | title "Move product search from Postgres to Meilisearch" names the action and the choice |
| C11 | pass | `Context` names the four-hour sync stall and the 2026-11-20 decision |
| C12 | pass | Postgres tuning lost on the shared disk budget; a managed service lost on cost; both carry reasons |
| C13 | pass | `Consequences` names the thirty-second lag, the outright search outage, and the cross-team dependency |
| C14 | pass | the stall and its source are named as the brief, with the missing incident report stated; the ticket IDs and the dependency are named, not asserted from thin air |
| C15 | pass | title, rules and consequences all speak to where product search is served |
| C16 | pass | the one unknown is under `## Open questions` and does not change the decision |
| C17 | pass | `## Open questions` is the only optional section and rests on a surviving unknown |
| C18 | pass | no other record decides this; the corpus is empty |
| C19 | pass | all three triage conditions hold (see above) |
| C20 | pass | the progress pattern finds nothing; the suite is in `Refs:` and the work stays on the tickets |

All twenty checks pass or are not applicable.
