# Output

Where reports are written. This file is optional.

Copy it to `OUTPUT.local.md` beside `SKILL.md`, or to `$XDG_CONFIG_HOME/deep-research/OUTPUT.md`, and set one line. On Windows, use `%APPDATA%\deep-research\OUTPUT.md`.

```
reports_dir: ~/notes/reports
```

Rules:

- The path may be absolute, start with `~`, or use a Windows variable such as `%USERPROFILE%`.
- `OUTPUT.local.md` is gitignored. Keep a personal path in it and commit only `OUTPUT.example.md`.