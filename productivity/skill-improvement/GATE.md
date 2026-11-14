# Gate

Phase 3. A gate is the skill checking its own output. It turns every rule into a numbered check.

The gate lives at `<skill>/GATE.md`. A skill with no other reference files carries the gate as a section in its entry file. The step map sits with the gate.

## Contents

- Shape
- Writing a check
- Step map
- Brought-in work
- Numbering

## Shape

Each check has a number, a name, a list of conditions, and a "Done when" line. Where a condition is mechanical, give the command.

A check reads like this:

- **7. Markers.** Every tag is one of the five. No bare bracket survives. Every value is in its enum. Done when the tag list, the bare-bracket grep, and the enum read are all clean.

The command sits above the condition, in its own block, so the reader can run it without reading the prose.

## Writing a check

- One rule per check. Two rules in one check fail together, and you cannot tell which broke.
- The check names the file that owns the rule.
- The condition is observable in the output, not in the author's intent.
- A check that needs judgement says so, and says what to compare.
- A check that can be a command is a command.

## Step map

A table from every step to the checks that close it.

| Step | Checks |
|---|---|

Every step appears. Every check appears at least once. A check that closes no step is either a rule no step applies, or a step that is missing.

## Brought-in work

When the skill accepts work it did not produce, the gate needs a second entry path: which checks still apply, which are skipped, and why. State it once, in the gate.

A brought-in path is a row in the step map and a line above the checks. It is not a second gate.

## Numbering

Numbers are stable. Add at the end; never renumber. A reference to an earlier check number in another file must stay true.

When a check is removed, leave the number and mark it retired, so old references still resolve.
