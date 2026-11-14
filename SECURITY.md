# Security policy

This repository is prose and shell, not a service, so the realistic risks are
small but real: a secret pasted into an example, a persona that impersonates a
living person, or an installer that writes outside the directory it was told to.

## Reporting a vulnerability

Open a private security advisory on GitHub:

<https://github.com/marcubus/skills/security/advisories/new>

If that is unavailable, contact the maintainer directly. Please do not open a
public issue for anything that could expose a credential or a private
transcript.

Include:

- the commit you ran,
- the skill and the agent or model,
- the input, with private text removed,
- what happened, and what you expected.

## Never paste

- API keys or bearer tokens of any kind,
- private transcripts or persona briefs you do not want published,
- anything from a `personas/` store or a `reviews/` report that is not yours.

## What is in scope

- `scripts/install.sh` and `scripts/check.py`.
- Skill instructions that would make an agent exfiltrate data, run a destructive
  command, or ignore a refusal it should keep.
- Content that impersonates a real living person, or reproduces copyrighted text.

Out of scope: the behaviour of a third-party agent or model reading a skill, and
the output of a speech engine a skill targets. Report those upstream.

## Supported versions

Only the latest commit on `main` is supported. Fixes ship as new commits and, for
anything material, a new CalVer release. Pin a commit SHA or a tag if you need
reproducibility.
