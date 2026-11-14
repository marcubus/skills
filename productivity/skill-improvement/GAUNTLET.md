# Gauntlet

Phase 2. Rounds of three reviewers, each in a fresh context, until a round returns zero blockers and zero majors.

## Contents

- A round
- Runs
- Reads
- Audit
- Fixing
- Exit

## A round

Run the three reviewers in parallel subagents where the harness supports it. Otherwise run them in sequence and re-read every file from disk between them.

Each reviewer returns findings only. No reviewer edits a file. The main agent fixes.

Cap each reviewer at 400 words. A reviewer that writes more is summarising, not finding.

Write every finding as a row in the report's findings table. The shape and the rules for a row are in `REPORT.md`.

## Runs

Brief:

> You are a fresh agent using this skill for the first time. You have the skill folder and nothing else. Walk it start to finish on a concrete input. Report, by file and line: (a) any step where you do not know what to read, what to produce, or when you are done; (b) any promise in the description or the body that no rule delivers; (c) any rule that no step applies; (d) any place you would have to ask the user a question. Under 400 words.

The question in (d) is the sharpest signal. A skill that needs a question is not finished.

## Reads

Brief:

> Read `CRAFT.md`. Report, by file and line, every place the skill fails one of its checks: a pointer that will not fire, material at the wrong rung of the hierarchy, a step with a vague or weak completion criterion, a meaning in two places, a line that is stale, a no-op, or a negation. Quote the line. Under 400 words.

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
