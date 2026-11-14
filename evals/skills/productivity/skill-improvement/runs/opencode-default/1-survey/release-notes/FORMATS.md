# Formats

Four formats: short, standard, detailed, changelog.

## Short

One line per change.

## Standard

One sentence per change, grouped by area.

## Detailed

A paragraph per change, with the reason.

## Changelog

Every commit, in order, with the author.

## Writing rules

- Lead with the user-visible change.
- Group by area, not by commit.
- One sentence per change.
- Name the version in the first line.
- Keep the past tense.
- No internal ticket IDs.
- No author names.
- Link the compare view.
- End with the upgrade note when the bump is major.
- Spell out acronyms on first use.

## Choosing a format

| Bump | Format |
|---|---|
| patch | short |
| minor | standard |
| major | detailed |
| nightly | changelog |
