# Reply

Record written: `docs/adrs/ADR-0001-deliver-outbound-webhooks-via-redis-job-queue.md`

There was no `docs/adrs/` directory before this record, so the shape is `FORMAT.md`'s default, not an existing house record. No record in the corpus covers this decision, so C18 is against an empty set.

Delivery is scheduled: the suite is `TASK-0002` (add the webhook topic and publisher) and `TASK-0003` (cut the API over and remove the inline path), named in `Refs:`. `TASK-0001`, the already-open retry-budget ticket, is not named in `Refs:` because it carries no record link and belongs to no ADR; it is described in `Context` in prose instead, since it is a predecessor, not part of this suite.

Status is `proposed`: nothing is implemented. The brief states the change is not implemented, and the repository only holds ticket stubs.

## Gate result per check

| Check | Result | Evidence |
|---|---|---|
| C1 | pass | `grep -vE '^docs/adrs/ADR-[0-9]{4}-[a-z0-9]+(-[a-z0-9]+)*\.md$'` returned nothing. |
| C2 | pass | No duplicate numbers; highest is `ADR-0001`, which is this record, one past the empty directory's high of none. |
| C3 | pass | `**Status:** proposed`, one line, and it matches the evidence: no implementation in the repo. |
| C4 | pass | `Status`, `Date` (2026-11-21, ISO 8601) and `Author` appear in that order in lines 3 to 5, with `Deciders`, `Revisit by` and `Refs` in the same block. |
| C5 | pass | Headings in order: `Context`, `Decision`, `Considered options`, `Consequences`. |
| C6 | pass | No relative link targets; the only `ADR-` mention is this record's own number, and `ADR-0001-*.md` exists. |
| C7 | not applicable | `docs/adrs/README.md` does not exist. No row appended. |
| C8 | not applicable | Status is `proposed`; no `**Implemented:**` line and no `## Implementation`. Both counts are 0, as expected for an unbuilt decision. |
| C9 | pass | No `password`, `token`, `key` or `secret` assignment matches. |
| C10 | pass | Title "Move outbound webhook delivery onto the Redis job queue" holds the verb "move" and names the chosen mechanism. |
| C11 | pass | `Context` names the trigger: a slow endpoint holding a worker for up to thirty seconds, and last month's eleven-minute public API outage from one endpoint that stopped reading. |
| C12 | pass | Two alternatives, each with its reason: inline delivery with a two-second timeout (drops slower endpoints, three of the ten largest customers are slower); managed provider (cost at 40,000 deliveries a day, revisit above 500,000). |
| C13 | pass | `Consequences` names costs: asynchronous delivery no longer aligns with customer retry semantics, and a backlog delays every customer. |
| C14 | pass, with a stated limit | Every figure and service name is attributed to the maintainers' brief of 2026-11-21, and `Context` says the repository holds no data proving them. Nothing is presented as repository-verified. |
| C15 | pass | Title, the three `Decision` rules and `Consequences` all speak to one choice: delivery moves to the queue. |
| C16 | pass | No `## Open questions`; the interview left no unknown that bears on the decision. |
| C17 | pass | Only the four core sections. No optional section was added. |
| C18 | pass | The directory held no records before this one, so no other record decides this question and nothing was amended or superseded. |
| C19 | pass | Hard to reverse (delivery path and worker model change), surprising without context (why the response returns before the send), real trade-off (two alternatives lost for stated reasons). |
| C20 | pass | The C20 grep found nothing: no checklist, status/progress section or in-flight wording. Both delivery tickets are named in `Refs:`; the already-open retry-budget ticket appears only as prose in `Context`, since it is not part of this suite. |
| C21 | pass | `TASK-0002` and `TASK-0003` each resolve to one file in `docs/tickets/`, each carries `**Record:** ADR-0001`, and no ID repeats. |

## Interview assumptions

- **Author and Deciders.** The brief names "the notify maintainers" on 2026-11-21 and no individual, and the target is not a git repository, so both lines carry `notify maintainers`. If a named person should own the record, change those two lines.
- **Revisit by.** Set to `2027-05-21`, six months after the decision. The brief gives a traffic threshold (500,000 deliveries a day) rather than a date; the date is the review point and the threshold is restated in `Consequences`. Adjust the date if the team reviews on a different cadence.
