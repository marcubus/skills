# Audit

Checks the agent's file and search tools can settle, plus a few short reads. Run them from inside the target folder, before reading for judgement and again after every round. Each check's command is an equivalent mechanical route for a host with a POSIX shell. The agent route is primary; the command is the fallback.

| Check | Agent route | Pass when |
|---|---|---|
| A1 | Read the folder name and the first six lines of `SKILL.md` | `name` matches the slug pattern and equals the folder name |
| A3 | Count the lines in `SKILL.md` | Under 500 |
| A4 | List every file except `examples/`, collect the backticked `.md`, `.txt`, `.yaml`, and `.json` paths in the files, and open each one | No referenced path is missing |
| A5 | List every file and note its extension | No `.py`, `.sh`, `.js`, `.ts`, or `.rb` file |
| A6 | List every file except `examples/` and `AUDIT.md`, and search for `curl `, `authorization:`, `bearer `, `api_key`, `content-type:`, and `http` | No hit |
| A7 | List every file except `AUDIT.md`, and search for `sk-`, `ghp_`, `xoxb`, `xoxp`, `xoxa`, `xoxr`, `xoxs`, and `-----BEGIN` | No hit |
| A8 | Read every heading in every file | No concept carries two names, and no two headings name one concept |
| A9 | Recompute each stated count from the file it describes | Every count matches |
| A10 | List every file, collect every backticked path as a reference, and compare the two sets | Every orphan is loaded by a manifest or named in the report; `examples/` is excluded |
| A11 | List every directory | No `evals` directory inside the skill |
| A12 | Search `SKILL.md` for each variant name | No hit |
| A13 | Read the `## ` headings in each file | No heading repeats within one file; fenced blocks are ignored |
| A14 | List every file except `examples/` and `AUDIT.md`, and search for the vague words in the command | Every hit is replaced or recorded as an accepted finding |
| A16 | Find every `check N` reference and open the gate | Every number exists |
| A19 | Read `agents/openai.yaml` and the `SKILL.md` description | `short_description` states the same outcome in fewer words and names no extra branch |
| A20 | Read the description and the opening paragraph | Every property adjective names the mechanism that proves it, or is cut |
| A21 | Read the target `GATE.md`, then run or hand-apply every command against the named fixtures | The clean fixture prints no complaint, the broken fixture prints the documented count, and every check has a command or a named read |

A19 is not applicable when no manifest exists. A16, A18, and A21 are not applicable when the skill has no gate, and the report says so.

A check that names a search term is a detector, not an example.

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
- A16 Check numbers
- A17 Variant capability table
- A18 Step map
- A19 Manifest label
- A20 Claims prove themselves
- A21 The target's gate runs

## Law map

Each law names its check. Some are greps; some are reads.

| Law | Check |
|---|---|
| 1 Placement is the mechanism | A11 |
| 2 Every rule has a check | A16, A18, and the step map |
| 3 One meaning, one place | A8, A13, and R8 in `CRAFT.md` |
| 4 State the loss | read: every transform records its drop in the report's Decisions |
| 5 Recompute every number | A9 |
| 6 Delete before you add | read: the file count after a fix |
| 7 Fix the file that should have prevented it | read: the eval section of the report |
| 8 Say the target, not the ban | A14, and R12 in `CRAFT.md` |
| 9 A claim names its proof | A20 |
| 10 The target proves itself | A21 |

## A1 Frontmatter

```bash
basename "$PWD"
sed -n '1,6p' SKILL.md | grep -E '^(name|description):'
```

Pass when `name` matches `^[a-z0-9]+(-[a-z0-9]+)*$` and equals the folder name.

## A2 Description

Read the description. Pass when it names the outcome in its first clause and lists the modes or branches a person picks it for. A description that opens with "Helps with" fails.

## A3 Line budget

```bash
wc -l SKILL.md
```

Pass under 500. A file over 100 lines needs a contents list; A15 checks it.

## A4 References resolve

```bash
find . -path './examples' -prune -o -type f \
  -exec grep -hoE '`[A-Za-z0-9._/-]+\.(md|txt|yaml|json)`' {} + |
  tr -d '`' | sort -u |
  while read -r f; do [ -e "$f" ] || echo "missing: $f"; done
```

Pass with no hit. `examples/` is excluded because an example shows a shape, and its file names are illustrative.

## A5 No scripts

```bash
find . -type f \( -name '*.py' -o -name '*.sh' -o -name '*.js' -o -name '*.ts' -o -name '*.rb' \)
```

Pass with no hit. A skill delivers text and instructions; a script belongs to the tool that runs it.

## A6 No payload

Search terms, not examples:

```bash
find . -path './examples' -prune -o -type f ! -name 'AUDIT.md' \
  -exec grep -niE 'curl |authorization:|bearer [A-Za-z0-9$]|api[_-]?key *[:=]|content-type:|https?://' {} +
