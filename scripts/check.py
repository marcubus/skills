#!/usr/bin/env python3
"""Repository checks. Runs in CI and from `make check`.

Stdlib only, so a fresh clone can run it with no install step.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FAILURES: list[str] = []


def fail(check: str, message: str) -> None:
    FAILURES.append(f"{check}: {message}")


def tracked(*paths: str) -> list[Path]:
    out = subprocess.run(
        ["git", "ls-files", "-z", "--", *paths],
        cwd=ROOT,
        capture_output=True,
        check=True,
    ).stdout.decode()
    return [ROOT / p for p in out.split("\0") if p]


def read_frontmatter(path: Path) -> dict[str, str] | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line or line.startswith((" ", "\t", "#")):
            continue
        key, sep, value = line.partition(":")
        if sep:
            fields[key.strip()] = value.strip()
    return fields


def check_frontmatter() -> None:
    skill_files = sorted((ROOT / "skills").glob("*/*/SKILL.md"))
    if not skill_files:
        fail("A1", "no skills/*/*/SKILL.md found")
    for path in skill_files:
        rel = path.relative_to(ROOT)
        fields = read_frontmatter(path)
        if fields is None:
            fail("A1", f"{rel}: missing a leading --- frontmatter block")
            continue
        for key in ("name", "description"):
            value = fields.get(key)
            if not value:
                fail("A1", f"{rel}: frontmatter has no {key}")
            elif not (value.startswith('"') and value.endswith('"')):
                fail(
                    "A1",
                    f"{rel}: {key} must be quoted; an unquoted colon and space breaks YAML",
                )
        name = fields.get("name", "").strip('"')
        if name and name != path.parent.name:
            fail("A1", f"{rel}: name {name!r} does not match folder {path.parent.name!r}")


def check_manifests() -> None:
    plugin_path = ROOT / ".claude-plugin" / "plugin.json"
    market_path = ROOT / ".claude-plugin" / "marketplace.json"
    for path in (plugin_path, market_path):
        if not path.exists():
            fail("A2", f"{path.relative_to(ROOT)}: missing")
            return
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            fail("A2", f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
            return

    plugin = json.loads(plugin_path.read_text(encoding="utf-8"))
    listed: set[Path] = set()
    for entry in plugin.get("skills", []):
        skill_dir = (ROOT / entry).resolve()
        listed.add(skill_dir)
        if not (skill_dir / "SKILL.md").is_file():
            fail("A2", f"plugin.json lists {entry}, which has no SKILL.md")

    for path in sorted((ROOT / "skills").glob("*/*/SKILL.md")):
        if path.parent.resolve() not in listed:
            fail("A2", f"{path.parent.relative_to(ROOT)} is not listed in plugin.json")


LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


def check_links() -> None:
    for path in tracked("*.md"):
        rel = path.relative_to(ROOT)
        # Eval fixtures are synthetic repositories. Their links are content under
        # test, and a scenario may deliberately point at a file it has not created.
        if rel.parts[0] == "evals":
            continue
        in_fence = False
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            for target in LINK.findall(line):
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                clean = target.split("#", 1)[0]
                if not clean:
                    continue
                candidates = [path.parent / clean, ROOT / clean]
                if not any(c.exists() for c in candidates):
                    fail("A3", f"{rel}:{lineno}: link target {target} does not exist")


def check_version() -> None:
    version_path = ROOT / "VERSION"
    if not version_path.exists():
        fail("A4", "VERSION is missing")
        return
    version = version_path.read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"\d{4}\.\d{2}\.\d+", version):
        fail("A4", f"VERSION {version!r} is not CalVer YYYY.MM.MICRO")
        return
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    if f"## [{version}]" not in changelog:
        fail("A4", f"CHANGELOG.md has no '## [{version}]' entry")


SECRETS = re.compile(
    r"(sk-[A-Za-z0-9]{16,}|ghp_[A-Za-z0-9]{20,}|xox[baprs]-[A-Za-z0-9-]{10,}"
    r"|-----BEGIN [A-Z ]*PRIVATE KEY-----)"
)


def check_secrets() -> None:
    for path in tracked():
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for lineno, line in enumerate(text.splitlines(), 1):
            if SECRETS.search(line):
                fail("A5", f"{path.relative_to(ROOT)}:{lineno}: looks like a secret")


def check_local_only() -> None:
    for path in tracked("reviews", "skills/*/*/personas"):
        rel = path.relative_to(ROOT)
        if rel.parts[0] == "reviews":
            fail("A6", f"{rel} is tracked; review reports stay local")
        elif rel.name not in {"README.md", ".gitignore"}:
            fail("A6", f"{rel} is tracked; a generated persona stays local")


def main() -> int:
    check_frontmatter()
    check_manifests()
    check_links()
    check_version()
    check_secrets()
    check_local_only()

    if FAILURES:
        for line in FAILURES:
            print(line, file=sys.stderr)
        print(f"\n{len(FAILURES)} check(s) failed", file=sys.stderr)
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
