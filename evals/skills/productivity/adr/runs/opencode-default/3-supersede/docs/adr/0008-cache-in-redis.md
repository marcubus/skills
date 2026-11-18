# Move the parsed-transaction cache to Redis

**Status:** proposed
**Date:** 2026-11-18
**Author:** sys-admin
**Refs:** ADR-0007

This record replaces [ADR-0007](0007-cache-in-postgres.md). It decides where the `ledger` CLI caches parsed transactions, and nothing about how the cache is populated.

## Context

ADR-0007 put the parsed-transaction cache in a `ledger_cache` table in the Postgres instance the reporting notebook already uses, and its Consequences named the cost it was accepting: the cache is shared state, so two CLI runs at once contend on the same table and writes take a row lock ([ADR-0007](0007-cache-in-postgres.md), Consequences).

That predicted cost has landed. Two CLI runs at once now contend on the `ledger_cache` table, and the row lock serialises a 3-second rebuild behind a 40-second one. The reporting notebook reads the same table, so a rebuild blocks a report until the rebuild's transaction commits (change brief, 2026-11-18).

The trigger is that contention and that blocked report. The 40-second rebuild that ADR-0007 measured on a 12-month history is unchanged and is still the fallback.

## Decision

1. Parsed transactions are cached in Redis, which the workstation already runs, under one key per month.
2. A key per month is the unit of rebuild and of read, so rebuilding one month holds no lock that another CLI run or the notebook needs.
3. The `ledger_cache` table is dropped in the same change that adds the Redis path.
4. The cache stays derived data: an unreachable Redis or an absent key falls back to the 40-second rebuild rather than failing the run.

## Considered options

- **Keep the `ledger_cache` table and narrow the lock to one month.** Rejected: the row lock is not the only serialisation. A month's rebuild deletes and reinserts its rows inside one transaction, so the notebook reading that month still waits for the commit, and two runs still meet on the same table.
- **A directory of JSON files keyed by month, beside the exports.** Rejected: ADR-0007 rejected it for a directory walk across months and for half-written months; a key per month removes the walk but not the partial write, which a single-key Redis write does not have.
- **Keep Postgres and give the notebook a read replica.** Rejected: it adds a second Postgres instance to run, patch and back up on the workstation, for derived data that can be regenerated from the exports.

## Consequences

- The CLI now depends on Redis as well as Postgres. A run with Redis down pays the 40-second rebuild, where the Postgres path degraded one table at a time; a Redis outage degrades every month at once.
- The cache leaves the reporting database's backups. A Redis flush or eviction costs a rebuild of every month, not of one, and the database backup no longer carries derived data that could be restored for free.
- The notebook's read path changes from a SQL query against `ledger_cache` to a key read per month, so a change to the notebook ships with this one.
- A month-keyed cache gives up range queries: reading a 12-month summary is twelve key reads rather than one query.

## Open questions

- Whether the change has landed. The brief says the table is dropped in the same change, but this repository holds no `ledger` code, so the record stays `proposed` until a diff exists.
- No key expiry or eviction policy is stated. Whether Redis is configured to evict these keys under memory pressure is unrecorded; an evicted key costs a rebuild, not a wrong answer, so the decision does not turn on it.
