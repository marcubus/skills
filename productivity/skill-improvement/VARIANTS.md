# Variants

When a skill has more than one external target, split the mechanism out of the core.

## Contents

- When to split
- The three parts
- Capability table
- Transform verbs
- Naming
- Check

## When to split

Split when two conditions hold:

- The skill serves two or more targets, backends, or formats.
- The mechanism differs between them.

If only the words differ, keep one file and a table.

## The three parts

- **Core**: the procedure and the intent. It says what must happen, never how a target does it.
- **Variant**: one file per target. It holds the mechanism, a capability table, and the transform rules.
- **Registry**: one file that lists the variants and the rule for choosing one.

The core names the variant. The variant names the mechanism.

## Capability table

Every variant opens with a table of what it carries.

| Element | In the output |
|---|---|
| element A | kept |
| element B | translated |
| element C | dropped |

A reader knows what will be lost before reading a rule.

## Transform verbs

Three, and only three:

- **Keep**: the target reads it as written.
- **Translate**: replace it with the target's form.
- **Drop**: remove it, keep the words, and record the loss.

A drop is not a failure. It is a documented loss. Every drop appears in the deliverable's notes.

## Naming

- The variant file is named for the target, in the target's own spelling.
- A deliverable names the target only when the target changes the deliverable's form.
- The registry names the default.

## Check

- The core carries the procedure; the mechanism lives in the variant.
- The variant carries the mechanism; the procedure stays in the core.
- Every element in every capability table is keep, translate, or drop.
- Every drop is recorded somewhere the reader will look.
