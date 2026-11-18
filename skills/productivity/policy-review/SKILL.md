---
name: "policy-review"
description: "Reviews a privacy policy, terms of service, EULA, or cookie notice against a personal data posture. Use when the user gives a link or pasted text and asks what it says about data training, reuse, sharing, retention, transfers, breach, children, or their rights. Reports a short review with recommendations, and calls nothing a show stopper."
---

# Policy review

This skill reads a policy against one standard, the reader's posture, and reports what matters in plain words.

Nothing it finds is a show stopper. Every flag is a fact the reader should know, ranked by how much attention it deserves.

## Contents

- Inputs
- Posture
- Handling
- Workflow
  - Step 1: Resolve the source
  - Step 2: Read against the posture
  - Step 3: Rank the flags
  - Step 4: Write the review
  - Step 5: Run the gate
- Severity
- Reply
- Limits
- Files

## Inputs

A link is fetched once, from the URL the user gives. Use the policy text. A summary is not a policy.

When the user gives no text, ask for the link or the paste. When the user gives a summary, ask for the policy text.

When the user gives two versions, take both and treat the later effective date as current.

When a paste ends mid-sentence, or a fetch returns part of a page, review what is present and name the gap in the footer. A login wall, paywall, or bot check stops the fetch, so ask for a paste.

## Posture

The posture is the standard. Read it in this order, taking the first that exists.

1. `POSTURE.local.md` beside `SKILL.md`, the reader's own posture.
2. `$XDG_CONFIG_HOME/policy-review/POSTURE.md`, when the first is absent. When `$XDG_CONFIG_HOME` is unset, read `~/.config`, or `%APPDATA%\policy-review\POSTURE.md` on Windows.
3. `POSTURE.example.md`, the generic default.

Name the file used in the footer. The reader keeps a personal copy at `POSTURE.local.md`, which git ignores.

When only the example exists, tell the reader to copy it to `POSTURE.local.md` and fill the context, as an action in What you can do.

A gate is a line the reader does not cross. A preference informs the ranking. Score every gate and preference in context as PASS, CONDITIONAL, FAIL, or NOT STATED. The shipped posture carries 17 lines. Score the gates and preferences only.

CONDITIONAL means the line clears only against a named condition the entity offers and the reader can verify, such as a signed contract or an opt-in setting. The flag names the condition and how the reader can check it. Where the reader cannot verify it, score FAIL.

A gate or preference missing from a local posture is a gap. Compare the gates against the six in `POSTURE.example.md` and the preferences against the eleven, name the gap in the footer, and score the rest. Use the gates the posture carries.

When the posture context is blank, assume the reader's own data only and say so in the footer.

When the document is silent on a gate, score NOT STATED.

## Handling

This skill reads and reports. It stores nothing.

- Read only the source the user gives. No search, no reputation lookup, no third party.
- Keep the text in memory for the turn and let it go.
- Quote one to three sentences per flag.
- Name the fetch route in the footer. Name the fallback when the fetch fails.
- Write a file only when the user asks for one.

## Workflow

### Step 1: Resolve the source

Resolve the posture file in the order in Posture. Fetch the link or take the paste. When the fetch fails, or the user gives no text, the reply is one short paragraph under 150 words asking for the paste. Do not write the six parts. Name the document type, the effective date, and the regime.

Take the regime from the governing-law clause. When the document names none, take the posture's jurisdiction. When both are silent, mark the regime NOT STATED.

Done when the posture file is named, the source text is present, the type is named, the effective date is recorded or marked NOT STATED, the regime is named or marked NOT STATED, and the entity is named or marked unnamed.

### Step 2: Read against the posture

Score the current version, one line per posture ID, carrying the score and the quote or the missing section. The working notes are the scores you hold in context for this turn, not a file. Read the family that carries each line, using the index in `RED-FLAGS.md`.

Done when every posture line has a score, and every score has a quote or a named missing section.

### Step 3: Rank the flags

A family is one section of `RED-FLAGS.md`. Write one flag per family, carrying every posture ID in it. Rank by exposure, using the posture context and the definition in Severity. Order by what the reader loses if the clause is used against them: children and health first, then identity and payment, then the reader's own content, then the rest. Gates come before preferences.

