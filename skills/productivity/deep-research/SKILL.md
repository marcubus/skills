---
name: "deep-research"
description: "Researches a question across sources into one cited report, or turns a supplied document into one."
---

# Deep research

The report is the deliverable; the two exits at step 3 answer in chat and write none. Every claim traces to a source or is labelled an inference, and every source carries a tier and a date, or is named undated.

## Contents

- Inputs
- Workflow
  - Step 1: Frame the question
  - Step 2: Open the run
  - Step 3: Search in waves
  - Step 4: Validate
  - Step 5: Write the report
  - Step 6: Run the gate
  - Step 7: Deliver
- Output
- Limits
- Files

## Inputs

A topic, a question, or a document.

The scope rule:

1. Ask at most two questions about scope, audience, or angle. A scope is a named population, geography, time frame, or metric. When more than two qualify, ask the two whose answers change the most figures.
2. Ask only when the topic names none of these and no outcome, or when the metric is a category such as economics, cost, performance, or adoption rather than a measure.
3. Otherwise start, and put the boundaries the axes leave out in `exclusions:`, and the boundary the topic does name in `brief:`.
4. When no user is present, ask nothing. A person in the conversation is a user; an agent or skill that invoked the run is not. Take the broadest reading, record it in `brief:`, and name what that reading leaves out in `gaps:`. When the search tool is missing or returns nothing and no document was supplied, ask for seed sources when a user is present; otherwise proceed with the sources at hand and name the missing seed sources as a gap in the report. When there is no search tool, no seed source, and no supplied document, the run stops at step 3, which states how.

Two more questions sit outside that set and are expected, both only when a user is present. When a document was supplied, ask whether it is the whole source, and record the answer in `brief:`. When the user gives a tone, an audience, or seed sources, hold them for step 2 to write to `brief:`, and do not ask again. When the user answers a scope question, the answer edits the question sentence; exclusions always go to `exclusions:`.

A supplied document as the only evidence is a sole-source run, which `EVIDENCE.md` defines under A sole-source run.

## Workflow

### Step 1: Frame the question

Write one sentence naming what the report answers. Apply the Inputs scope rule before choosing axes, and put the two extra questions to the user when their condition holds. Step 2 writes the question to the top of `notes.md`. A topic one page answers is settled at step 3, which states the exit.

Then pick three to six axes from this list, choosing the ones this topic needs, so every part of the question is carried by one axis. For each, record the part of the question it serves and its FINDINGS label, as `EVIDENCE.md` defines it. A term of art the topic leaves undefined, such as a size threshold or a market segment, belongs to the definition axis, not to a scope question.

- Definition or mechanism, what it is and how it works
- Landscape, who is involved, how big, how adopted
- Money, pricing, cost, funding, who pays whom
- Technical depth, how it works under the hood
- Real-world experience, practitioner accounts and case studies
- Alternatives, what competes and how it differs
- History and trajectory, how the situation came to be and where it is going
- Criticism and failure modes, what detractors say, what goes wrong, and who gets hurt
- Regulation and law, what is permitted and required

Done when the question is one sentence, no more than two scope questions were put to the user, the boundaries the axes leave out are named for `exclusions:` or it is `none`, and there are three to six axes, each with a name, the part of the question it serves, and its FINDINGS label. Three is allowed only when the fourth axis you considered adds nothing the other three do not carry, and you record the axis you did not take and why in `gaps:`.

### Step 2: Open the run

Create the run directory described in `EVIDENCE.md` and write the five entries it lists. Choose at least two candidate source families from `SOURCING.md`, or one with the reason recorded in `overrides:`, and record them in `source_families:`. Apply the lock rule under The run directory in `EVIDENCE.md`, and resolve the report path by the Output section below. Then write the report skeleton at its final path: the header block and the labels from `REPORT.md` in its order, with one ALL CAPS label per axis after the FINDINGS label, each axis label followed by the line `TO BE WRITTEN`, and the same line under every other section.

Done when the run directory holds all five entries, `notes.md` carries every field `EVIDENCE.md` lists, in its order, with `overrides:` and `gaps:` filled or `none` and `skeleton_written_at:` set, `incentive`, `fetches`, and `delivered` read `none`, and the skeleton exists at the final path with every label in `REPORT.md`, the FINDINGS label, and one ALL CAPS label per axis, each with a `TO BE WRITTEN` line.

### Step 3: Search in waves

Run the axes in waves. Run queries with the harness search tool, such as `websearch`. When the harness has no search tool, use the seed sources the user gave as the first queries. Apply the anti-SEO rules in `SOURCING.md` to every result before fetching it.

