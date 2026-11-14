---
name: Release Notes
description: Helps with release notes.
---

# Release Notes

Turn a set of merged changes into release notes for the next version.

## Formats

Three formats: short, standard, detailed. Pick one from the version number.

- A patch gets short.
- A minor gets standard.
- A major gets detailed.

## Steps

1. Read the changes.
2. Decide the version bump.
3. Write the notes.
4. Publish.

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

## Publish

Send the notes to the release service.

```bash
curl -X POST https://api.example.com/v1/releases \
  -H "Authorization: Bearer $RELEASE_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"tag_name":"v1.4.0","target_commitish":"main","prerelease":false,"body":"..."}'
```

## Template

Use `TEMPLATE.md` for the body. The template has twelve sections.

## Gate

The gate has eight checks.

1. The version is present.
2. Every change has one sentence.
3. No ticket IDs.
4. The compare link resolves.
5. The upgrade note is present on a major.
6. The notes are under 400 words.

## Formats in detail

See `FORMATS.md` for the format definitions.

## Scripts

Run `scripts/render.py` to produce the final text.
