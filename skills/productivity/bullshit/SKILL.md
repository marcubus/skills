---
name: "bullshit"
description: "Bullshits an answer claim by claim — a verdict and its evidence for each — then re-audits its own annotations. Use when asked to fact-check one, or before relying on a claim-heavy reply of your own."
---

# Bullshit

Every assertion is bullshit until a quote from a fetched page says otherwise — and a quote is one you fetched this session, pasted verbatim. Memory, search snippets and inference reach `➖` at most. The work is finding which assertions fail; the failure is leaving one unexamined, or agreeing with the response because it is confidently written.

**Input**: one turn response — pasted, quoted, or the reply you just gave. With nothing named, take your own last turn.
**Output**, in the reply: one annotated reproduction of that response, a tally, and an audit line. The annotation is the artifact; save it as `reply` before the audit when you want the gate's shell route.

## Contents

- 1. Decompose
- 2. Flag
- 3. Verify
- 4. The bar
- 5. Annotate
- 6. Audit

## 1. Decompose

Read the response sentence by sentence and number every claim `C1`, `C2`, … in the order written. One proposition each: split conjunctions, split a sentence that asserts a fact and a cause — both lines factual — and keep a figure with its qualifier, the base, date and method a source gives it. Until step 3 supplies a qualifier, the figure stands alone and `⚠️` catches the gap.

Tag each line:

- **factual** — checkable against a source.
- **definitional** — true by convention ("HTTP 404 means not found").
- **opinion** — a judgment. It carries the word `opinion`, no verdict, and its factual load becomes its own numbered claim.

Factual and definitional lines carry the verdicts. A claim about what people believe or do is factual; a judgment about quality is an opinion. A response that is all opinion gets one line saying so — `no checkable claim` — and that is the finding.

**Done when** every sentence maps to a numbered line, with filler folded into the line it introduces, and the lines follow the response's order.

## 2. Flag

Read the numbered lines once for the shapes bullshit takes. A flag sets the suspicion level and the search order; the verdict comes from evidence.

- **Authority with no name**: "experts agree", "studies show", "industry standard".
- **Unsourced precision**: exact percentages, dates, version numbers, prices, sample sizes — and the round figures, "80% of", "10x faster".
- **Confidence doing evidence's work**: "clearly", "obviously", "definitely", "in fact".
- **Totalisers**: "never", "always", "the only", "no one", "every".
- **Named artifacts**: a paper, law, function, flag, API, benchmark, standard, quote.
- **Internal conflict**: two claims that cannot both hold, or one figure stated twice with different values.
- **Causation from correlation**: a "because" or "which is why" joining two facts that merely co-occur.
- **Quoted text**: a quote inside the response gets its wording and its attribution checked separately.

**Done when** every line carries one of these names or `clean`, written beside it for step 5's `Why`.

## 3. Verify

Search in **waves**: batch the lines whose searches are independent into one wave, then the next.

Search through `searxng-search`, which owns the endpoint and its categories. Fetch bodies with webfetch, `crawl` for JS-heavy pages, and the primary document where the fact lives. A snippet is a lead; quote from the body.

Per claim, climb this ladder and stop at the first rung that earns a verdict:

1. **Locate** — does the artifact exist? Search its name, the exact phrase, the registry, the changelog. Check the version and the date: a fact true in 2021 is a different claim in the present.
2. **Primary** — fetch the document that owns the fact.
3. **Quote** — grep that body for the span carrying the claim, ≤15 words, keeping its negation, condition and scope. A span cut before a "not" reads as its opposite; when the qualifier falls outside the window, quote the qualifier instead. A span you cannot find is a span that does not exist, whatever the page seemed to say.
4. **Counter** — search the strongest contradiction: the negation, the alternative spelling, the later version, the opposing figure.

**Counter by rule.** A claim whose own text carries a percentage, a rate, a multiple or a totaliser runs rung 4 even when an earlier rung earned a verdict; the trigger is the claim, never the flag you chose for it.

The budget is one query at rungs 1 and 2, two at rung 4, and rung 3 greps a body already fetched: four queries per claim. A specific claim whose four return nothing earns a fifth, and the `Why` says which four failed. Read results for **origins**, not results. Every `Why` that reports a search prints the query in backticks. Twenty claims is a comfortable reply; a longer one is annotated in waves, and the audit line states the count it covered.