1. Broad sweep. One query per axis, phrased as a stranger would phrase it, with no product or vendor vocabulary, and with the first intent `SOURCING.md` assigns that axis under Query intents. Start each axis at the place `SOURCING.md` names under Where to look first.
2. Fan out. Two more queries per axis, so each axis has three queries before the depth pass and at least two distinct intents from `SOURCING.md`.
3. Blindspots. Three queries in total, one per axis at most, choosing the three that could overturn a headline claim from what a smart reader would ask and the user did not: cost, alternatives, failure modes, who profits. Log each one under the axis it serves, never under a new axis name, or as a `gaps:` line when it serves none.
4. Depth. Two queries per axis: one following the unexpected names, products, and claims the first three waves surfaced, and one operator query as `SOURCING.md` describes under Query intents, so a filing, a specification, or a dataset is reached. Chain the backward and forward hops `SOURCING.md` describes under Citation chaining; a hop is a fetch, not one of the five queries.

After a wave that added rows, write a claim row for each new claim; filling here may be out of order and may be rough, and step 5 normalises the order and rewrites each section. A rough row is normalised before the gate runs, so a draft row may break the quote and column rules while the search is still open.

Fetch the page, not the snippet. Every fetch is cited as a tool call in the same turn, as truth discipline rule 1 in `EVIDENCE.md` requires. Save the page with `curl` to the body file whenever a shell is available; that is the default route. When no shell is available, use the harness fetch and file tools and log the route in `notes.md`; the hash then covers your transcription rather than the page, so say so. Reach for the non-web sources in `SOURCING.md` before settling for an article. Then:

1. Write the body to `bodies/<id>-<slug>.txt`, but only once it passes the render-failure rule under Dead and paywalled pages in `SOURCING.md`. A failed fetch leaves no body file.
2. Compute the SHA-1 over the file you wrote with `sha1sum`, `shasum -a 1`, or the Python fallback in `GATE.md`, or write `n/a` for a supplied document copied in without a fetch.
3. Write the source row with all ten columns in one write.
4. Write the claim rows the body supports, with the quote copied from the cached file.

After the first wave, add the families actually used to `source_families:`, keeping the candidates, including the family that carries the primary source for every number.

The search is done when every axis has been through the first, second, and depth waves, which is five queries per axis and at least two intents, and the three blindspot queries are run. At that point stop searching, read the cached bodies already found, tier 1 first, and write from them. Stop earlier only when the sources are exhausted for every axis, every axis has a claim with an origin and a quote, and the most recent wave added no new claim row; name the exhaustion in `gaps:`.

A gap that survives the stop condition is a finding. It goes in WHAT COULD NOT BE VERIFIED with the phrasings you tried.

When the first wave shows that one page answers the question, with one source and no figure in dispute, stop: answer in chat, delete the skeleton, and write `delivered:` with the UTC timestamp, so a later run starts fresh. When the waves produce no usable source and no document was supplied, delete the skeleton, write no report, and reply with the topic that could not be run and the missing sources as the gap; write `delivered:` with the UTC timestamp too. Neither exit runs steps 4 to 7.

On a sole-source run the waves are waived; the body, its hash, its source row, and its claim rows are still required.

Done when the stop condition holds or the run is sole-source, every fetched body that passes the render-failure rule has a source row, its sha1, and its claim rows, `sources.tsv` holds three rows or more unless the run is sole-source or the report names the shortfall in WHAT COULD NOT BE VERIFIED, each axis's backward and forward hop is recorded as a source row or a `gaps:` line, and `source_families:` names the candidates and the families used. When no search tool was available, the source floor and the two-family rule are waived, and the reason is recorded in `overrides:`.

### Step 4: Validate

Run the sourcing rules in `SOURCING.md` on every claim. Check domain concentration once for the run, under its heading in `SOURCING.md`. A claim turns on recency when a newer figure would change the finding, so judge that here. Rewrite the `tier` column when an incentive caps it, and name the cap on each affected claim row in `note`. Apply Primary-source escalation in `SOURCING.md`. A source outside its freshness window is capped by `EVIDENCE.md`. Re-verify rows through their quotes, which is truth discipline rule 3 in `EVIDENCE.md`; check 6 then reads every quote against its claim. An undated source may carry only a claim that does not turn on recency, unless it is a specification or standard whose version is named; otherwise drop it. Label an inference as an inference, with its reasoning in the sentence that makes it. Then give every claim one of the four confidence labels in `EVIDENCE.md`, apply Independence and origin in `SOURCING.md`, and mark each contested row with the axis label it supports; its `note` names both figures, and WHERE THE SOURCES DISAGREE draws its paragraphs from those rows. For every contested claim, read the strongest version of the other case, as `SOURCING.md` sets under The opposite side. A figure converted from another currency names the rate and its date. Apply the coverage bar in `EVIDENCE.md`.

Done when every claim row carries a confidence label and a correct origins count, every contested claim row names both figures and the opposing source in its `note`, every figure filed under THE NUMBERS or BOTTOM LINE in `claims.tsv` meets the tier rule in `EVIDENCE.md`, every translated quote carries its translation, every converted figure names its rate and date, every source with an incentive has a note in `notes.md`, every unreachable origin is dropped or labelled tier 3, every out-of-window or undated source is labelled or dropped, a domain override adds its `gaps:` line, every axis meets the coverage bar or is exempt under it, and every gap is listed with the phrasings tried.