When more than seven families fail, merge the least exposed into one flag until there are seven, quoting the single most exposed clause and naming the rest.

Read `REGULATORY.md` when the regime is not Australian, the user names a regulated entity, or a posture line carries a statutory duty, which is G3, G5, S2, S6, S7, and S8.

Done when there are three to seven flags, or fewer when fewer families fail, one per family, in exposure order, and each carries a severity, its posture IDs, a quote, a heading, a recommendation, what it means, and what it means for this reader.

### Step 4: Write the review

Write the six parts, the footer, and the What changed line when there are two versions, in the order in Reply, using no banned word from `GATE.md` and no em dash or semicolon outside a quote.

Done when the six parts, the footer, and any What changed line are present, in order, and the word count is under the budget in Reply.

### Step 5: Run the gate

Run `GATE.md`, including its shell check when the skill folder is at hand. Fix the reply and run the gate again after any failure.

Done when every check in `GATE.md` passes.

## Severity

Two levels.

- **High attention**: a gate scored FAIL or NOT STATED, or a preference that touches direct exposure.
- **Worth knowing**: a preference that widens exposure without touching direct exposure. A line that clears only as CONDITIONAL sits in the normal line with its condition, and becomes a flag only when the condition is unmet or unverifiable.

Direct exposure means the data the reader actually holds in the service. Judge it against the posture context, which names the data at stake.

Silence is a flag. A gate scored NOT STATED is High attention. A missing retention clause is an unbounded permission, not a blank.

## Reply

The six parts apply once the source is readable. A reply carries six parts, a footer, and a What changed line when there are two versions.

**Bottom line.** Two or three sentences. What the document is, the worst flag or the fact that nothing is material, and the line that nothing here is a show stopper.

**What to know.** Three to seven flags, or fewer when fewer families fail, most important first. Each flag carries a short name, its posture IDs, its severity, one quote of one to three sentences, the heading, what it means, and what it means for this reader. A family with several IDs quotes its most exposed clause. When a flag cites a statute, name the clause.

**What is normal.** One line naming the gates that passed, the preference families with nothing material, and any gate the document cannot carry.

**What you can do.** Two to five actions.

**The one question worth asking.** One question, addressed to the entity.

**Not legal advice.** One line.

**Footer.** The source, the retrieval date, the effective date, the regime, and the posture file. Add the fetch route when a link is used, any gap or posture gap, and the blank-context note when used.

With two versions, compare the clauses that differ and add a **What changed** line of up to 30 words above the bottom line, naming the change that matters most.

| Part | Words |
|---|---|
| What changed, two versions only | 30 |
| Bottom line | 45 |
| What to know | 185 |
| What is normal | 30 |
| What you can do | 60 |
| The one question | 25 |
| Not legal advice | 15 |
| Footer | 35 |

The table is the three-flag baseline, and its caps sum to 395. Each extra flag adds up to 40 words.

See `examples/reply.md` for a worked reply.

## Limits

- Judge the published text at the retrieval date. What the entity does behind the policy is unobservable, so describe the text as written.
- This is not legal advice. Describe what the text states and omits.
- One posture, one reading. A different household needs its own posture.
- A cookie notice or a EULA carries fewer lines than a privacy policy. A gate the document cannot carry is one the document type does not address, such as a breach clause in a cookie notice. Score the gates it can carry and name the rest in the normal line.

## Files

- `POSTURE.example.md`: the generic standard, six gates and eleven preferences
- `POSTURE.local.md`: the reader's posture, gitignored
- `$XDG_CONFIG_HOME/policy-review/POSTURE.md`: an alternative posture location, or `%APPDATA%\policy-review\POSTURE.md` on Windows
- `RED-FLAGS.md`: phrases to search for, mapped to posture IDs
- `REGULATORY.md`: APP map, breach scheme, automated decisions, APRA, the 2024 Act, and the non-Australian overlay
- `GATE.md`: the checks and the step map
- `examples/reply.md`: a worked reply
