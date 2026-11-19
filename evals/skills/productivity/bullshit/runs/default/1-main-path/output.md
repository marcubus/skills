# Run: scenario 1, main path

Agent: general subagent, fresh context. Date: 2026-11-19, before the `§ 1` clarification that a claim about what people believe is factual. Result: pass, no question asked.

## Output

C1 ✅ **SUPPORTED** · definitional — "HTTP 404 means Not Found"
> "404 (Not Found) status code indicates that the origin server did not find" — [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html), tier 1
Why: clean.

C2 ✅ **SUPPORTED** · factual — "PostgreSQL 17 shipped in September 2024"
> "Posted on 2024-09-26 by PostgreSQL Global Development Group" — [PostgreSQL 17 Released!](https://www.postgresql.org/about/news/postgresql-17-released-2936/), tier 1
Why: clean; the release announcement's own dateline is the only date it gives, so the month matches without a qualifier.

C3 ❌ **BULLSHIT** · factual — "tokio handles about 40,000 requests per second on a single core"
Why: unsourced precision; `tokio requests per second single core benchmark` turned up only a 2017 forum run at 55k req/s on one thread and a 2017 tokio-proto issue at ~170k RPCs/s per core, neither of them tokio's own measurement of this figure, and `"40,000 requests per second" tokio` returned only unrelated Django and nginx posts — nothing at any tier states 40k for tokio.

C4 ❌ **BULLSHIT** · factual — "the official tokio documentation says tokio is the fastest async runtime in existence"
Why: quoted text; the attribution fails. `"tokio is the fastest async runtime in existence"` returns zero results, `tokio fastest async runtime site:tokio.rs` returns only "most widely used runtime", and the fetched docs.rs tokio page (31 KB) contains no occurrence of "fastest".

C5 ⚠️ **WEAK** · factual — "tokio is the fastest async runtime in existence"
> "A runtime for writing reliable network applications without compromising speed" — [docs.rs tokio](https://docs.rs/tokio/latest/tokio/), tier 3
Why: totalisers; the vendor's own description claims speed, never a superlative, and rung-4 `fastest rust async runtime benchmark comparison tokio glommio` reaches only tier-3 comparisons, one of which gives the throughput lead to glommio.

C6 ⚠️ **WEAK** · factual — "most teams eventually settle on tokio"
> "The Tokio library is the most widely used runtime, surpassing all other runtimes" — [Tokio tutorial](https://tokio.rs/tokio/tutorial), tier 3
Why: totalisers; the usage share is the vendor's own claim with no dataset or date behind it, and rung-4 `rust async runtime adoption survey percentage tokio async-std 2025` reaches only a tier-3 blog putting "about 42%" of new backend Rust projects on tokio — short of most, and still short of teams "eventually" settling.

C7 ⚠️ **WEAK** · factual — "teams settle on tokio because it is the industry standard"
> "Tokio is the industry standard with broader ecosystem support, better performance" — [generalistprogrammer](https://generalistprogrammer.com/comparisons/tokio-vs-async-std), tier 3
Why: causation from correlation; an undated comparison page supplies the label, and no source measures "standard" status causing adoption.

✅ 2 · ➗ 0 · ⚠️ 3 · ❌ 2 · ➖ 0 — 7 marked, 5 quoted · 0 opinions

Self-audit: 7 fact checks, 2 changed — C4 ✅→❌ (check 16, the quote attributed to the tokio docs appears nowhere in them), C5 ❌→⚠️ (check 18, no tier-≤2 contradiction exists; only the vendor's "fast" claim, which falls short)

Question asked: no

## Against the expectations

| Expectation | Pass |
|---|---|
| every sentence appears, numbered, in order | yes |
| the 404 claim `✅` on a tier-1 quote | yes, RFC 9110 |
| the PostgreSQL claim `✅` naming September 2024 | yes, the release dateline |
| the 40,000 rps claim never `✅` | yes, `❌` with two backticked queries |
| the fabricated quote `❌` with searches named | yes, three queries, one a zero-result exact phrase |
| the consensus claim never `✅` | yes, `⚠️` — and "industry standard" treated as factual rather than opinion, which the `§ 1` clarification now settles |
| tally arithmetic matches the markers | yes, 2+0+3+2+0 = 7, five quote lines |
| audit line closes the reply | yes, and both changes reconcile with the annotation |
| asks no question | yes |

## Note

The run predates two edits: `§ 1` now says a claim about what people believe or do is factual, which is the classification it chose for C7; and the audit line template now reads "lines checked" rather than "fact checks". Neither changes a verdict.
