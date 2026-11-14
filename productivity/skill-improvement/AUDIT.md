# Audit

Mechanical checks. No judgement. Run these before reading for judgement, and again after every round.

Run each against the skill under review. A check that names a search term is a detector, not an example.

## Contents

- Law map
- A1 Frontmatter
- A2 Description
- A3 Line budget
- A4 References resolve
- A5 No scripts
- A6 No payload
- A7 No secrets
- A8 One term
- A9 Numbers
- A10 Orphans
- A11 Evals placement
- A12 Variant leak
- A13 Duplicate headings
- A14 Vague words
- A15 Contents list
- A16 Cross-references

## Law map

Five laws are mechanical and three need a read. This table is the contract between `SKILL.md` and this file.

| Law | Check |
|---|---|
| 1 Placement is the mechanism | A11 |
| 2 Every rule has a check | A16, and the target's step map |
| 3 One meaning, one place | A8, A13, and R8 in `CRAFT.md` |
| 4 State the loss | read: every transform records its drop |
| 5 Recompute every number | A9 |
| 6 Delete before you add | read: the file count after a fix |
| 7 Fix the file that should have prevented it | read: the eval section of the report |
| 8 Say the target, not the ban | A14, and R12 in `CRAFT.md` |

## A1 Frontmatter

```bash
basename "$PWD"
sed -n '1,6p' SKILL.md | grep -E '^(name|description):'
```

Pass when `name` matches `^[a-z0-9]+(-[a-z0-9]+)*$` and equals the folder name.

## A2 Description

Read the description. Pass when it names the outcome in its first clause and lists the branches that should trigger it. A description that opens with "Helps with" fails.

## A3 Line budget

```bash
wc -l SKILL.md
```

Pass under 500. A reference file over 300 lines needs a contents list.

## A4 References resolve

```bash
grep -rhoE '`[A-Za-z0-9._/-]+\.(md|txt|yaml|json)`' . --exclude-dir=examples |
  tr -d '`' | sort -u |
  while read -r f; do [ -e "$f" ] || echo "missing: $f"; done
```

Pass with no output. `examples/` is excluded because an example shows a shape, and its file names are illustrative.

## A5 No scripts

```bash
find . -type f \( -name '*.py' -o -name '*.sh' -o -name '*.js' -o -name '*.ts' -o -name '*.rb' \)
```

Pass with no output. A skill delivers text and instructions; a script belongs to the tool that runs it.

## A6 No payload

Search terms, not examples:

```bash
grep -rniE 'curl |authorization:|bearer [A-Za-z0-9$]|api[_-]?key *[:=]|content-type:|https?://' . \
  --exclude=AUDIT.md --exclude-dir=examples
```

Pass with no output. A request body, a URL, an auth header, and a response field all belong to the tool that makes the call.

`examples/` is excluded because a report may quote the payload it found. The Reads reviewer checks that no example quotes a live one.

## A7 No secrets

```bash
grep -rniE '(sk-|ghp_|xox[baprs]-|-----BEGIN)' . --exclude=AUDIT.md
```

Pass with no output.

## A8 One term

```bash
grep -rn '^#' .
```

Read the heading list. Pass when no concept carries two names across files. Two headings that name one concept are one concept in two places.

## A9 Numbers

Every count in prose is derived. Recompute each one from its artifact:

```bash
wc -l <file>; wc -w <file>; grep -c '<pattern>' <file>
```

Pass when every stated count matches its artifact. A count with no artifact is a claim, not a number.

## A10 Orphans

```bash
comm -23 \
  <(find . -type f | sed 's|^\./||' | sort) \
  <(grep -rhoE '`[A-Za-z0-9._/-]+`' . | tr -d '`' | sort -u)
```

Pass when every orphan is loaded by a harness or named in the report. The entry file is always an orphan: nothing points at it.

## A11 Evals placement

```bash
find . -type d -name evals
```

Pass with no output. Evals live outside the skill folder.

## A12 Variant leak

For each variant name:

```bash
grep -ni '<target>' SKILL.md
```

Pass with no output. The core names the variant; it does not carry the variant's mechanism.

## A13 Duplicate headings

Within one file, a heading appears once:

```bash
for f in $(find . -name '*.md'); do
  grep '^## ' "$f" | sort | uniq -d | sed "s|^|$f: |"
done
```

Pass with no output. A heading repeated across files is a signal, not a failure: R8 decides whether the content is duplicated.

## A14 Vague words

```bash
grep -rniE '\b(appropriate|proper|robust|seamless|leverage|utilise|ensure|good|nice)\b' . \
  --exclude=AUDIT.md --exclude-dir=examples
```

Every hit is replaced with the specific thing, or justified in the report.

## A15 Contents list

Every file over 100 lines opens with a contents list. Every heading in the file appears in that list, and every list entry names a heading.

## A16 Cross-references

Every reference to a check number, a file name, or a step number resolves.

```bash
grep -rnoE 'check [0-9]+' . --exclude-dir=examples
```

Pass when every number exists in the gate. A skill with no gate marks this check not applicable, and says so in the report.
