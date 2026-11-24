# Convert timestamps to UTC at the service boundary

**Status:** proposed
**Date:** 2026-11-19
**Author:** marcus

## Context

An ordering bug in the settlement ledger forced this decision: two regions disagreed about the order of the same events by up to five hours, because timestamps from untrusted clients arrived in local time and were stored as sent. The service is a single-service monorepo, and its work is tracked in commit messages, so no ticket accompanies this record. The two maintainers made the decision on 2026-11-19.

## Decision

1. Every event that enters the service through the HTTP or queue boundary is converted to UTC before it is stored.
2. Stored event timestamps are UTC values; an event that already carries UTC is stored unchanged.
3. The sender's local time and offset are not stored with the event.

## Considered options

- **Convert at read time in each consumer.** Rejected because four consumers already exist, and each would need the same conversion plus the sender's locale, which is not stored.
- **Store the sender's offset beside every timestamp.** Rejected because it doubles the index width on the events table, and only two of the four consumers need the offset.

## Consequences

- Historical rows keep their local-time values, so queries that span the cutover need a date-aware filter until the backfill lands.
- Events written after the cutover order consistently across regions, which removes the five-hour disagreement at the write path (reported by the maintainers in the request for this record, 2026-11-24).
- Every ingress path must apply the conversion, so the HTTP and queue boundaries now share one rule rather than leaving each consumer to interpret timestamps.
