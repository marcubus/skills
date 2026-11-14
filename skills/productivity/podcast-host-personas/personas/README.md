# Local store

Generated profiles live here and nowhere else. This folder is yours, not the skill's.

Everything in it is gitignored except this file and `.gitignore`, so a persona you generate never lands in the repository and never blocks an update to the skill. The skill ships the rules for building a persona; it does not ship anybody's persona.

The folder is created on first build, along with `index.jsonl`. An empty index means an empty store, which is the state before your first persona.

## What belongs here

- `personas/<id>.md`, one generated profile per file, named for its id.
- `personas/index.jsonl`, one JSON line per stored profile. The distinctness gate reads this file, so a profile without a line is invisible to it and will duplicate silently.

## What does not

- Worked examples. Those live in `examples/`, are tracked, and carry no index line.
- Anything you want to keep across a reinstall. A fresh install of the skill replaces this folder, so copy it out first, or keep the store outside the skill folder and name it in the brief. A named store replaces `personas/` for that build.
