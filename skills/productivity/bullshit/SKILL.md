---
name: "bullshit"
description: "Bullshits an answer claim by claim — a verdict and its evidence for each, failures first, then re-audits its own annotations. Use when asked to fact-check one, or before relying on a claim-heavy reply of your own."
---

# Bullshit

Every assertion is bullshit until a quote from a fetched page says otherwise. A quote is one you fetched this session and pasted verbatim. Memory, search snippets, and inference reach `🤷` at most. The work is finding which assertions fail. The failure is leaving one unexamined or agreeing with the response because it is confidently written.

**Input**: one turn response — pasted, quoted, or the reply you just gave. With nothing named, take your own last turn.
**Output**, in the reply: the failed claims annotated and ordered, the warnings and the supported claims summarised as counts, a tally, and an audit line. The full annotation is the artifact. Save it as `reply` before the audit when you want the gate's shell route. The reply renders it.

## Contents

- 1. Decompose
- 2. Flag
- 3. Verify
- 4. The bar
- 5. Annotate and render
- 6. Audit

## 1. Decompose

Read the response sentence by sentence and number every claim `C1`, `C2`, … in the order written. One proposition each. Split conjunctions. Split a sentence that asserts a fact and a cause. Both are claims. Keep a figure with its qualifier, the base, date, and method a source gives it. A figure whose qualifier, base, date, or method the response leaves out is flagged at step 2 and settled at step 4.

Tag each line:

- **claim** — checkable against a source, and it names its author: `agent` for the response under test, `you` for the person it answers.
- **definitional** — true by convention. HTTP 404 means not found.
- **opinion** — a judgment. It carries the word `opinion`, no verdict, and its factual load becomes its own numbered claim. A status, quality, or competence judgment is itself the opinion, so it is not split again.

Claims and definitional lines carry the verdicts. A statement about what people believe or do is a claim. A judgment about quality is an opinion, and a judgment about a person's or a team's competence is one too. A status judgment is an opinion unless a named survey, registry, or body declares it. A response that is all opinion still numbers its lines, all tagged `opinion`, and its reply opens with `no checkable claim` above them, which is the finding.

**Done when** every sentence maps to a numbered line, with filler folded into the line it introduces, and the lines follow the response's order.

## 2. Flag

Read the numbered lines once for the shapes bullshit takes. A flag sets the suspicion level and the search order. The verdict comes from evidence.

- **Authority with no name** (`authority`): "experts agree", "studies show", "industry standard".
- **Unsourced precision** (`unsourced`): exact percentages, dates, version numbers, prices, sample sizes. And the round figures, "80% of", "10x faster".
- **Confidence doing evidence's work** (`confidence`): "clearly", "obviously", "definitely", "in fact".
- **Totalisers** (`totalisers`): "never", "always", "the only", "no one", "nobody", "none", "every", "most".
- **Named artifacts** (`named`): a paper, law, function, flag, API, benchmark, standard, quote.
- **Internal conflict** (`internal`): two claims that cannot both hold, or one figure stated twice with different values.
- **Causation from correlation** (`causation`): a "because" or "which is why" joining two facts that merely co-occur.
- **Quoted text** (`quoted`): a quote inside the response is two claims. The wording, and its attribution.

**Done when** every claim and definitional line carries one of these tokens or `clean`, written beside it for step 5's `Why`. An opinion line carries none.

## 3. Verify

Search in **waves**: batch the lines whose searches are independent into one wave, then the next.

Search through the agent's own search tool. Fetch bodies with webfetch, `crawl` for JS-heavy pages, and the primary document where the fact lives. A snippet is a lead. Quote from the body.

Per claim, climb this ladder and stop at the first rung that earns a verdict:

