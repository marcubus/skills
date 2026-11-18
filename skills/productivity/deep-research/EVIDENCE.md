# Evidence

The run's state is two tables, `notes.md`, `run.lock`, and a folder of fetched bodies, written at the moment of the fetch, never afterwards from memory. A row written from a live page and a row written from imagination look identical to the next reader, including the agent that wrote them. The columns exist to make the difference visible: a cached body, a hash over it, and a quote that occurs in it. They prove the quote matches the body, not that the body came from the URL, so the report cites what the body says.

## Contents

- The run directory
- A sole-source run
- `sources.tsv`
- `claims.tsv`
- Fetching a body
- Quotes
- Confidence labels
- The coverage bar
- Truth discipline

## The run directory

`${TMPDIR:-${TEMP:-/tmp}}/research-<slug>/`. The slug is the report's slug, so the run directory and the report share one name.

Five entries:

| Entry | Job |
|---|---|
| `run.lock` | One line, the start epoch, written with `echo "$(date +%s)" > run.lock`. It marks the directory as a run. One run per slug. |
| `sources.tsv` | Every fetched body. Created with its header line. |
| `claims.tsv` | Every claim the report will make, with its sources and its quote. Created with its header line. |
| `bodies/` | One file per source, named `<id>-<slug>.txt`, where the slug is the report's slug. |
| `notes.md` | The fields below. |

The lock rule. Look for an existing run directory for this topic before starting. Where one exists and `notes.md` has `delivered: none` or no `delivered:` line, resume that run. Where `delivered:` carries a timestamp, the run finished: move the two tables, `notes.md`, and `bodies/` to `archive/<epoch>/`, and rewrite `run.lock` with the new start epoch. A directory holding `run.lock` and no `notes.md` is a crash before step 2 finished: archive it and start fresh. The delivered report stays where it is.

`notes.md` carries these fields, in this order:

```
question: <one sentence>
questions_asked: <the scope questions put to the user, or none>
brief: <the tone, audience, seed sources, whether a supplied document is the whole source, the boundary the topic names, and any length the user named, or none>
exclusions: <the boundaries the axes leave out, such as a geography or a time frame, or none>
report: <the resolved report path>
axes:
- <AXIS NAME> | <the part of the question it serves> | <the FINDINGS label>
skeleton_written_at: <YYYY-MM-DDTHH:MM:SSZ>
source_families: <the candidate families at step 2, then the families used at step 3, both on the line separated by semicolons, from SOURCING.md>
incentive: <one line per source with an incentive: S3 vendor marketing, or none>
fetches: <one line per fetch that took a fallback route: the url, the status, and the route that worked, or none>
overrides: <one line per override and its reason: a domain override, a one-family reason, or a no-search waiver, or none>
gaps: <one line per gap: the axis and what could not be established, or none>
delivered: <YYYY-MM-DDTHH:MM:SSZ, written at step 7 or at a step 3 exit, or none>
```

The FINDINGS label is the report heading the axis becomes, so the axis and the section are one thing with one name. `REPORT.md` sets what makes a label.

## A sole-source run

A sole-source run takes a supplied document as the entire evidence. Copy the document into `bodies/` as `S1-<slug>.txt`, or save pasted text there, write its source row and its claim rows by the procedure in step 3, quote it as one source, and say in the report that the findings rest on one document with no outside corroboration. Steps 1, 2, and 4 to 7 run as written; step 3 states what it waives.

A supplied document with a working search tool is a normal run. Search, and cite the document as one source among the others. When the search returns no usable source other than the supplied document, the run is sole-source and says so.

## `sources.tsv`

Ten columns, tab separated. Write the header line first:

```
id	url	domain	title	published	fetched_at	sha1	tier	origin	body
```

| Column | Carries |
|---|---|
| `id` | `S1`, `S2`, in order of first successful fetch. A failed fetch gets no row and leaves no gap in the id sequence. |
| `url` | The exact URL fetched, or the file path for a supplied document. |
| `domain` | The host, without `www.`, or `local` for a file. |
| `title` | The page title as fetched. |
| `published` | The page's own date, `YYYY-MM-DD`, `YYYY-MM`, or `undated`. |
| `fetched_at` | UTC, `YYYY-MM-DDTHH:MM:SSZ`, or `n/a` for a supplied document. |
| `sha1` | First twelve hex characters of SHA-1 over the raw body. Use `sha1sum` on Linux, `shasum -a 1` on macOS, or the Python fallback in `GATE.md`. `n/a` only for a supplied document copied in without a network fetch. |
| `tier` | `1`, `2`, or `3`, defined below. |
| `origin` | A short label naming the underlying event or document. Rows sharing a label are one origin. |
| `body` | The path including the folder, `bodies/<id>-<slug>.txt`, so a check run from the run directory can test it. |

Tiers:

- **Tier 1**: primary. The document itself, the dataset, the filing, the specification, the changelog, the peer-reviewed paper, a first-hand account from an identified practitioner. A vendor's documentation and changelog are tier 1 for what the product does.
- **Tier 2**: reputable secondary. Established press with a byline, an analyst report with a disclosed method and sample, a regulator's summary.
- **Tier 3**: everything else. Vendor marketing, affiliate roundups, undated blogs, forum posts, social media, summaries of documents the author did not read.

A vendor's own pricing page is tier 1 for the price it lists, and tier 3 for any claim about its quality or its competitors.

