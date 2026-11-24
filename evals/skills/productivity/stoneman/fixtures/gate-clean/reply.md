Not a pool leak. Three replicas at pool 20 is 60 checked-out sockets, and each socket pins a backend. `max_connections` 100 leaves 40 for admin, migrations, monitoring, and replication, and a fourth client class takes the last of them. Postgres then answers `FATAL: sorry, too many clients already`.

Check `pg_stat_activity` grouped by `application_name` for the class you did not count.

Sizing: 10 per replica is 30, leaving 70 of the 100 spare. Or one pgbouncer in transaction mode with a pool of 20.