```

Pass with no hit. A request body, a URL, an auth header, and a response field all belong to the tool that makes the call.

`examples/` is excluded because a report may quote the payload it found. R13 in `CRAFT.md` checks that no example quotes a live one.

## A7 No secrets

```bash
find . -type f ! -name 'AUDIT.md' -exec grep -niE '(sk-|ghp_|xox[baprs]-|-----BEGIN)' {} +
```

Pass with no hit.

## A8 One term

```bash
grep -rn '^#' .
```

Read the heading list. This is the one check that needs judgement: pass when no concept carries two names across files, and no two headings name one concept.

## A9 Numbers

Every count in prose is derived. Recompute each one from its artifact:

```bash
wc -l <file>; wc -w <file>; grep -c '<pattern>' <file>
```

Pass when every stated count matches its artifact. A count with no artifact is a claim, not a number.

## A10 Orphans

```bash
tmp="${TMPDIR:-${TEMP:-/tmp}}"
find . -type f | sed 's|^\./||' | sort > "$tmp/skill-files.txt"
grep -rhoE '`[A-Za-z0-9._/-]+`' . | tr -d '`' | sort -u > "$tmp/skill-refs.txt"
comm -23 "$tmp/skill-files.txt" "$tmp/skill-refs.txt" | grep -v '^examples/'
```

Pass when every orphan is loaded by a harness or named in the report. The entry file is always an orphan; a harness manifest, when present, is expected too. `examples/` is excluded: the entry file points at the folder, and the files inside it are illustrative.

## A11 Evals placement

```bash
find . -type d -name evals
```

Pass with no hit. Evals live outside the skill folder.

## A12 Variant leak

For each variant name:

```bash
grep -ni '<target>' SKILL.md
```

Pass with no hit. The core names the variant; it does not carry the variant's mechanism.

## A13 Duplicate headings

Within one file, a heading appears once:

```bash
for f in $(find . -name '*.md'); do
  awk '/^```/{fence=!fence; next} !fence && /^## /' "$f" |
    sort | uniq -d | sed "s|^|$f: |"
done
```

Pass with no hit. Fenced blocks are skipped. A heading repeated across files is a signal, not a failure: R8 decides whether the content is duplicated.

## A14 Vague words

```bash
find . -path './examples' -prune -o -type f ! -name 'AUDIT.md' \
  -exec grep -niE '\b(appropriate|proper|robust|seamless|leverage|utilise|ensure|good|nice)\b' {} +
```

Every hit is replaced with the specific thing. A hit kept on purpose is recorded as an accepted finding in the report.

## A15 Contents list

Every file over 100 lines opens with a contents list. Every heading after it appears in the list, and every list entry names a heading.

A contents list is exempt from R11: it serves the reader, and the model reads the file whole.

## A16 Check numbers

Every reference to a check number resolves.

```bash
find . -path './examples' -prune -o -type f -exec grep -noE 'check [0-9]+' {} +
```

Pass when every number exists in the gate. File names are A4; step numbers are A18. A skill with no gate marks A16 and A18 not applicable, and says so in the report.

## A17 Variant capability table

Read the registry. For each variant it names, the variant opens with a capability table, and every row is keep, translate, or drop.

A skill with no variant marks this not applicable.

## A18 Step map

Read the gate. It carries a step map, every step appears in it, and every check appears at least once.

A skill with no gate marks this not applicable.

## A19 Manifest label

Read the harness manifest. Pass when its short description states the same outcome as the entry file's description, in fewer words, and names no branch the description lacks.

```bash
sed -n 's/^  short_description: "\(.*\)"/\1/p' agents/openai.yaml
sed -n 's/^description: //p' SKILL.md
```

A skill with no manifest marks this not applicable.

## A20 Claims prove themselves

Read the description and the opening paragraph. Every adjective that asserts a property of the output or the process names the mechanism that proves it, or is cut.

```bash
sed -n '3p' SKILL.md
sed -n '/^# /,/^## /p' SKILL.md | head -20
```

The properties to look for: verified, complete, exhaustive, accurate, current, safe, guaranteed, reliable. "Writes one verified report" fails when the only mechanism is a hash over the quote, because the hash proves the quote matches the body and says nothing about where the body came from. "Writes one sourced report" passes, because the sources are the mechanism and the report carries them.

A claim that survives names its proof in the same sentence or in the step that enforces it.

## A21 The target's gate runs

Read the target's `GATE.md`. Run every check by its agent route, from the directory the check names, against the fixtures it names. When a shell is available, also execute every command block as the equivalent route.

```bash
awk '/^```bash/{f=1;next} /^```$/{f=0} f' GATE.md | head -80
```

Pass when the clean fixture prints no complaint, the broken fixture prints exactly the number of complaints the gate documents, and every check's evidence is produced by a command or a named read.

A gate that has never been run is a promise, not a check. A block that errors on a missing file is a finding even when the rule it tests is sound.

A skill with no gate marks this not applicable.
