# ADR run — scenario 3 (supersede)

## Deliverable

`docs/adr/0008-cache-in-redis.md` — **status: `proposed`**

## Changes to existing files

1. `docs/adr/0007-cache-in-postgres.md` — one line changed: `**Status:** accepted` → `**Status:** superseded by ADR-0008`. Nothing else in the record was touched (FORMAT.md, "Amending and superseding": the status line is the only edit a superseded record takes).
2. `docs/adr/README.md` — appended the row `| [0008](0008-cache-in-redis.md) | Move the parsed-transaction cache to Redis | proposed |`, and changed the existing 0007 row's status cell from `accepted` to `superseded by ADR-0008` so the index does not contradict the record. No row was reordered or removed.

## Shape and corpus

- `docs/adr/` held one record, `0007-cache-in-postgres.md`, plus an index. There was no pair of highest-numbered records to compare, so the shape followed that record: status block, `Context`, `Decision`, `Considered options`, `Consequences`, and `Implementation` where the record is accepted. The new record keeps the same headings, adds `Open questions`, and omits `Implementation` because it is not accepted (C8).
- Record that already covers the decision: ADR-0007, "Keep the parsed-transaction cache in Postgres". Its Decision section decides the same question — where parsed transactions are cached — so this run is a successor, not a new decision and not an amendment.

## Triage

All three hold, so the record was written: hard to reverse (the table is dropped and a second service becomes load-bearing), surprising without context (the code now depends on Redis when Postgres was there and worked), and a real trade-off (three alternatives, each with a stated loss).

## Interview

No user was available. The brief was taken as the answer to every question, so no rounds were run and nothing was asked. Unknowns that the brief did not settle are under `## Open questions`.

Settled from the brief: title, three alternatives with reasons, the costs, and the fallback that survives the change.

## Status evidence

`proposed`. The brief says the table is dropped "in the same change", but this repository contains no `ledger` code — `docs/adr/` is the only content — so there is no diff or git log entry to show the change landed. Per FORMAT.md the evidence decides, not the tense of the request, so the record is `proposed` and the gap is the first line under `## Open questions`. `Implemented:` and `## Implementation` are therefore absent.

## Gate

| Check | Result | Evidence |
|---|---|---|
| C1 Filename | pass | `docs/adr/0008-cache-in-redis.md`; the grep printed nothing |
| C2 Number | pass | no duplicate numbers; highest is `0008`, the record's number |
| C3 Status | pass | `**Status:** proposed` is one of the four values |
| C4 Status block | pass | `Status`, `Date` (2026-11-18), `Author` in that order under the title |
| C5 Core sections | pass | `Context Decision Considered options Consequences`, in order, under the repo's own name for the options section |
| C6 Links resolve | pass | both commands printed nothing; the only targets are `0007-cache-in-postgres.md` and `ADR-0007` |
| C7 Index row | pass | one row for 0008, title matches the record's `# ` title |
| C8 Implemented shape | not applicable | record is `proposed`; `Implemented:` and `## Implementation` counts are 0, as expected |
| C9 No secret | pass | no hit; the record names no credential at all |
| C10 Title | pass | "Move the parsed-transaction cache to Redis" — verb plus the choice |
| C11 Context trigger | pass | two concurrent CLI runs contending on the table, and a report blocked behind a rebuild |
| C12 Options lose for a reason | pass | narrowed lock, JSON directory, read replica — each with its reason |
| C13 Cost named | pass | Redis outage degrades every month at once; range queries become N key reads; the notebook must change |
| C14 Claims proved | pass | the row-lock cost cites ADR-0007 Consequences; the 3 s behind 40 s contention and the existing Redis instance cite the change brief of 2026-11-18; the 40 s rebuild cites ADR-0007 Context |
| C15 One decision | pass | where the cache lives; dropping the table and keeping the fallback are consequences of that one choice, not a second one |
| C16 Unknowns labelled | pass | two lines under `## Open questions`, neither changes the choice of store, and the status stays `proposed` |
| C17 No padding | pass | `Open questions` is the only optional section and earns its ladder row; it repeats no core section |
| C18 No duplicate decision | pass | ADR-0007 is the only record on this question and it is now `superseded by ADR-0008`; its decision text is unedited |

## Open questions carried into the record

- Whether the change has landed in the repository (it is `proposed` on that basis).
- Key expiry or eviction policy for the Redis keys — unrecorded, and it does not change the decision.
