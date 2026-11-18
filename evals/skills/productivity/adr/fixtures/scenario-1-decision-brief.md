# Brief: state storage for the `ledger` CLI

`ledger` is a single-user command-line tool that reads bank exports and writes a monthly summary. It runs on one laptop.

Today every run rebuilds the summary from the CSV exports, which takes about 40 seconds on a 12-month history. The exports are re-downloaded by hand.

We have decided to keep a local cache of parsed transactions between runs. The cache is derived data: deleting it costs one rebuild and nothing else.

Facts:

- The tool is Python 3.12, distributed as a wheel, no daemon.
- The laptop has no always-on service and no server.
- Two candidates were considered: a SQLite file next to the exports, and a directory of JSON files keyed by month.
- SQLite won because a single file is easier to back up and to delete, and because the queries are per-month range scans.
- The cost: the cache file becomes a thing users can corrupt by editing it by hand, so it needs a version column and a rebuild path.
- The repository has no `docs/adr` directory yet.

Write the record.
