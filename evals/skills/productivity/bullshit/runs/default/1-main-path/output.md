# Run: scenario 1, main path

Agent: general subagent, fresh context. Date: 2026-11-24. Result: pass, no question asked.

## Output

> agent: "As the official tokio documentation says, … "tokio is the fastest async runtime in existence"."

> "A runtime for writing reliable network applications without compromising speed." — [tokio crate documentation](https://docs.rs/tokio/latest/tokio/), tier 1

C4 ❌ **BULLSHIT** · claim — agent: the official tokio documentation contains the sentence calling tokio the fastest async runtime in existence
Why: quoted text; the exact phrase returns nothing (`"tokio is the fastest async runtime in existence"`), `tokio.rs documentation "fastest" async runtime superlative claim` finds no such sentence in the docs or a tier ≤2 report of it, and the fetched crate documentation describes speed without a ranking or superlative, so the attribution is invented.

> agent: "As the official tokio documentation says, …"

C5 ❌ **BULLSHIT** · claim — agent: tokio is the fastest async runtime in existence
Why: totalisers; no fetched benchmark ranks tokio first and the documentation offered as the source makes no comparative claim — `fastest async runtime Rust benchmark comparison glommio tokio monoio ranking` and `"fastest async runtime" Rust tokio claim debunked` turn up no ranking naming tokio fastest at any tier, so the absence test is met.

> agent: "The Rust tokio runtime handles about 40,000 requests per second on a single core."

C3 ❌ **BULLSHIT** · claim — agent: tokio sustains about 40,000 requests per second on a single core
Why: unsourced precision; no tokio document, changelog or published benchmark states a single-core throughput figure, and nothing at any tier carries this number — `tokio official benchmark throughput requests per second single core async runtime comparison` and `tokio slower than 40,000 requests per second single threaded runtime overhead` both return without it, so the absence test is met.

> agent: "Most teams eventually settle on tokio because it is the industry standard."

C6 🤷 **UNVERIFIED** · claim — agent: most teams eventually settle on tokio
Why: authority with no name; generality — no population, timeframe or measure is given, so absence carries nothing, and `most teams eventually settle on tokio` and `Rust survey async runtime usage tokio percentage most used 2024` find no fetched survey that counts teams settling.

C7 · opinion — agent: tokio is the industry standard

> agent: "The HTTP 404 status code means "Not Found"."

> "404 (Not Found) status code indicates that the origin server did not find" — [RFC 9110 · HTTP Semantics, §15.5.5](https://www.rfc-editor.org/rfc/rfc9110.html#name-404-not-found), tier 1

C1 ✅ **SUPPORTED** · definitional — agent: RFC 9110 defines HTTP 404 as Not Found
Why: clean; section 15.5.5 of RFC 9110 names the code 404 (Not Found) and defines it as the origin server not finding a current representation for the target resource.

> agent: "PostgreSQL 17 shipped in September 2024."

> "The PostgreSQL Global Development Group today announced the release of PostgreSQL 17" … "2024-09-26" — [PostgreSQL 17 Released!](https://www.postgresql.org/about/news/postgresql-17-released-2936/), tier 1

C2 ✅ **SUPPORTED** · claim — agent: PostgreSQL 17 was released in September 2024
Why: clean; the project's own release announcement says it announced the release of PostgreSQL 17 and is dated 2024-09-26, and the 17 release notes repeat that date.

✅ 2 · ❓ 0 · ⚠️ 0 · ❌ 3 · 🤷 1 — 6 marked · 1 opinion

Self-audit: 6 lines checked, 1 changed — C5 ⚠️→❌ (check 16, the documentation quote says fast, not fastest, and does not rank tokio)

✅ 2 SUPPORTED · ⚠️ 0 WEAK — full annotations above

## Against the expectations

| Expectation | Pass |
|---|---|
| every sentence appears, numbered, in order | yes: C1 to C7 |
| the 404 claim carries `✅` and a tier-1 quote naming RFC 9110 | yes: C1 |
| the PostgreSQL claim carries `✅` and a September 2024 quote | yes: C2 |
| the 40,000 rps claim is never `✅` and names its searches | yes: C3 `❌`, two queries |
| the "fastest async runtime" claim carries `❌` with the searches named | yes: C4 and C5 |
| the consensus claim is never `✅` | yes: C6 `🤷` on `generality` |
| "industry standard" appears as an opinion line with no marker | yes: C7 |
| tally arithmetic matches the markers | yes: 2+0+0+3+1 = 6 marked, 1 opinion, 7 lines |
| the audit line is second to last, the counts line last | yes |
| no question to the user | yes |

## Note

Two earlier runs of this scenario failed the opinion expectation: both carried "it is the industry standard" as a weak claim, not an opinion. The skill did not state the rule; `SKILL.md` § 1 now says a status judgment is an opinion unless a named survey, registry or body declares it. The output above is the run after that fix.