**Done when** every factual and definitional line carries a quote, or a `Why` saying what was tried — in backticks wherever a search ran.

## 4. The bar

Every verdict names what settled it. These are the only admission rules.

| Verdict | Earned when |
|---|---|
| `✅ SUPPORTED` | A tier-1 quote establishes it outright, or two independent origins at tier ≤2 agree — and no credible source contradicts |
| `➗ CONTESTED` | Credible sources disagree. Both sides quoted, reported as the split it is |
| `⚠️ WEAK` | A fetched quote that falls short: one origin, tier 3, part of the claim, or the claim dropped its qualifier |
| `❌ BULLSHIT` | A tier ≤2 span says otherwise and no tier ≤2 source supports it; or the quote offered does not establish the claim (misquoted, out of context); or it meets the absence test below |
| `➖ UNVERIFIED` | The body sits behind a **wall**; the claim lies over a **horizon** — the future, the unobservable; or it is a **generality** too vague for absence to mean anything |

**Tiers.** 1 primary — the document itself: dataset, filing, spec, changelog, peer-reviewed paper, first-hand account. 2 reputable secondary — bylined press, disclosed-method analysis, regulator summary. 3 everything else — marketing, affiliate roundups, undated blogs, forums, summaries of unread documents. A vendor is tier 1 for what its product does, tier 2 at best for a benchmark it publishes, and tier 3 for its quality and its competitors: a self-published number needs an independent origin for `✅`.

**Origins.** Two pages share an origin when they report the same event, release, dataset or document. The domain changes nothing; the thing being reported decides. Three affiliate posts quoting one press release are one origin, and one origin cannot carry `✅`.

**Absence test.** `❌` on absence needs all four: the claim is specific; two counter-queries ran with different intents — the negation, and the registry or vendor that would own the fact; nothing turned up at any tier; and the `Why` prints both in backticks. A single fetched tier-3 page makes it `⚠️`.

**Definitions** earn `✅` from the one tier-1 document that states the convention; the origin count binds factual claims.

**Precedence.** Where two rows could apply, the verdict further from `✅` wins. Tier breaks the tie before the verdict does: a tier-1 document against a tier-2 summary is a settled `❌` or `✅`, and `➗` needs credible sources of comparable tier on both sides.

**Done when** every line carries the verdict its strongest applicable row admits.

## 5. Annotate

Write one line per numbered claim, then its quote and its reason. A real reply annotates every claim; the `…` below marks lines cut from this example:

```
C1 ✅ **SUPPORTED** · definitional — "HTTP 404 means Not Found"
> "origin server did not find a current representation for the target resource" — [RFC 9110](…), tier 1
Why: clean.

C4 ❌ **BULLSHIT** · factual — "the library handles 40k requests per second"
> "peak throughput on our benchmark hardware was 4,100 rps" — [Benchmarks](…), tier 1
Why: unsourced precision; off by an order of magnitude, and the 16-core qualifier the source carries is gone.

C5 ➖ **UNVERIFIED** · factual — "this is the approach most teams settle on"
Why: authority with no name; a generality, so absence carries nothing, and `searxng` finds no source stating it.

C6 · opinion — "the design will age well"

…
✅ 6 · ➗ 1 · ⚠️ 3 · ❌ 2 · ➖ 1 — 13 marked, 12 quoted · 2 opinions
```

A quote line appears under every `✅`, `➗` and `⚠️`, and under an `❌` whenever a source contradicts it. An absence `❌` carries its queries instead, in backticks. A `➖` carries only its `Why`, which names what was tried.

Follow the annotations with the tally: the five markers count marked lines, the quoted count counts quote lines, and opinions are counted apart, so marked plus opinions is the line count.

**Done when** every line follows the shape above and the tally follows the last claim.

## 6. Audit

Run every check in `GATE.md` against the reply, fix what fails, and rerun those checks. Read your annotations as someone else's: this is where a generous verdict gets caught.

Close the reply with the audit line — `<old>` is the verdict before this pass, and the annotation above shows `<new>`:

```
Self-audit: <marked lines> lines checked, <changed> changed — <id> <old>→<new> (check <n>, <reason>), …
```

**Done when** every check passes and that line ends the reply.

The machinery is `deep-research`'s evidence model cut down to one reply. When the job needs a report rather than an annotation, that skill carries the full version: cached bodies, hashes, and a coverage bar per section.
