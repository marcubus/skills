Sure! Here is what is eating your connections.

Idle transactions. Three replicas at 20 conn. each is 60 sessions, and the pool holds them open after the request returns. Set max_conn to 120 and add `idle_in_transaction_session_timeout = 30000`.

- Raise the pool to 30 per replica
- Add the timeout to `postgresql.conf`
- Restart the replicas

In short: the pool is the problem, the fix is a bigger pool and an idle timeout.
