# Move outbound webhook delivery onto the Redis job queue

**Status:** proposed
**Date:** 2026-11-21
**Author:** notify maintainers
**Deciders:** notify maintainers
**Revisit by:** 2027-05-21
**Refs:** TASK-0002, TASK-0003

## Context

Outbound webhook delivery currently runs inside the HTTP request path of the `notify` service. A customer endpoint that reads slowly holds an HTTP worker for up to thirty seconds. Last month one customer's endpoint stopped reading altogether and the public API was down for eleven minutes.

The queue work cannot start from a clean base: a separate, already-open ticket caps the outbound sender at three retries per delivery with exponential backoff, and that retry budget is expected to land before the queue change.

All figures in this record (thirty seconds, eleven minutes, ten largest customers, three slower endpoints, 40,000 deliveries a day) come from the maintainers' brief of 2026-11-21. This repository holds no incident report, traffic sample or customer latency data that would prove them.

## Decision

1. Outbound webhook delivery moves off the HTTP request path and onto the existing Redis-backed job queue.
2. The API responds once the delivery is enqueued; sending, timeout handling and retry accounting belong to the queue worker.
3. After cutover the inline delivery path is removed, not kept behind a flag as a second route.

## Considered options

- **Keep delivery inline and drop the timeout to two seconds.** Rejected: a two-second timeout drops deliveries to every endpoint slower than two seconds, and three of the ten largest customers are slower than that.
- **Switch to a managed webhook provider.** Rejected on cost at the current volume of about 40,000 deliveries a day. The option is worth reopening above 500,000 deliveries a day.

## Consequences

- Delivery is asynchronous, so the API returns before the webhook is sent. The customer's own retry semantics no longer line up with our response codes, and that mismatch has to be documented for integrators.
- A queue backlog delays every customer, not just the slow one whose endpoint is misbehaving.
- The service takes on worker capacity and queue monitoring as part of its delivery guarantee.
- Revisit this record when traffic approaches 500,000 deliveries a day, since the managed-provider rejection rests on that figure.
