# Bullshit

## What
Fact-checks an answer claim by claim: verdict and evidence for each, failures first. Every assertion is bullshit until a quote from a fetched page says otherwise. Memory, search snippets, and inference reach 🤷 at most.

## Why Use It
When you need to verify claims before acting on them. Catches unsupported statistics, misquoted sources, or confident assertions without evidence.

## How (Brief)

Invoke as a skill: `/bullshit`. Call it with nothing to fact-check your last turn. Example:

```
/bullshit
```

Or tell it what to check:

```
/bullshit paste the response you want checked
```

## Output Structure

The reply leads with what failed:

1. **❌ BULLSHIT** — most consequential first (ties break by lower C number)
2. **❓ CONTESTED** — same ranking
3. **🤷 UNVERIFIED** — in claim order
4. Opinions — in claim order
5. ⚠️ WEAK and ✅ SUPPORTED — only when requested

Then the tally, audit line, and counts line ending the reply.

## The Four Verdicts

| Verdict | Earned When |
|---|---|
| **✅ SUPPORTED** | Tier-1 quote establishes it outright, or two independent origins at tier ≤2 agree with no contradiction at equal or higher tier |
| **❓ CONTESTED** | Credible sources disagree; both sides quoted as the split is |
| **⚠️ WEAK** | Fetched quote falls short: one origin, tier 3, partial claim, or higher tier supports while lower contradicts |
| **❌ BULLSHIT** | Tier ≤2 span says otherwise with no support at tier ≤2; misquoted text; or absence test passes |
| **🤷 UNVERIFIED** | Body behind a wall; claim over a horizon (future, unobservable); or generality too vague for absence to mean anything |

## Sourcing Tiers

- **Tier 1** — Primary: dataset, filing, spec, changelog, peer-reviewed paper, first-hand account
- **Tier 2** — Reputable secondary: bylined press, disclosed-method analysis, regulator summary
- **Tier 3** — Everything else: marketing, affiliate roundups, undated blogs, forums, summaries of unread documents

## Workflow Summary

1. **Decompose** — number every claim C1, C2, ...; tag as claim, definitional, or opinion
2. **Flag** — mark shapes bullshit takes: authority with no name, unsourced precision, confidence doing evidence's work, totalisers, named artifacts, internal conflict, causation from correlation
3. **Verify** — search in waves: locate artifact, fetch primary document, grep for quote span, search strongest contradiction
4. **Apply the bar** — verdict per claim using tier rules and precedence
5. **Annotate and render** — write artifact in response order, reply in failure order
6. **Audit** — run GATE.md checks against the artifact

## Evidence Rules

- Quote ≤15 words from fetched bodies; keep negation, condition, scope
- A span you cannot find is a span that does not exist
- One query at rungs 1 and 2, two at rung 4; four queries per claim maximum
- Absence test needs: specific claim, two counter-queries with different intents, nothing found

## Files

| File | Purpose |
|---|---|
| `SKILL.md` | Full workflow, six phases, evidence model |
| `GATE.md` | Audit checks for the artifact and rendered reply |

## Limits

- The body sits behind a wall: paywalls, login walls, bot checks stop verification
- A comfortable reply runs in one pass; longer ones are annotated in waves
- Opinions carry no verdict; they appear only in counts line unless requested

## Attribution

Original concept by Marcubus. This implementation provides a claim-by-claim fact-checking system with tiered sourcing and automated audit gates.
