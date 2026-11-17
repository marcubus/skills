# Sourcing

How to find sources, and how to judge them. The evidence rules are in `EVIDENCE.md`; this file is about the hunt.

## Contents

- Query intents
- Where to look first
- Source families
- Primary-source escalation
- Anti-SEO rules
- Domain concentration
- Citation chaining
- Dead and paywalled pages
- Non-web sources
- Freshness
- Independence and origin
- Incentive
- The opposite side

## Query intents

One query per axis returns one cluster of pages, usually the cluster best optimised for that phrasing. Every axis gets at least two of these intents, and step 3 sets the query count: definitional (`how does X work`), comparative (`X vs Y`, `X alternatives`), critical (`X problems`), primary (`X specification filetype:pdf`), practitioner (`X reddit`), quantitative (`X cost per kWh 2026`).

The axis picks the first intent: definition and mechanism take the definitional intent, landscape the comparative, money the quantitative, technical depth and alternatives the primary, real-world experience the practitioner, criticism and failure modes the critical, history the primary, and regulation and law the primary.

Vary the phrasing, not only the word order. A query written in the vendor's vocabulary returns vendor pages. A query written in the sceptic's vocabulary returns the other half of the picture. Use operators where they help: `site:`, `filetype:pdf`, `intitle:`, a year, a minus term to exclude a dominant brand.

## Where to look first

The axis decides the first place to look. Searching every axis the same way is the most common way a report ends up thin.

- Definition or mechanism. The reference work, the standard, the documentation, then the press.
- Landscape. Analyst summaries with a disclosed sample, then the vendors' own numbers, then the press.
- Money. Pricing pages and filings first. A review that quotes a price is a secondary source for a primary fact. When no vendor publishes a price, as in a market sold by tender, PPA, or an analyst's levelised-cost model, take the tender result as the primary, or the model as a tier 2 source, and name its assumptions.
- Technical depth and alternatives. Version-pinned documentation, changelogs, and issue threads; benchmarks and independent tests with a stated method, never vendor comparison pages.
- Real-world experience, criticism, and failure modes. Forums, issue trackers, named practitioners, the strongest version of the other case, incident reports, post-mortems, and enforcement actions.
- History, trajectory, and regulation. Contemporaneous reporting and the original announcement; roadmaps, release notes, and funding; the statute or the regulator's page, never the summary of it.

## Source families

Decide which families this topic needs before searching: a technical or legal topic needs official and primary, a market topic needs analyst and trade press, and a contested topic needs both sides. A report built from one family is a report about that family.

- Official and primary: standards, legislation, filings, documentation, datasets, peer-reviewed papers.
- Regulator and government: enforcement actions, consultations, statistical releases.
- Analyst and research: reports with a disclosed method and sample.
- Trade press and community: beat reporters who name their sources; issue trackers, forums, mailing lists, conference talks.
- Vendor: what the seller says about itself. Useful as a claim, never as proof.

## Primary-source escalation

For any claim about a price, a policy, a standard, a statistic, or a product capability, go to the origin before citing the article about it: the vendor's pricing page for a price, the published document for a policy, the specification for a standard, the dataset or methodology for a statistic, the changelog or docs for a capability. The tier rule that follows from it lives in `EVIDENCE.md`. When the origin cannot be reached, the figure is dropped, or kept in FINDINGS as the secondary's claim and labelled tier 3.

## Anti-SEO rules

Search results are written for synthesis engines. A page that ranks is a page written to be quoted, which is not the same as a page that is right. Assume the top results are optimised until proven otherwise.

- Prefer a named author with a byline and a visible date. An undated page with no author is a content farm until it proves otherwise.
- Read the roundup for names, then price each one from its own page.
- Take every number with its base. "52 percent of 400 surveyed enterprises, in March 2026, self-selected through a newsletter" is a finding; "52 percent adoption" is not.
- Read the paywalled study before trusting the article about it. When the study cannot be read, the article is tier 3 and is labelled that way.
- Trust the boring page. A specification, a filing, or a changelog reads badly and is usually right.