1. **Locate**. Does the artifact exist? Search its name, the exact phrase, the registry, the changelog. Check the version and the date. A fact true in 2021 is a different claim in the present.
2. **Primary**. Fetch the document that owns the fact.
3. **Quote**. Grep that body for the span carrying the claim, ≤15 words, keeping its negation, condition, and scope. A span cut before a "not" reads as its opposite. When the qualifier falls outside the window, quote the qualifier instead. A span you cannot find is a span that does not exist, whatever the page seemed to say.
4. **Counter**. Search the strongest contradiction: the negation, the alternative spelling, the later version, the opposing figure.

**Counter by rule.** A claim whose own text carries a percentage, a rate, a multiple or a totaliser runs rung 4 even when an earlier rung earned a verdict. The trigger is the claim, never the flag you chose for it.

The budget is one query at rungs 1 and 2, two at rung 4, and rung 3 greps a body already fetched: four queries per claim. A specific claim whose four return nothing earns a fifth, and the `Why` says which four failed. Read results for **origins**, not results. Every `Why` that reports a search prints the query in backticks. A comfortable reply runs in one pass. A longer one is annotated in waves, every claim still marked.

**Done when** every claim and definitional line carries a quote or a `Why` saying what was tried. In backticks wherever a search ran.

## 4. The bar

Every verdict names what settled it. These are the only admission rules.

| Verdict | Earned when |
|---|---|
| `✅ SUPPORTED` | A tier-1 quote establishes it outright, or two independent origins at tier ≤2 agree. No source of equal or higher tier contradicts. |
| `❓ CONTESTED` | Credible sources disagree. Both sides quoted, reported as the split it is. |
| `⚠️ WEAK` | A fetched quote that falls short: one origin, tier 3, part of the claim, the claim dropped its qualifier, or a higher tier supports it while a lower tier contradicts. |
| `❌ BULLSHIT` | A tier ≤2 span says otherwise and no tier ≤2 source supports it. Or the quote offered does not establish the claim (misquoted, out of context). Or it meets the absence test below. |
| `🤷 UNVERIFIED` | The body sits behind a **wall**. The claim lies over a **horizon**. The future, the unobservable. Or it is a **generality** too vague for absence to mean anything. |

**Tiers.** 1 primary. The document itself: dataset, filing, spec, changelog, peer-reviewed paper, first-hand account. 2 reputable secondary. Bylined press, disclosed-method analysis, regulator summary. 3 everything else. Marketing, affiliate roundups, undated blogs, forums, summaries of unread documents. A vendor is tier 1 for what its product does, tier 2 at best for a benchmark it publishes, and tier 3 for its quality and its competitors. A self-published number needs an independent origin for `✅`.

**Origins.** Two pages share an origin when they report the same event, release, dataset, or document. The domain changes nothing. The thing being reported decides. Three affiliate posts quoting one press release are one origin. One origin cannot carry `✅`.

**Absence test.** `❌` on absence needs all four: the claim is specific. Two counter-queries ran with different intents. The negation, and the registry or vendor that would own the fact. Nothing turned up at any tier. The `Why` prints both in backticks. A single fetched tier-3 page makes it `⚠️`.

**Definitions** earn `✅` from the one tier-1 document that states the convention. The origin count binds claims.

**Precedence.** The rows are exclusive. `❌` needs a contradicting span at tier ≤2 and no support at tier ≤2. `✅` needs support and no contradiction at equal or higher tier. `❓` needs comparable-tier sources on both sides. `⚠️` takes a claim a fetched quote supports only in part. `🤷` takes a claim no readable body can settle. Where two rows still fit, the one further from `✅` wins. The distance runs `✅`, `⚠️`, `❓`, `❌`. `🤷` sits outside that scale and is never reached while a usable body exists. Tier settles before distance does. A tier-1 document against a tier-2 summary takes the tier-1 row. `❓` needs comparable tiers.

**Done when** every line carries the verdict its strongest applicable row admits.

## 5. Annotate and render

### Artifact

Write one annotation per numbered claim, in the response's order. This is the artifact: every claim carries a verdict, its evidence and its `Why`. Save it as `reply` before step 6. The reply renders it — the order changes, the verdicts do not.

### Render

The reply leads with what failed:

