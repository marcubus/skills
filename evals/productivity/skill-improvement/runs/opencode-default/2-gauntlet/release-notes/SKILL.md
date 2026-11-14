---
name: release-notes
description: Turns merged changes into release notes in one of four formats. Use when a release needs notes, a changelog entry, or a version summary for users.
---

# Release notes

Turn merged changes into notes a user can act on. The skill delivers text. Publishing belongs to the caller.

## Steps

1. Read the changes. Done when every merged change has a summary line and an area.
2. Choose the format. Done when `FORMATS.md` names the format for this bump, and the reason is recorded.
3. Write the notes. Done when every change has one sentence, grouped by area, in every section of `TEMPLATE.md`.
4. Check the notes. Done when all eight checks pass.

## Rules

`FORMATS.md` holds the ten rules. Read them before step 3.

## Template

`TEMPLATE.md` holds the nine sections and their order. Every section appears, even when empty.

## Gate

### 1. Version present

The first line names the version. Done when the version matches the bump in step 2.

### 2. One sentence per change

Done when no change carries two sentences and no sentence carries two changes.

### 3. Format matches the bump

Done when the format is the one `FORMATS.md` gives for this bump.

### 4. Grouped by area

Done when no area appears twice and no group is a commit hash.

### 5. No ticket IDs

Done when no internal ticket identifier appears in the notes.

### 6. No author names

Done when no author name appears in the notes.

### 7. Acronyms spelled out

Done when every acronym is spelled out at first use.

### 8. Length

Done when short and standard are under 400 words, and detailed and changelog are under 800.

## Step map

| Step | Checks |
|---|---|
| 1 Read the changes | 2 |
| 2 Choose the format | 3 |
| 3 Write the notes | 1, 4, 5, 6, 7, 8 |
| 4 Check the notes | 1 to 8 |

A brought-in note enters at step 4 and runs checks 3 to 8.

## Voice

Write for the person upgrading, not the person who wrote the change. Name the effect, not the implementation. A fix that nobody can see belongs in the changelog, not the summary.
