# Move product search from Postgres to Meilisearch

**Status:** proposed
**Date:** 2026-11-20
**Author:** Platform team
**Revisit by:** 2027-05-20
**Refs:** CAT-812, CAT-813, CAT-814

## Context

Product search for the `catalog` service is served today by a Postgres full-text index. Last week's catalogue sync stalled for four hours: the GIN index rebuild competed with the nightly import for I/O, and search returned stale prices for the whole stall. The platform team decided on 2026-11-20 that search moves out of Postgres.

The evidence for the stall and its duration is the platform team's brief of 2026-11-20 and the sync incident it reports. Neither the incident report nor a monitoring export has been supplied, and this repository holds no record of it, so the figures rest on that account alone.

The data team already runs a Meilisearch instance for internal search. The catalogue itself stays in Postgres and remains the system of record; only the search index moves.

## Decision

1. Product search for the `catalog` service is served by the data team's Meilisearch instance, not by the Postgres full-text index.
2. Postgres remains the system of record for the catalogue, and the Meilisearch index is derived from it and rebuildable from it.
3. Indexing is asynchronous, and a delay of up to about thirty seconds between a catalogue write and its visibility in search is accepted.
4. Catalogue writes never block on the search index; an indexing failure is retried without failing the write.
5. A Meilisearch outage takes search down rather than degrading it, and the rest of the `catalog` service stays up.
6. The Postgres search path is removed only after dual-write and backfill have completed, as CAT-813 and CAT-814 sequence it.
7. The choice is revisited when the catalogue passes five million rows, or at the revisit date, whichever comes first.

## Considered options

- **Meilisearch, chosen.** It is already operated by the data team, so it adds no new vendor and keeps the index off the catalogue's disk budget.
- **Keep Postgres and tune the index.** Rejected: smaller GIN pages and a separate tablespace still draw on the same disk budget as the nightly import, so the stall recurs at the next catalogue growth threshold.
- **Buy a managed search service.** Rejected on cost at the current catalogue size; it is the option to reopen if the catalogue passes five million rows.

## Consequences

- Search results can lag the catalogue by up to the indexing delay, about thirty seconds, so a price change is briefly invisible to search.
- A Meilisearch outage now takes search down completely, where a slow Postgres search degraded instead.
- Search depends on a service owned by another team, so its capacity and availability become a cross-team commitment that this decision does not itself secure.
- Until CAT-814 lands, the service carries dual writes and two search paths, which is more moving parts than either endpoint alone.

## Open questions

- Which team owns the shared Meilisearch instance's capacity and on-call for product-search load is not settled. The answer changes who operates search, not whether Meilisearch serves it.
