# Reply

Record written: `docs/adrs/ADR-0001-convert-timestamps-to-utc-at-the-service-boundary.md`

## Shape notes

- `docs/adrs/` was empty, so the record follows `FORMAT.md`'s house shape. No highest-numbered record existed to copy.
- No covering record exists: nothing in the directory decides when timestamps are normalised (C18).
- The repository keeps no issue tracker, wiki or `docs/tickets/`, and no ticket exists or is planned for this change. Delivery is unscheduled, and the record names no suite in `Refs:`.
- The `Refs:` line is omitted: there are no records, files or tickets for it to list.
- The `Revisit by:` line is omitted: the decision rests on no vendor, version, load figure or price that can change. The one dated condition, the backfill, is work for the ticket, and no ticket exists yet.
- `Deciders:` is omitted because the two maintainers' names are not known. `Context` records that the two maintainers made the decision on 2026-11-19.
- `Author:` is `marcus`, the configured git user, since the change is not committed and that is the requester's identity.

## Gate

| Check | Result | Evidence |
|---|---|---|
| C1 Filename | pass | `ADR-0001-convert-timestamps-to-utc-at-the-service-boundary.md` matches `^[0-9]{4}-[a-z0-9]+(-[a-z0-9]+)*\.md$` |
| C2 Number | pass | only file in `docs/adrs/`; number `0001` is unused and one past the highest (none) |
| C3 Status | pass | `**Status:** proposed`, one of the four values; evidence matches: the brief says the change is not implemented, and the repo holds no change |
| C4 Status block | pass | `Status`, `Date` (`2026-11-19`), `Author` in that order within the first 3 lines |
| C5 Core sections | pass | `## Context`, `## Decision`, `## Considered options`, `## Consequences`, in order |
| C6 Links resolve | pass | no relative link targets and no `ADR-NNNN` references |
| C7 Index row | n/a | `docs/adrs/README.md` does not exist, so the repo keeps no index |
| C8 Implemented shape | n/a | record is `proposed`, so no `**Implemented:**` line and no `## Implementation` section |
| C9 No secret | pass | grep for password/token/key/secret assignments returns nothing |
| C10 Title states the decision | pass | "Convert timestamps to UTC at the service boundary" names the choice and carries the verb "Convert" |
| C11 Context names the trigger | pass | the settlement ledger ordering bug, with the five-hour two-region disagreement |
| C12 Every option lost for a reason | pass | two alternatives, each with its rejection reason (four consumers need locale not stored; index width doubles for two of four consumers) |
| C13 A cost is named | pass | historical rows keep local-time values, so cutover-spanning queries need a date-aware filter |
| C14 Every claim has proof | pass | figures and facts come from the request for the record, cited in `## Consequences` as reported by the maintainers on 2026-11-24; no paths are asserted |
| C15 One decision | pass | title, rules and consequences all speak to normalising ingress timestamps to UTC |
| C16 Unknowns are labelled | pass | no open unknown survives; no `## Open questions` section needed |
| C17 No padding | pass | only the four core sections; no optional section present |
| C18 No duplicate decision | pass | no other record exists; none decides this question |
| C19 Triage | pass | hard to reverse (storage convention across all ingress and history), surprising without context (why not convert at read time), real trade-off (two alternatives lost for stated reasons) |
| C20 No work in flight | pass | no checklist, progress section or status marker; delivery is unscheduled and `Refs:` names no suite |

Twenty checks: 18 pass, 2 not applicable (C7, C8), 0 fail.
