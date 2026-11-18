# Reply — ADR write (scenario 1)

**Path:** `docs/adr/0001-cache-parsed-transactions-in-sqlite.md`
**Status:** `proposed`
**Title:** Cache parsed ledger transactions in a single SQLite file

Gate: C1–C6, C9–C18 pass. C7 not applicable (no `docs/adr/README.md` in the repo). C8 not applicable (record is `proposed`; no implementation in the repo to read).

Decided by me, not by the brief: I added "keep rebuilding from CSV on every run" as a third considered option (the brief named only two candidates) so the options section carries the status quo's rejection reason, and I recorded `Author` as the repository git user `marcubus` because the brief names no author — both are flagged under `## Open questions`.
