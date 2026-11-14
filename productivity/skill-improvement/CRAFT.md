# Craft

The Reads reviewer's checklist. Five levers, each with the check that catches it. The doctrine is Matt Pocock's `writing-for-agents`; this file is the version to run.

## Contents

- 1. The pointer
- 2. The two loads
- 3. The hierarchy
- 4. Completion criteria
- 5. Pruning
- Check list

## 1. The pointer

The description is a context pointer: it names the material and the branches that reach it. Its wording decides whether the skill fires.

Check:

- The first words name the outcome, not the category.
- Every branch is a distinct case, not a synonym.
- The pointer does not repeat identity the body already carries.

## 2. The two loads

Context load is what sits in the window every turn. Cognitive load is what the person has to remember.

- A model-invoked skill spends context load: its description is read every turn.
- A user-invoked skill spends cognitive load: the person has to remember it exists.

Check:

- Model-invoked: the description earns its line every turn.
- User-invoked: the name is memorable and the description reads well in a list.
- Material behind a pointer is cheaper than material inlined. Material with no pointer at all rides entirely on memory.

## 3. The hierarchy

Three rungs: an in-file step, an in-file reference, a disclosed reference behind a pointer.

Check:

- Every step is in the entry file.
- Reference that only some branches reach is disclosed.
- Reference that every branch reaches is inline.
- A concept's definition, rules, and caveats sit under one heading.
- No file is long because appending was easier than splitting.

## 4. Completion criteria

Every step ends on a condition that says done.

Check:

- The condition is checkable: a count, a file, a command, a list.
- The condition is demanding: "every rule applied" beats "a change list produced".
- The step does not end early because the later steps are visible.

## 5. Pruning

Check:

- One meaning, one place.
- The environment is not restated: file names, commands, and config the agent can look up.
- Every line still bears on what the skill does.
- No line restates a default the model already obeys.
- The skill states the target behaviour, and a prohibition appears only as a hard guardrail beside its positive form.

## Check list

Run these as greps where possible; the rest are reads.

| # | Check | Fails when |
|---|---|---|
| R1 | Pointer names the outcome first | The description opens with "Helps with" |
| R2 | One trigger per branch | Two synonyms for one case |
| R3 | Steps in the entry file | A step lives in a reference |
| R4 | Reference disclosed by branch | A long table every branch must load |
| R5 | Co-location | A rule separated from its definition |
| R6 | Checkable completion | "Understand the input" |
| R7 | Demanding completion | "Produce a list" where "every item classified" is possible |
| R8 | One meaning, one place | The same rule in two files |
| R9 | Environment not restated | The folder tree copied into the skill |
| R10 | No stale line | A count that no longer matches |
| R11 | No no-op | A line the model already obeys |
| R12 | Positive phrasing | A ban with no target behaviour |
