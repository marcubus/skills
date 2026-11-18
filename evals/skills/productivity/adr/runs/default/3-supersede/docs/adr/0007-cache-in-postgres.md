# Keep the parsed-transaction cache in Postgres

**Status:** superseded by ADR-0008
**Date:** 2026-09-02
**Author:** sys-admin
**Implemented:** 2026-09-04

## Context

The `ledger` CLI rebuilds its monthly summary from CSV exports on every run, and that takes about 40 seconds on a 12-month history. The workstation already runs a Postgres instance for the reporting notebook, and it is up whenever the CLI is used.

The trigger was a user report of the 40-second rebuild happening twice in one session, once per command.

## Decision

1. Parsed transactions are cached in a `ledger_cache` table in the existing Postgres instance.
2. The table carries a `schema_version` column, and a version mismatch drops and rebuilds it.
3. The cache is derived data. Deleting the table costs one rebuild and nothing else.

## Considered options

- **A SQLite file beside the exports.** Rejected: it would be a second database engine to install and back up on the same machine that already runs Postgres.
- **A directory of JSON files keyed by month.** Rejected: range queries across months become a directory walk, and partial writes leave half a month behind.

## Consequences

- The CLI now depends on Postgres being reachable, so a run without it falls back to the 40-second rebuild rather than failing.
- The cache is shared state: two CLI runs at once contend on the same table, so writes take a row lock.
- Backups of the reporting database now include derived data that can be regenerated.

## Implementation

- `ledger/cache.py`: the `ledger_cache` table, the schema-version check and the rebuild path.
- `ledger/cli.py`: the fallback when Postgres is unreachable.
- Verified with `python -m ledger --rebuild-cache` on a 12-month history, which drops and repopulates the table in 3.1 s.