### Step 5: Write the report

Read `examples/report.md` before filling the skeleton, then fill it in the order in `REPORT.md`, to its prose rules, which own the marker and the number. Normalise every rough claim row: trim a quote to fifteen words, repair its column count, and fill its `note`. Delete each `TO BE WRITTEN` line as its section is filled; the labels stay. Rename an axis label whose finding changed, keeping it a statement. Remove the label and stub of an axis that ended with no claim and is not exempt under the coverage bar, drop it from the `axes:` list, promote every `gaps:` line into WHAT COULD NOT BE VERIFIED, and promote a one-family reason from `overrides:` there too. Renumber the claim ids to the report's order.

Done when every section is filled, or omitted only when empty and named in WHAT COULD NOT BE VERIFIED, a three-axis run says why in WHAT COULD NOT BE VERIFIED, every `gaps:` line appears there, no `TO BE WRITTEN` line remains, the report is inside the band in `REPORT.md`, including its named-length exception, or below its floor with the reason named in WHAT COULD NOT BE VERIFIED, and SOURCES lists every source in the shape `REPORT.md` sets.

### Step 6: Run the gate

Run checks 1 to 12 in `GATE.md`. Fix the report and run them again after any failure. Each check names its evidence: a block section, a report command, or a read of `notes.md` and the two tables. The ledger block runs from the run directory. A failure is fixed in the report, not explained away: when a check disproves an earlier claim, retract it and cite the check and its output, as truth discipline rule 2 in `EVIDENCE.md` requires.

Done when checks 1 to 12 pass.

### Step 7: Deliver

The reply is the handoff. It carries, in this order, the items below.

- The invoking skill's name, when another skill invoked the run.
- The report path, stated plainly as written.
- The word count, and whether the material needed more than the band.
- The source count by tier.
- The key finding in one sentence.
- Every conflict, one line each.
- Every gap, one line each, with what was tried.
- The confidence of the headline claim, and what would change it.

Done when checks 2 and 12 pass, the reply carries every item above, any exemption from the word band, the source floor, or the concentration cap is named, every figure in the reply is one you can reproduce from the files, and `delivered:` is written last.

## Output

One file, at <reports-dir>/YYYY-MM-DD-<slug>-report.md. The date is the local date of the run, and every timestamp in the run files is UTC. The slug is the subject of the request in lowercase with hyphens, dropping articles, prepositions, and the verbs of the request such as `research`, `write`, and `report`, at most 60 characters: `grid-scale sodium-ion battery storage economics 2026` becomes `grid-scale-sodium-ion-battery-storage-economics-2026`, which is 52 characters. When the slug runs over 60, drop the least distinguishing word.

The reports directory resolves in this order, first hit wins. A config file with no `reports_dir` line falls through to the next rule. A path beginning with `~` is expanded to the user's home directory (`$HOME`, `%USERPROFILE%`, or the host's equivalent) before use. The skill creates the directory at that path when it is absent; the config file is the user's to create.

1. A path the user names in the request, unless it would put the report inside the run directory; that path is refused and rule 4 is used.
2. The `reports_dir` line in `$XDG_CONFIG_HOME/deep-research/OUTPUT.md`, or `~/.config/deep-research/OUTPUT.md` when `XDG_CONFIG_HOME` is unset, or `%APPDATA%\deep-research\OUTPUT.md` on Windows.
3. The `reports_dir` line in `OUTPUT.local.md` beside this file.
4. `reports/` in the directory the user invoked the skill from, which is the session's working directory. When that directory is a git work tree and the user named no path, use `$XDG_DATA_HOME/deep-research/reports/` instead, or `$HOME/.local/share/deep-research/reports/` when `XDG_DATA_HOME` is unset, or `%LOCALAPPDATA%\deep-research\reports\` on Windows, so a generated report lands outside the commit history. The report path recorded in `notes.md` under `report:` shows which directory that was, so a gate run from the run directory still knows where the report lives.

Everything else the run produces is working material, whose home is the run directory in `EVIDENCE.md`. The reports directory holds reports only. When the target path already holds a report, keep it and write beside it: add `-2` before the report extension, then `-3`, and record the new path in `report:`.

## Limits

- Research is bounded: the report cites what supports and what contradicts rather than everything published.
- When the origin behind a paywall cannot be read, cite the secondary and name the paywall as the gap in WHAT COULD NOT BE VERIFIED. `SOURCING.md` has the routes to the claim behind one.

## Files

- `SOURCING.md`: finding and judging sources.
- `EVIDENCE.md`: the run directory, the two tables, and truth discipline.
- `REPORT.md`: the report's shape and prose rules.
- `GATE.md`: twelve checks.
- `OUTPUT.example.md`: the optional reports directory override.
- `examples/report.md`: the worked report.
