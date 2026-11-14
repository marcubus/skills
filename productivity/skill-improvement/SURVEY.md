# Survey

Phase 1. Read the skill before judging it. The output is a contract sentence, an inventory, and a fact table.

## Contents

- Inventory
- Contract
- Fact table
- Baseline audit
- Exit

## Inventory

List every file in the folder, and every file outside it that the skill points at.

| File | Lines | Role | Points at | Pointed at by |
|---|---|---|---|---|

Role is one of: entry, reference, variant, example, fixture, asset.

Flag at once:

- a file no other file points at (orphan)
- a pointer to a file that does not exist (broken)
- a file over 300 lines that is not a reference
- anything executable

## Contract

Write one sentence: "Given an input, this skill produces an output, by this method."

Then test the description against it:

- Does the description name the outcome?
- Does it name the branches that should trigger it?
- Would a person scanning ten skills know when to pick this one?

A user-invoked skill is indexed by the person. A model-invoked skill is indexed by the pointer. The description has to work for whichever it is.

## Fact table

Collect every fact the skill asserts in more than one place: an enum, a count, a filename, a budget, a limit, a rule.

| Fact | Where it appears | Single source |
|---|---|---|

The single source is the one place that should own it. Every other appearance is a cache that must match, or a duplicate that must go.

## Baseline audit

Run `AUDIT.md` once before reading for judgement. The mechanical findings are cheap, and they stop you arguing about what a grep settles.

## Exit

Done when the inventory is complete, the contract is one sentence, and every repeated fact has a row.
