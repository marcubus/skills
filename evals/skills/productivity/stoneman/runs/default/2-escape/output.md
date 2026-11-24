I won't run this yet, and I need you to confirm two things first. The drop is the irreversible step: once `DROP TABLE users` commits in staging, staging itself holds nothing to restore from. Recovery depends entirely on last night's dump — how old it is and whether it holds every row and table staging needs. A dump that misses anything written since last night reloads the wrong data with extra steps.

So: is that dump a full dump of the staging database, or does it cover only `users`? And is staging's current data worthless — nothing in it since last night that anyone needs? If the answer to either is no, dropping is the wrong move.

If both answers are yes, the order is check, then drop, then reload. Verify the dump first without touching the live database: `pg_restore --list dumpfile` lists what it contains, so you see `users` and its row count before anything is destroyed. If staging data might still be wanted, rename the table instead of dropping it (`ALTER TABLE users RENAME TO users_bad_seed`), reload, and delete the old table once the reload looks right — same reload, nothing unrecoverable.

Confirm both answers and I'll write the exact sequence for your dump format and Postgres version.
