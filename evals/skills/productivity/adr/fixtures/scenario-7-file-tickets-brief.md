# Brief: outbound webhook delivery for the `notify` service

Our repo keeps its work as files under `docs/tickets/`; there is no external tracker and no wiki. `TASK-0001-add-retry-budget.md` is already open.

We are moving outbound webhook delivery from the request path onto the existing Redis-backed job queue, because a slow customer endpoint currently holds an HTTP worker for up to thirty seconds and last month's incident took the public API down for eleven minutes when one customer's endpoint stopped reading.

The decision was made by the notify maintainers on 2026-11-21.

Alternative considered and rejected: keep delivery inline and drop the timeout to two seconds. Rejected because a two-second timeout drops deliveries to every endpoint slower than that, and three of our ten largest customers are slower.

Alternative considered and rejected: switch to a managed webhook provider. Rejected on cost at the current volume of about 40,000 deliveries a day; revisit above 500,000 a day.

Cost: delivery is now asynchronous, so the API returns before the webhook is sent and the customer's retry semantics no longer line up with our response codes. Also a queue backlog delays every customer, not just the slow one.

The change is not implemented. Delivery needs two tickets: one to add the topic and the publisher, one to cut the API over and remove the inline path. Both are new work, so open them.

Record this as an ADR.
