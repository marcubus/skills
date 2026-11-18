# Brief: the cache moves to Redis

The `ledger` cache decision has changed. Two CLI runs at once now contend on the `ledger_cache` table, and the row lock serialises a 3-second rebuild behind a 40-second one. The reporting notebook also reads the table, so a rebuild blocks a report.

We are moving the cache to Redis, which the workstation also runs, because a key per month removes the contention entirely and lets the notebook read a month while another is rebuilt.

The Postgres table is dropped in the same change. The fallback to the 40-second rebuild stays.

Write the record.
