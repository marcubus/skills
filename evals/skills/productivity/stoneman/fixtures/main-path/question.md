# Question

We run three replicas of the API behind the load balancer. Each has a Postgres pool of 20 connections and `max_connections` is 100. Under load we get `FATAL: sorry, too many clients already`, but the pool metrics show around 20 in use per replica. The pool is not leaking, we checked. What is eating the connections, and how should we size the pool?
