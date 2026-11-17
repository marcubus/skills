# Gauntlet

Phase 2. Rounds of four reviewers, each in a fresh context, until a round returns zero blockers and zero majors.

## Contents

- A round
- Runs
- Reads
- Voice
- Audit
- Fixing
- Exit
- Lens pass

## A round

Run the four reviewers in parallel subagents where the harness supports it. Otherwise run them in sequence and re-read every file from disk between them.

Each reviewer returns findings only. No reviewer edits a file. The main agent fixes.

Cap each reviewer at 400 words. A reviewer that writes more is summarising, not finding.

Write every finding as a row in the report's findings table. The shape and the rules for a row are in `REPORT.md`.

## Runs

Brief:

> You are a fresh agent using this skill for the first time. You have the skill folder and nothing else. Walk it start to finish on a concrete input. Report, by file and line: (a) any step where you do not know what to read, what to produce, or when you are done; (b) any promise in the description or the body that no rule delivers; (c) any rule that no step applies; (d) any place you would have to ask the user a question. Under 400 words.

The question in (d) is the sharpest signal. A skill that needs a question is not finished.

## Reads

Brief:

> Read `CRAFT.md`. Report, by file and line, every place the skill fails checks R1 to R9: a pointer that will not fire, material at the wrong rung of the hierarchy, a step with a vague or weak completion criterion, a meaning in two places, a line that is stale, or a no-op. Quote the line. Under 400 words.

Reads judges structure. Voice judges prose, and the split exists because one reviewer with fourteen checks spends its attention on the first nine.

## Voice

Brief:

> Read `CRAFT.md`. Report, by file and line, every place the skill fails checks R10 to R14: a stale count, a no-op, a ban with no target behaviour, an example carrying a live value, or an idea spelled out where one defined word would anchor it. Quote the line. Under 400 words.

A prohibition that is a hard guardrail is not a finding when its positive form sits beside it.

## Audit

Brief:

> Run every check in `AUDIT.md` from inside the target folder. Report each hit with its command and output. List cross-file duplicate headings and hand them to Reads; do not judge them. No fixes. Under 400 words.

## Fixing

Fix in severity order. After a fix, re-run the check that caught it, not the whole round.

When two findings share a cause, fix the cause once. Two stale counts are one missing rule about derived numbers.

When a fix would add a file, name the file it replaces, or say why nothing replaces it.

## Exit

Done when a full round returns zero blockers and zero majors. Record the round number and the counts in the report.

A round that returns only minors ends the gauntlet. Batch the minors into one pass.

When the cap is reached without a clean round, the cap is the exit and the report says so. Record the class of the findings that remain, not only the count: contradictions open is a failure, seams open is a stop. "Seams" means counts, duplicated pointers, and done conditions that disagree with a branch they allow.

## Lens pass

After the exit, run one pass with a lens the gauntlet does not use. The four reviewers share one doctrine, so they converge on one class of finding; a second lens finds what the first cannot see.

Pick one:

- A second doctrine, read in full and applied as a checklist.
- A domain expert brief: the skill's own subject matter, judged for wrongness rather than for craft.
- An adversarial reader brief: someone who wants the output to fail.

Brief the lens reviewer like the others, findings only, 400 words. Record the pass as its own section in the report, with the lens named. Its findings go through the same severity ladder and the same fix pass. A lens pass that finds nothing is recorded as clean.
