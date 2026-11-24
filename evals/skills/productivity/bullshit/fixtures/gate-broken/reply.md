# Annotation: gate-broken

> agent: "The HTTP 404 status code means \"Not Found\"."

> "origin server did not find a current representation for the target resource" — [RFC 9110](…), tier 1

C1 ✅ **SUPPORTED** · definitional — agent: HTTP 404 means not found
Why: clean; RFC 9110 §15.5.5 states the convention.

> agent: "PostgreSQL 17 shipped in September 2024."

> "PostgreSQL 17 was released on September 26, 2024" — [PostgreSQL 17 release notes](…), tier 1

C2 ✅ **SUPPORTED** · claim — agent: PostgreSQL 17 shipped in September 2024
Why: clean.

> agent: "The Rust tokio runtime handles about 40,000 requests per second on a single core."

> "over 40,000 requests per second on the maintainer's benchmark hardware, measured with the project's own harness and no independent rerun" — [vendor benchmark](…), tier 3

C4 ⚠️ **WEAK** · claim — agent: tokio handles 40,000 requests per second on a single core
Why: unsourced precision; tier 3 only, and `tokio 40000 requests per second benchmark` and `tokio throughput single core` return no independent figure.

> agent: "Most teams eventually settle on tokio because it is the industry standard."

C5 🤷 **UNVERIFIED** · claim — agent: most teams settle on tokio
Why: authority with no name; no source states it, and `most teams settle on tokio` and `tokio adoption survey` return nothing.

> agent: "The tokio tutorial calls it the most widely used runtime."

> "the most widely used runtime, surpassing all other runtimes" — [tokio tutorial](…), tier 3

C6 ⚠️ **WEAK** · claim — agent: tokio is the most widely used async runtime
Why: unsourced precision; `tokio adoption share` returns one undated blog.

C7 — "tokio is the industry standard"

✅ 3 · ❓ 0 · ⚠️ 2 · ❌ 0 · 🤷 0 — 5 marked · 0 opinions

Self-audit: 6 lines checked, 2 changed — C4 ✅→⚠️ (check 10, no core count), C9 🤷→❌ (check 16, the quote does not establish it)

✅ 3 SUPPORTED · ⚠️ 2 WEAK — full annotations on request
