---
name: "adr"
description: "Writes one architecture decision record (ADR), edits or supersedes an existing one, and reviews a record by check number."
---

# Architecture decision records

The skill records a decision; it does not make it and does not implement it. The triage conditions in `FORMAT.md` decide whether a choice earns a record.

## Contents

- Modes
- The decision interview
- Writing a record
- Reviewing a record
- Files

## Modes

| Mode | Ask | Deliverable |
|---|---|---|
| write | "record this decision" | a record, in the shape and lifecycle `FORMAT.md` gives |
| review | "review ADR-NNNN" | an editorial review by check number, fixing only the editorial defects |

## The decision interview

The frontier is the set of questions whose prerequisites are already settled. Ask only the frontier, in rounds. A round holds at most three questions. Number them, and give each one your recommended answer, so that "yes" settles it.

- Three rounds is the limit.
- Look up every fact yourself in the repository. Never ask for something you could read.
- A premise the repository contradicts goes back to the user as a question. It never enters the record as a fact.
- An unknown that survives the third round becomes a line under `## Open questions`. It never becomes an invented fact.

## Writing a record

1. **Read the house shape and the corpus.** List docs/adr/, read its index if one exists, and read the two highest-numbered records. Follow the shape of the highest-numbered one, with `FORMAT.md` settling anything it does not show. Search the records for one that covers this decision: a record covers it when its Decision section decides the same question. Done when the reply names the shape, how the repo marks implementation, and the covering record or says none does.
2. **Triage.** Apply the three triage conditions in `FORMAT.md`. Done when all three hold, or you have stopped and named the lighter home, even when the request was explicit.
3. **Interview.** Run the rounds above, including the evidence for the status: the diff or the git log. Done when the interview has settled the title, at least two alternatives with reasons, one cost, the status evidence, the deciders, and a revisit date where the decision has one.
4. **Resolve the decision.** Choose the outcome by `FORMAT.md`'s lifecycle and amending rules, and fill the four core sections. Done when the filled sections answer C10, C12, C13, C14 and C15.
5. **Write the file.** Create docs/adr/NNNN-slug.md, edit a `proposed` record in place, append the amendment section, or write the successor and change the old record's status line, as `FORMAT.md`'s amending rules describe each. Done when C1, C2, C3, C4, C5, C6, C8, C9, C17 and C18 pass, and the old record reads `superseded by ADR-NNNN` when there is a successor.
6. **Index the record.** Append one row when the index at docs/adr/README.md exists. Done when C7 passes, or the repo keeps no index.
7. **Run the gate.** `GATE.md`, every check. Done when every check passes and the path is in the reply.

## Reviewing a record

1. **Read the record and what it points at.** Done when C6 passes and every file it names has been opened.
2. **Run the gate.** Done when each of C1 to C19 carries its evidence in the reply, or the reply says why the check does not apply.
3. **Fix the editorial checks**, C1, C2, C4 to C7 and C9, and report each fix as a diff in the reply. Done when every editorial check passes.
4. **Route the substantive ones.** Every substantive finding, C10 to C18, takes `FORMAT.md`'s amending rules, which are write mode. A defect in C3 or C8 is reported and left for the implementer, and a record that fails C19 is reported as not earning a record, with the lighter home named. Done when each is named as an amendment, a successor, an implementer defect, or a lighter home.
5. **Report.** One line per failure: check number, file and line, and the smallest fix. Done when every failing check appears with its number, file, line and fix.

## Files

| Path | Contents | Read when |
|---|---|---|
| `FORMAT.md` | the house shape, triage, the status block, the lifecycle, amending and superseding, the index row | every write; review steps 2, 4 and 5 |
| `GATE.md` | nineteen checks, the step map | write step 7; review steps 2 to 5 |
