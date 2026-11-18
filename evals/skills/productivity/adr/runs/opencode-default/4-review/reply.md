# Review — ADR-0004 Session storage

Run folder: `runs/opencode-default/4-review/`
Record: `docs/adr/0004-session-storage.md`
Mode: **review** (brought-in work — this skill did not write this record, so C8 is skipped and the record keeps whatever shape the repo gave it).

## What I read

- `docs/adr/0004-session-storage.md` — the record.
- `docs/adr/` — one file only. No `README.md` index, no `0001`–`0003`, no `0012-cookie-signing.md`.
- `0012-cookie-signing.md` — **does not exist**, so the record's only outbound reference could not be opened (see C6).

## Gate result

| Check | Result | Evidence |
|---|---|---|
| C1 Filename | **pass** | `docs/adr/0004-session-storage.md` — four digits, hyphenated lowercase slug; the grep prints nothing. |
| C2 Number | **pass** | Directory holds only `0004`; no duplicate numbers, highest is `0004`. |
| C3 Status | **pass (mechanical) / FAIL (substantive)** | `**Status:** accepted` matches the allowed set. But `accepted` means "implemented", and the repo holds no implementation. See routing below. |
| C4 Status block | **pass** | `Status`, `Date`, `Author` in that order at lines 3–5; `Date` is `2026-08-14`. |
| C5 Core sections | **pass after fix** | Was `Decision → Context → Considered options → Consequences`. Now `Context → Decision → Considered options → Consequences`. |
| C6 Links resolve | **pass after fix** | Was `broken: 0012-cookie-signing.md` and `missing: ADR-0012`. Both commands now print nothing. |
| C7 Index row | **not applicable** | `docs/adr/README.md` does not exist; the repo keeps no index. |
| C8 Implemented shape | **skipped** | Brought-in work (GATE.md, "Brought-in work"). Reported anyway under routing: the record is `accepted` but carries neither `**Implemented:**` nor `## Implementation`. |
| C9 No secret | **pass after fix** | Line 29 was `SESSION_KEY=hunter2-not-real` — a key assignment with a value. Removed. |
| C10 Title states the decision | **FAIL** | `# Session storage` is a topic noun with no verb. |
| C11 Context names the trigger | **FAIL** | Line 9 gives background only ("has a login page and a settings page", "previously kept in a module-level dictionary"). No event or constraint that forced the decision *now*. |
| C12 Every option lost for a reason | **FAIL** | One alternative at line 18: "This was the other candidate" — no reason it lost. A second alternative is required. |
| C13 A cost is named | **FAIL** | All three Consequences (lines 22–24) are benefits. Nothing is given up. |
| C14 Every claim has proof | **FAIL** | The only external fact cited was the dangling ADR-0012 link, now removed. Lines 22–24 are unsupported assertions; `SESSION_KEY` is named with no file or command proving where it is read. |
| C15 One decision | **pass** | Rule 2 (key source) is a detail of rule 1, not a second choice. |
| C16 Unknowns are labelled | **FAIL** | No `## Open questions`. Line 24 asserts a second worker exists; key rotation and the framework signing helper are treated as settled. |
| C17 No padding | **pass after fix** | `## Configuration` (old line 26) is not a ladder section and held only a secret. Removed with the C9 fix. |
| C18 No duplicate decision | **pass** | `0004` is the only record in the directory; nothing else decides session storage. |

## Editorial fixes applied (diff)

### 1. C5 — core sections out of order

Context must precede Decision.

```diff
-## Decision
-
-1. Session state is stored in a signed cookie, not server-side.
-2. The signing key comes from `SESSION_KEY` in the environment.
-
 ## Context
 
 The web front end has a login page and a settings page. Sessions were previously kept in a module-level dictionary. Cookies are a familiar mechanism and the framework already has a signing helper.
 
+## Decision
+
+1. Session state is stored in a signed cookie, not server-side.
+2. The signing key comes from `SESSION_KEY` in the environment.
+
 ## Considered options
```

No wording changed, only the order of the two sections.

### 2. C6 — dangling reference to ADR-0012

Old line 14 pointed at `0012-cookie-signing.md`, which is not in `docs/adr/`. The `ADR-0012` mention also failed the number check. Removed the sentence:

```diff
-The web front end has a login page and a settings page. Sessions were previously kept in a module-level dictionary. Cookies are a familiar mechanism and the framework already has a signing helper. The relevant background is in [ADR-0012](0012-cookie-signing.md).
+The web front end has a login page and a settings page. Sessions were previously kept in a module-level dictionary. Cookies are a familiar mechanism and the framework already has a signing helper.
```

If `0012-cookie-signing.md` exists in a wider corpus and was meant to be copied in beside this record, restore the link rather than the sentence — the reference is the only proof the record had (C14).

### 3. C9 (and C17) — secret value in the record

Old lines 26–29 held a `## Configuration` section whose entire content was a key assignment:

```diff
-## Configuration
-
-```bash
-SESSION_KEY=hunter2-not-real
-```
```

The section is not on the optional ladder and carried nothing but the value. `SESSION_KEY` is still named in Decision rule 2, which is the form C9 asks for. The file now ends at the Consequences list.

## Substantive findings routed

Per SKILL.md review step 4, these are not edited here. Each takes the amendment-or-successor rule in FORMAT.md, which is write mode. The record is `accepted`, so the vehicle is an **amendment** — except where noted.

| Check | File:line | Smallest fix | Vehicle |
|---|---|---|---|
| C3 | `docs/adr/0004-session-storage.md:3` | `accepted` claims implementation, but the repo contains no code, no diff and no `## Implementation`. Either flip to `proposed` until the change lands, or name the files and commands that carried it out. **Left for the implementer.** | implementer defect |
| C8 | same file, after line 5 | If `accepted` stands, add `**Implemented:** YYYY-MM-DD` after `Author` and a `## Implementation` section naming the session module and the settings file. Skipped as a check because this record is brought-in work; reported because the status depends on it. | implementer defect |
| C10 | line 1 | Retitle to a phrase with a verb: `# Store session state in a signed cookie`. | amendment |
| C11 | line 9 | Name the trigger: the deployment moved to more than one worker, so the module-level dictionary stopped being shared. State it as the reason the decision came due. | amendment |
| C12 | line 18 | Add the reason Redis lost (an extra service to run and back up, for a session payload of a few hundred bytes), and add a second alternative — a database table — with its reason. | amendment |
| C13 | lines 22–24 | Add the cost: the session cannot be revoked before it expires, and the cookie grows with every field added to it. | amendment |
| C14 | lines 22–24 | Cite the proof for each claim: the signing helper's module path, and the file that reads `SESSION_KEY`. Drop or source the "second worker" claim. | amendment |
| C16 | end of file | Add `## Open questions` for key rotation and for whether more than one worker is actually deployed. If the multi-worker premise is unsettled, the record cannot stay `accepted`. | amendment |
| C18 | — | Nothing to do; recorded as passing. | — |

## Note on the record's status

C3 and C8 point the same way: the record says `accepted` while nothing in the repository shows the decision was built. FORMAT.md's lifecycle table makes the evidence decide, not the tense of the request, and a change that has only partly landed is `proposed`. I did not change the status — review mode leaves C3 and C8 to the implementer — but the amendment above should not be written against an `accepted` record until that evidence exists.
