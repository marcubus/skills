# Review: release-notes

## Verdict

Phase 5, done: 0 blockers, 0 majors, 0 minors.

## Contract

Given merged changes and a version bump, the skill produces release notes in one of four formats, by grouping changes by area and writing one sentence per change.

The skill delivers text. Publishing belongs to the caller.

## Inventory

| File | Lines | Role | Points at |
|---|---|---|---|
| `SKILL.md` | 72 | entry | `FORMATS.md`, `TEMPLATE.md` |
| `FORMATS.md` | 41 | reference | none |
| `TEMPLATE.md` | 39 | reference | none |

## Findings

All thirteen findings from the survey are closed.

| id | severity | file:line | what | fix |
|---|---|---|---|---|
| F1 | blocker | `SKILL.md:43-46` | Request body, endpoint, auth header | Deleted. The skill delivers text; the caller sends it |
| F2 | major | `SKILL.md:2` | `name: Release Notes` | `name: release-notes` |
| F3 | major | `SKILL.md:3` | "Helps with release notes." | Outcome first, then the three branches |
| F4 | major | `SKILL.md:12` | Three formats, four in the reference | One table in `FORMATS.md`; the entry file names it |
| F5 | major | `SKILL.md:51` | Pointer to a missing template | `TEMPLATE.md` supplied, nine sections |
| F6 | major | `scripts/render.py` | Script inside the skill | Deleted |
| F7 | major | `evals/README.md` | Evals inside the skill | Deleted |
| F8 | major | `SKILL.md:55` | Eight checks claimed, six listed | Gate rebuilt with eight, count recomputed |
| F9 | major | `SKILL.md:33` | "No author names" with no check | Check 6 |
| F10 | major | `SKILL.md:46` | Release-service field names | Removed with the payload |
| F11 | minor | `SKILL.md:25-35` | Ten rules in two files | One home in `FORMATS.md` |
| F12 | major | `SKILL.md:18-23` | Steps with no completion criterion | Every step ends on a checkable condition |
| F13 | major | `SKILL.md:55-64` | No step map, no check for format or grouping | Step map added; checks 3 and 4 added |

## Rounds

| Round | Blockers | Majors | Minors | Exit |
|---|---|---|---|---|
| 1 | 1 | 11 | 1 | continue |
| 2 | 0 | 0 | 0 | gauntlet ends |

## Evals

| Scenario | Result | Evidence |
|---|---|---|
| 1 main path | not run | the fixture has no input |
| 2 variant | not run | the fixture has no input |
| 3 gate alone | not run | the fixture has no input |

The gate can be run on a brought-in note, but the fixture ships no note. Building the eval suite is phase 4 work and was not asked for here.

## Audit

| Check | Command | Hits |
|---|---|---|
| A1 frontmatter | name grep | 0 |
| A3 line budget | `wc -l SKILL.md` | 72 |
| A4 references | reference grep | 0 |
| A5 scripts | find | 0 |
| A6 payload | payload grep | 0 |
| A10 orphans | comm | 1, the entry file |
| A11 evals | find | 0 |
| A12 variant leak | target grep | 0 |
| A13 duplicate headings | heading sort | 0 |
| A14 vague words | vague grep | 0 |
| A15 contents | read | 0, no file over 100 lines |
| A16 cross-references | check-number grep | 0 |

## Decisions

- The publish step is gone rather than moved to a variant file. A release skill that posts to a service has to hold a credential; the skill delivers text and the caller publishes. The loss is recorded here.
- `TEMPLATE.md` is supplied rather than the pointer removed. The template carries the nine-section order the notes depend on.
- The changelog format keeps every commit but no longer names the author, because rule seven bans author names. The loss is recorded here.

## State

| Item | Value |
|---|---|
| Blockers | 0 |
| Majors | 0 |
| Minors | 0 |
| Phase reached | 5 |
| Done | yes |
