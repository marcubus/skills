# Annotation: gate-clean

> agent: "The HTTP 404 status code means \"Not Found\"."

> "origin server did not find a current representation for the target resource" — [RFC 9110](…), tier 1

C1 ✅ **SUPPORTED** · definitional — agent: HTTP 404 means not found
Why: clean; RFC 9110 §15.5.5 states the convention.

> agent: "PostgreSQL 17 shipped in September 2024."

> "PostgreSQL 17 was released on September 26, 2024" — [PostgreSQL 17 release notes](…), tier 1

C2 ✅ **SUPPORTED** · claim — agent: PostgreSQL 17 shipped in September 2024
Why: clean; the release announcement's own dateline is the only date it gives.

> agent: "The Rust tokio runtime handles about 40,000 requests per second on a single core."

> "over 40,000 requests per second on the maintainer's benchmark hardware" — [vendor benchmark](…), tier 3

C3 ⚠️ **WEAK** · claim — agent: tokio handles 40,000 requests per second on a single core
Why: unsourced precision; tier 3 only, and the hardware is the vendor's own, so `tokio 40000 requests per second benchmark` and `tokio throughput single core` return no independent figure.

> agent: "As the official tokio documentation says, \"tokio is the fastest async runtime in existence\"."

C4 ❌ **BULLSHIT** · claim — agent: the official tokio documentation calls tokio the fastest async runtime in existence
Why: quoted text; no tokio document carries that span. Searched `tokio is the fastest async runtime in existence` and `site:docs.rs tokio fastest`; nothing at any tier.

> agent: "Most teams eventually settle on tokio because it is the industry standard."

C5 🤷 **UNVERIFIED** · claim — agent: most teams settle on tokio
Why: authority with no name; generality — absence carries nothing, and `most teams settle on tokio` and `tokio adoption survey` return no source stating it.

C6 · opinion — agent: tokio is the industry standard

✅ 2 · ❓ 0 · ⚠️ 1 · ❌ 1 · 🤷 1 — 5 marked · 1 opinion

Self-audit: 5 lines checked, 1 changed — C3 ✅→⚠️ (check 10, the quote states no core count)

✅ 2 SUPPORTED · ⚠️ 1 WEAK — full annotations on request
