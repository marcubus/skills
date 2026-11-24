# Brief: search index for the `catalog` service

We are moving product search off the Postgres full-text index and onto the Meilisearch instance the data team already runs for internal search.

The trigger: last week's catalogue sync stalled for four hours because the GIN index rebuild competed with the nightly import for I/O, and search returned stale prices the whole time. The platform team decided on 2026-11-20 to move search out of Postgres.

Alternative considered and rejected: keep Postgres and tune the index (smaller GIN pages, separate tablespace), rejected because the import and the rebuild still share the same disk budget and the stall recurs whenever the catalogue grows past the next threshold.

Alternative considered and rejected: buy a managed search service, rejected on cost at the current catalogue size; revisit if the catalogue passes five million rows.

Cost: search results can lag the catalogue by up to the indexing delay, about thirty seconds, and a Meilisearch outage means search is down rather than degraded.

Delivery is not implemented yet. It is tracked as CAT-812 (provision the Meilisearch index and indexes), CAT-813 (dual-write and backfill), and CAT-814 (drop the Postgres search path) in the team tracker. The decision also depends on ADR-0006, which put the catalogue import on its own queue.

Record this as an ADR.