A tier 3 source is allowed. One rule governs it: no figure in THE NUMBERS or BOTTOM LINE rests on a tier 3 source. A tier 3 figure may appear in FINDINGS only when the text names it as that source's own claim.

## `claims.tsv`

Nine columns, tab separated. Write the header line first:

```
id	claim	section	sources	origins	confidence	quote	quote_source	note
```

| Column | Carries |
|---|---|
| `id` | `C1`, `C2`, in the order the report will use them. Step 5 renumbers after the sections are filled. |
| `claim` | One sentence, the claim the report will make. |
| `section` | The report label it lands in, in caps, such as `THE NUMBERS`, or the axis label it supports. A contested claim names its axis label, and WHERE THE SOURCES DISAGREE draws its paragraphs from the contested rows. |
| `sources` | Comma separated source ids, no spaces, such as `S3,S7`, or `none` for an `inference`. |
| `origins` | The count of distinct `origin` labels among those sources, or `0` for an `inference`. |
| `confidence` | `established`, `contested`, `single-sourced`, or `inference`. |
| `quote` | A verbatim span of at most fifteen words, copied from the body of `quote_source`. The writer cuts a longer span at a word boundary before the gate runs. Empty only for an `inference`. |
| `quote_source` | The source id whose body holds the quote, or `none` for an `inference`. |
| `note` | For a number: the base, the date, and the method, or `base not stated`. For a forecast: the vintage date, the scenario, and the model, labelled as a projection. For a contested claim: both figures and the opposing source. For a tender result or a levelised-cost model: its assumptions. For a translated quote: the translation. For a converted figure: the rate, its date, and the original figure. Empty otherwise. |

The `origins` count is the coverage bar made mechanical. Two articles about one press release carry one label and count as one.

The quote is the anti-fabrication device. A claim that cannot produce a verbatim span from a cached body is not evidence. Either find a span that supports it and label the claim by its origin count, or drop the claim.

## Fetching a body

The steps are in `SKILL.md` step 3. The body is what the fetch returned, saved without rewriting: do not strip navigation, do not reflow text, do not normalise spaces, because a re-encoded copy hashes differently and the hash must cover the saved file every quote is checked against. A fetch that returns page chrome as well as the article is written as returned; quote from the article text. A failed body follows the routes in `SOURCING.md`. Write no claim from it.

## Quotes

Copy the exact characters from the cached body, not from the browser. A typographic apostrophe rendered one way on the page breaks a literal search against the saved text. So does a non-breaking or thin space, which looks like an ordinary space and is not one, and so does a hard line break, which no single-line span can cross. An HTML body may hold entities such as `&#39;`, and a span that crosses a tag is not a span. A span that starts mid-sentence keeps the capital it was printed with. Pick one that survives the grep, and when a quote fails the check, compare the bytes with `grep -c` rather than the eye.

The quote carries the claim. It is not decoration, and it is not the page's best sentence. If the quote does not establish the claim on its own, the claim is wrong or the source is wrong, and either way it is not ready. For a figure, the quote establishes the number and the `note` carries its base, date, and method, so a short span never has to hold both. A source in another language is cached and quoted in the original, and the `note` column carries your translation of the quoted span, so a paraphrase in the report is never presented as the source's words.

## Confidence labels

Every claim carries one. The report names a claim `single-sourced` or `inference` where the bar or the reasoning requires it, and never prints a label for a claim that needs none.

- **Established**: two or more independent origins agree, and every source is inside the freshness window in `SOURCING.md`, or the report labels it with its date and why the claim still holds.
- **Contested**: credible sources disagree. The report presents both.
- **Single-sourced**: one origin only. Allowed for niche facts, and for a headline claim only when the text names it as single-sourced in the sentence that makes it. A source outside its freshness window caps its claim at `single-sourced`, unless the report labels it with its date and why the claim still holds.
- **Inference**: the report's own reasoning from established facts, marked as such in the text. Never presented as a sourced finding.

## The coverage bar

A headline claim states the report's answer or one of its figures, and is filed under BOTTOM LINE or THE NUMBERS in `claims.tsv`; before step 5 it is the claim that will carry the answer. Every other claim is supporting.

- Every headline claim has two independent origins, or the text names it as single-sourced or contested in the sentence that makes it.
- Every supporting claim has at least one origin and a confidence label, or is an `inference` with no origin and its reasoning in the text.
- An axis with no claim carrying an origin is exempt when it is recorded in `gaps:`, or when its claims all land in THE NUMBERS.

The bar binds because a claim that fails it is named in the report as `single-sourced` or `inference`. A run whose claims are all `single-sourced` says so in BOTTOM LINE. A run that labels everything `single-sourced` has met the bar and has also told the reader the report is thin, which is the honest outcome and the one the gate rewards.

## Truth discipline

Three rules, because a run that cannot prove its own work will, under pressure, disbelieve all of it and retract real research alongside the invented parts. Rule 1 binds the fetch logging in step 3, rule 2 the fix loop in step 6, and rule 3 the re-verification in step 4.

1. Cite the tool call and its output in the same reply as any claim about a file, a fetch, a tool result, or a system state.
2. A retraction cites the failing check. Name the command and the output that disproves the earlier claim.
3. When earlier figures are doubted, re-verify the doubtful rows through their quotes instead of retracting the set.