1. `❌ BULLSHIT`, most consequential first — the one a reader would act on before the others. Ties break to the lower `C` number.
2. `❓ CONTESTED`, same ranking.
3. `🤷 UNVERIFIED`, in claim order.
4. opinions, in claim order.
5. `⚠️` and then `✅`, in claim order, only when the request asks for them.
6. the tally, the audit line, then the counts line for the passes — in that order, ending the reply.

`C` numbers stay as step 1 assigned them, so the reply's order is not its numbering. `C7` above `C3` is the ranking, not a mistake.

### An entry

Context comes first: the response's own sentences that make the claim judgeable, `…` between non-adjacent fragments, each fragment prefixed by its speaker. `agent:` for the response under test. `you:` for the person. The offending sentence is among them, and the antecedent of a bare "it" or "this" is quoted, never paraphrased. A context fragment is quoted whole, however long the sentence. The 15-word cap binds evidence spans only. An opinion entry may carry the context block too.

Then the evidence, for every marked verdict with a quotable source: a blockquote carrying the citation, ending `tier <n>`. `🤷` carries none, and a `❌` earned by the absence test prints its queries in the `Why` instead.

Then the claim, on one line: `C<n> <marker> **<VERDICT>** · claim — agent:|you: <plain statement>`. The statement is prose, not a quotation, and it names its subject. The path, version, or artifact the claim is about.

Then `Why: <flag>. <what the evidence shows>.`

A blank line goes before and after every blockquote, or the renderer swallows the claim line.

```
> agent: "The library handles 40k requests per second on a 16-core box." … agent: "That makes it the fastest option in its class."

> "peak throughput on our benchmark hardware was 4,100 rps" — [Benchmarks](…), tier 1

C4 ❌ **BULLSHIT** · claim — agent: the library sustains 40k requests per second and is the fastest in its class. Unsourced precision. The evidence is an order of magnitude short, and the 16-core qualifier is the source's, not the claim's. `library 40k rps benchmark` and `library 4100 rps` find no independent figure.

> agent: "Most teams settle on this approach."

C5 🤷 **UNVERIFIED** · claim — agent: most teams settle on this approach
Why: authority with no name. Generality. Absence carries nothing, and `most teams settle` and `teams settle approach survey` find no source stating it.

C6 · opinion — agent: the design will age well

✅ 2 · ❓ 0 · ⚠️ 1 · ❌ 1 · 🤷 1. Five marked. One opinion.

Self-audit: 5 lines checked, 0 changed

✅ 2 SUPPORTED · ⚠️ 1 WEAK. Full annotations on request.
```

### Withhold

`⚠️` and `✅` appear only in the closing counts line. Their claims, quotes, tiers, and `Why` lines are shared when the request asks for them. Share the warnings. Full annotation. Everything. Show the workings. Don't summarise. Then every claim renders at full shape, in the same order, and the counts line still ends the reply. The counts line always appears, zeroes included: `✅ 0 SUPPORTED · ⚠️ 0 WEAK — nothing withheld`.

The tally counts the five markers. Counts opinions apart. The counts line carries no `C` numbers.

**Done when** the artifact annotates every line in response order, the reply renders in the order above, and the withheld lines are summaries rather than omissions.

## 6. Audit

Run every check in `GATE.md` against the artifact, fix what fails, and rerun those checks. Read your annotations as someone else's. This is where a generous verdict gets caught. Save the rendered reply as `render` for checks 19 to 22.

The audit line names the verdict that changed and the check that caught it. `<old>` is the verdict before this pass, and the render shows `<new>`. `<marked lines>` counts the numbered lines that carry a marker, so an opinion is not counted:

```
Self-audit: <marked lines> lines checked, <changed> changed — <id> <old>→<new> (check <n>, <reason>) …
```

It sits second to last: the counts line for the passes ends the reply.

**Done when** every check passes, the audit line is second to last, and the counts line is the last line.

The machinery is `deep-research`'s evidence model cut down to one reply. When the job needs a report, that skill carries the full version: cached bodies, hashes, and a coverage bar per section.
