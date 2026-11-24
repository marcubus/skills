No. SQLite writer lock serializes writes, so 16 workers add contention, not throughput. Flat at ~90 req/s on 4 cores, 4 workers. More workers = more processes blocked on the same writer lock. WAL stays: readers unaffected, writes still one at a time.

Raise throughput only off the write path: batch writes, shorten write transactions, or move writes to one dedicated writer process with a queue. Verify with a load test before assuming the lock is the ceiling — check if CPU is idle at 90 req/s.
