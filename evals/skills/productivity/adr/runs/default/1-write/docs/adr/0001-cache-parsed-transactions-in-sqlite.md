# Cache parsed ledger transactions in a single SQLite file

**Status:** proposed
**Date:** 2026-11-18
**Author:** marcubus

## Context

`ledger` is a single-user Python 3.12 command-line tool, distributed as a wheel, that reads bank exports and writes a monthly summary. It runs on one laptop with no always-on service and no server, so a cache cannot live in a daemon or in a database server.

Today every run rebuilds the summary from the CSV exports, which takes about 40 seconds against a 12-month history, and the exports are re-downloaded by hand. The rebuild is now the dominant cost of a run and grows with the length of the history, which is what forced a decision on where parsed transactions are kept between runs.

The cache is derived data: deleting it costs one rebuild and nothing else. This record decides the storage format only; how the exports are obtained stays out of scope. Every fact about the tool and its timings here is taken from the decision brief for this change, `scenario-1-decision-brief.md`, which records the author's own runs on their laptop.

## Decision

1. `ledger` keeps a local cache of parsed transactions in a single SQLite file stored next to the CSV exports.
2. The cache is derived data: a missing, unreadable or version-mismatched cache file is discarded and rebuilt from the exports, and deleting the file by hand loses nothing but the rebuild.
3. The cache carries a schema version column, and a file whose version does not match the version the running wheel expects is discarded and rebuilt rather than migrated.

## Considered options

- **A single SQLite file next to the exports — chosen.** One file is easier to back up and easier to delete than a tree of files, and the cache is queried with per-month range scans, which SQLite answers directly.
- **A directory of JSON files keyed by month — rejected.** Backing up or deleting the cache becomes a directory walk, and each per-month range scan becomes opening and parsing the files that span the range. It buys human-readable cache contents, which the decision does not need because the cache can always be rebuilt from the exports.
- **Keep rebuilding from the CSV exports on every run — rejected.** This is today's behaviour and it pays the 40-second parse on every run; the whole point of the change is to pay it once per export refresh.

## Consequences

- A warm cache skips the parse, so the 40-second cost is paid only on a cold cache or after an invalidation.
- Cost: the cache file is an ordinary file a user can edit by hand and corrupt. That is the reason Decision rules 2 and 3 exist, and both are code and tests that would not be needed if the cache could not be touched.
- Cost: the cache is a binary file, so a user cannot read it with the same tools they use on the JSON exports; inspecting it needs `sqlite3` or an equivalent.
- Because the cache is disposable, no backup or migration path is owed for it: a corrupt or outdated file is deleted and rebuilt.

## Open questions

- How a run decides the cache is stale relative to the exports — file mtime, a content hash, or an explicit refresh flag — is not settled. It does not change the storage choice, since either candidate needs the same rule.
- The exact filename and directory of the cache file, beyond "next to the exports", is not pinned down.
- The brief names no author; the `Author` line records the repository git user, `marcubus`.
