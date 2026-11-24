Idle connections count. `max_connections` counts every backend in `pg_stat_activity`, idle included; pool metrics count clients checked out of the pool. The pool is not leaking, and the two numbers measure different things.

What eats the connections, in likelihood order:

1. **Pool per worker process, not per replica.** Gunicorn/uvicorn cluster mode, Node cluster, several JVMs in one container: each worker process builds its own pool of 20. 3 replicas × 4 worker processes × 20 = 240 against 100. Each pool reports around 20 in use per replica; the server sees the sum.
2. **Idle pool members.** Most pools open toward `minIdle`/`max` and hold the connection after release. 3 replicas × 20 = 60 idle-at-rest floor, before any other client connects.
3. **Clients outside the pools.** `superuser_reserved_connections` (default 3), autovacuum workers (`autovacuum_max_workers`, default 3), postgres_exporter, `pg_dump` backups, migration jobs, walsenders, `psql` sessions, health checks that open a fresh connection per probe.
4. **Connection storm.** Replicas restart or traffic spikes, every pool opens toward `max` at once, the server refuses before any client backs off.

Who holds them:

```sql
SELECT application_name, client_addr, state, count(*)
FROM pg_stat_activity
GROUP BY 1, 2, 3
ORDER BY 4 DESC;
```

One `application_name` per worker process shows whether one replica holds many sessions. `state = 'idle'` is a held connection all the same.

Sizing:

```
usable   = max_connections - superuser_reserved_connections - admin headroom
pool_max = floor(usable / (replicas × worker_processes))
```

With `max_connections` 100, reserve 10 for monitoring, backup, migrations, autovacuum: usable 90. 3 replicas × 4 worker processes = 12 pools, so 7 per pool, rounded down.

If 7 per pool starves the app, put PgBouncer in transaction mode in front: app pools stay small, PgBouncer holds ~20–25 server connections for all 12 worker processes, `max_connections` untouched.

Then set `minIdle` low, `idleTimeout` on, `connectionTimeout` short so a refusal fails fast instead of queueing. Raising `max_connections` last: each backend costs memory and adds contention, and 100 → 200 does not fix a per-worker-process multiplication.

How many worker processes does each replica run? That is the divisor, and the 20 in the metrics is per pool, not per replica.
