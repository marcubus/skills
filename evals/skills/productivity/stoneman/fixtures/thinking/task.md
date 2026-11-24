# Task

We run the app with 4 Gunicorn workers on a 4-core VM. The database is SQLite in WAL mode, and writes are serialized by the writer lock. Throughput is flat at about 90 requests per second. Someone proposed raising the worker count to 16. Will that raise throughput? Do not change the journal mode; we need WAL for the readers.
