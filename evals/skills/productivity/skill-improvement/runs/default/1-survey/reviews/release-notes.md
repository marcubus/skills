# Review: release-notes

## Verdict

Phase 1, stopped: 1 blocker, 11 majors, 1 minor. The fixture is untouched.

## Contract

Given a set of merged changes and a version bump, the skill produces release notes in one of four formats, by grouping changes by area and writing one sentence per change.

The skill delivers text. The publish step it describes belongs to the caller.

## Inventory

| File | Lines | Role | Points at |
|---|---|---|---|
| `SKILL.md` | 70 | entry | `FORMATS.md`, `TEMPLATE.md`, `scripts/render.py` |
| `FORMATS.md` | 41 | reference | none |
| `scripts/render.py` | 4 | script | none |
| `evals/README.md` | 4 | fixture | none |

## Findings

| id | severity | file:line | what | why | fix |
|---|---|---|---|---|---|
| F1 | blocker | `SKILL.md:43-46` | A `curl` call with a URL, an auth header, a content type, and a request body | A6 no payload | Delete the block. The skill delivers the notes; the caller sends them |
| F2 | major | `SKILL.md:2` | `name: Release Notes` | A1 frontmatter | `name: release-notes` |
| F3 | major | `SKILL.md:3` | "Helps with release notes." | A2, R1 | Name the outcome and the branches: merged changes, a version bump, one of four formats |
| F4 | major | `SKILL.md:12`, `FORMATS.md:3` | Three formats in the entry file, four in the reference | Law 3 | One format table in `FORMATS.md`; the entry file points at it |
| F5 | major | `SKILL.md:51` | Points at `TEMPLATE.md`, which does not exist | A4 | Supply the template, or remove the pointer and the count |
| F6 | major | `scripts/render.py` | An executable inside the skill | A5 | Delete it. The skill delivers text |
| F7 | major | `evals/README.md` | An eval folder inside the skill | A11, law 1 | Delete it. Evals live outside the skill |
| F8 | major | `SKILL.md:55` | "The gate has eight checks", then six | Law 5 | Recompute the count after the gate is finished |
| F9 | major | `SKILL.md:33` | "No author names" has no gate check | Law 2 | Add the check, or drop the rule |
| F10 | major | `SKILL.md:46` | Release-service field names in the core file | A12 | Remove them with the payload |
| F11 | minor | `SKILL.md:25-35`, `FORMATS.md:21-30` | The ten writing rules appear twice | Law 3 | One home in `FORMATS.md`; the entry file points at it |
| F12 | major | `SKILL.md:18-23` | Four steps with no completion criterion | R6 | End each step on a checkable condition |
| F13 | major | `SKILL.md:55-64` | Six checks, no step map, and no check for the format choice, the grouping, or the acronym rule | Law 2 | Rebuild the gate: one check per rule, a step map, and a brought-in path |

## Fact table

| Fact | Where it appears | Single source |
|---|---|---|
| The format enum | `SKILL.md:12`, `FORMATS.md:3`, `FORMATS.md:34-40` | `FORMATS.md` |
| The writing rules | `SKILL.md:25-35`, `FORMATS.md:21-30` | `FORMATS.md` |
| The gate size | `SKILL.md:55` | the gate itself |
| The template sections | `SKILL.md:51` | `TEMPLATE.md`, which is missing |

## Rounds

| Round | Blockers | Majors | Minors | Exit |
|---|---|---|---|---|
| 1 | 1 | 11 | 1 | stopped after survey |

## Evals

| Scenario | Result | Evidence |
|---|---|---|
| 1 main path | not run | phase 1 |
| 2 variant | not run | phase 1 |
| 3 gate alone | not run | phase 1 |

## Audit

| Check | Command | Hits |
|---|---|---|
| A1 frontmatter | name grep | 1 |
| A4 references | reference grep | 1 |
| A5 scripts | find | 1 |
| A6 payload | payload grep | 3 lines |
| A11 evals | find -type d -name evals | 1 |
| A13 duplicate headings | heading sort | 1 |

## State

| Item | Value |
|---|---|
| Blockers | 1 |
| Majors | 11 |
| Minors | 1 |
| Phase reached | 1 |
| Done | no |
