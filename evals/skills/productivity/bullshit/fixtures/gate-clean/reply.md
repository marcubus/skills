C1 ✅ **SUPPORTED** · definitional — "HTTP 404 means Not Found"
> "origin server did not find a current representation for the target resource" — [RFC 9110](…), tier 1
Why: clean; a definitional claim earns the marker from the one document that states the convention.

C2 ✅ **SUPPORTED** · factual — "PostgreSQL 17 shipped in September 2024"
> "PostgreSQL 17 was released on September 26, 2024" — [PostgreSQL 17 release notes](…), tier 1
Why: clean.

C3 ⚠️ **WEAK** · factual — "tokio handles 40,000 requests per second on one core"
> "over 40,000 requests per second" — [vendor benchmark](…), tier 3
Why: unsourced precision; tier 3 only, and the figure's base and hardware are unstated. Rung 4 ran `tokio 40000 requests per second benchmark` and `tokio throughput single core`, neither of which returns the figure.

C4 ❌ **BULLSHIT** · factual — "the tokio docs call it the fastest async runtime in existence"
Why: quoted text; no tokio document carries that span. Searched `tokio is the fastest async runtime in existence`, `site:docs.rs tokio fastest`, and the tokio README; nothing at any tier.

C5 ➖ **UNVERIFIED** · factual — "most teams settle on tokio"
Why: authority with no name, causation from correlation; a generality, so absence carries nothing, and no source states it.

C6 · opinion — "tokio is the industry standard"

✅ 2 · ➗ 0 · ⚠️ 1 · ❌ 1 · ➖ 1 — 5 claims, 3 quoted · 1 opinion

Self-audit: 5 fact checks, 1 changed — C3 ✅→⚠️ (check 9, one tier-3 origin).
