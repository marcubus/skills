## Release

- Version: `YYYY.MM.MICRO`
- Tag: `vYYYY.MM.MICRO`

## Checklist

- [ ] `VERSION` holds the release version
- [ ] `CHANGELOG.md` has a `## [YYYY.MM.MICRO] - YYYY-MM-DD` entry, and `## [Unreleased]` is empty
- [ ] `make check`
- [ ] `make tag` created the annotated tag
- [ ] `git push origin main --follow-tags`
- [ ] The `release` workflow published the GitHub release