## Domain concentration

Draw the sources from the families named under Source families, so that no single domain supplies more than three sources in a run of twelve or fewer. Above twelve sources, no domain may supply more than a quarter of the sources, rounded down, so the cap is three at thirteen to fifteen sources, four at sixteen to nineteen, five at twenty to twenty-three. The cap exists for the same reason as the family rule.

When the topic genuinely lives on one domain, such as a single product's documentation, record the override and its reason in `notes.md` under `overrides`, and add a matching `gaps:` line so the report names it.

## Citation chaining

Two moves a search box cannot do, and they are where a deep report separates from a summary. Backward: take the best source and read its references, because the origin of a claim is usually one hop behind the article that made it. Forward: take the best source and find who cites it, by searching its exact title in quotes or its author plus the topic, because the critique of a study is usually a later paper rather than a news story.

Chain one hop backward and one hop forward per axis, where the origin is one hop away. Chaining is judgement: do it, record a chained source as an ordinary source row, and write a gap line when no origin is within one hop. It is for finding the primary and the rebuttal, not for reading the internet.

## Dead and paywalled pages

A failed fetch is a logged event, not a silent gap. Try the routes in order, and record the one that worked in `notes.md`: a different format, since some pages render as text but not as markdown; the print view, the AMP view, or the plain-text endpoint; the Wayback Machine at `web.archive.org/web/<YYYYMMDD>/<url>`; the origin, since a press release, a preprint, an author's copy, a regulator's copy, or a filing often carries the same claim; then give up, log the status and the routes tried in `fetches:`, and name the claim as a gap in WHAT COULD NOT BE VERIFIED. When neither the study nor a usable account of it can be read, the claim is a gap, not a row.

A body under two hundred bytes is a render failure, not a source. So is a large body that is mostly script, and a page that returns a captcha wall, a login wall, an error page, or a document other than the one the URL names. Read the first few hundred characters before trusting a body: a 200 status with a title and no article text is the most common form of this, and logging it as a source is how a report ends up citing a page nobody could read.

## Non-web sources

The best source for a technical or legal claim is often not a web page. Reach for these before settling for an article:

- PDFs. Test whether the text extracts before declaring one unreadable. Most decode.
- Filings and annual reports. The number is in the table, not the summary.
- Standards, specifications, changelogs, and issue threads. Clause numbers and diffs make a claim checkable.
- Court and tribunal records. The finding, not the reporting of it.

## Freshness

Set the window by subject, not by topic. A topic can be stable in its fundamentals and fast in its pricing.

| Subject | Window |
|---|---|
| Money, landscape, technical depth, alternatives | 6 months |
| Trajectory | 6 months |
| Regulation and law, a standard, or a specification | Current text, with the version or the date it changed |
| Definition and history | 2 to 3 years |
| Criticism, failure modes, real-world experience | no limit, always with the date |

Label a source outside its window with its date, so the reader can judge. An annual outlook is current for the year it covers, and its vintage date is named.

## Independence and origin

Two sources are independent when they do not share an origin. The test is the chain, not the domain. A vendor announcement and a news story quoting it are one source, and so are two analyst models that share one upstream price survey. Search the shared sentence in quotes before assigning a new `origin` label; when it appears on three domains, treat them as one source.

The `origin` column carries the label, and `EVIDENCE.md` defines it. Two rows with the same label are one origin, whatever their domains.

## Incentive

For every source, ask who benefits from the claim being believed. Write one line per source in `notes.md` when the answer is not "nobody". Vendor marketing benefits from capability claims, a competitor's comparison from the other side looking worse, an affiliate roundup from the click, an advocacy group from the harm being large, and a trade body from the market being big.

An incentive does not disqualify a source. It tells the report which claims need a second origin.

## The opposite side

For a contested claim, find the strongest version of the other case, not the weakest. Search the counter-claim in its own vocabulary, and read one source written by someone who holds it. A report that only quotes critics of a thing, or only its defenders, has not researched it. It has picked a side and dressed the choice as coverage.
