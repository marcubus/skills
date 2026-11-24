# Brief: timestamps at the edge

This repository is a single-service monorepo with no issue tracker, no wiki, and no `docs/tickets/`. Work is tracked in commit messages.

We are standardising on UTC at the edge: every event that enters the service through the HTTP or queue boundary is converted to UTC before it is stored. Timestamps from untrusted clients previously arrived in local time and were stored as sent, so two regions disagreed about ordering by up to five hours.

The decision was made by the two maintainers on 2026-11-19 after the ordering bug in the settlement ledger.

Alternative considered and rejected: convert at read time in each consumer. Rejected because four consumers already exist and each would need the same conversion plus the sender's locale, which is not stored.

Alternative considered and rejected: store the sender's offset beside every timestamp. Rejected because it doubles the index width on the events table and only two of the four consumers need the offset.

Cost: historical rows keep their local-time values, so queries spanning the cutover need a date-aware filter until the backfill lands.

The change is not implemented. No ticket exists for it, and none is planned until the next release window.

Record this as an ADR.
