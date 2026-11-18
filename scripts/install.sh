#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_DIR="$REPO_ROOT/skills/productivity"

DESTS=()
MODE="link"
DRY_RUN=0
FORCE=0
LIST=0

usage() {
  cat <<'EOF'
Install these skills into any agent skill directory.

Usage:
  scripts/install.sh --dest PATH [--dest PATH ...] [options]

Options:
  --dest PATH    Directory an agent reads skills from. Repeatable.
  --copy         Copy files instead of symlinking
  --force        Replace existing folders
  --dry-run      Print the plan without changing anything
  --list         List the skills in this repo
  -h, --help     Show this help

On Windows, run this from WSL or Git Bash. Use --copy when symlinks
are unavailable. Windows variables such as %USERPROFILE% are expanded.

Examples:
  scripts/install.sh --dest ~/.config/opencode/skills
  scripts/install.sh --dest ~/.claude/skills --dest ~/.agents/skills
  scripts/install.sh --dest ~/.agents/skills --copy
EOF
}

die() {
  printf 'error: %s\n' "$*" >&2
  exit 1
}

note() {
  printf '%s\n' "$*"
}

run() {
  if (( DRY_RUN )); then
    printf '  %s\n' "$*"
  else
    "$@"
  fi
}

expand_dest() {
  local path="$1"
  case "$path" in
    "~") path="$HOME" ;;
    "~/"*) path="$HOME/${path#\~/}" ;;
    "%USERPROFILE%"*) path="${USERPROFILE:-$HOME}${path#%USERPROFILE%}" ;;
    "%APPDATA%"*) path="${APPDATA:-$HOME/AppData/Roaming}${path#%APPDATA%}" ;;
    "%LOCALAPPDATA%"*) path="${LOCALAPPDATA:-$HOME/AppData/Local}${path#%LOCALAPPDATA%}" ;;
  esac
  path="${path//\\//}"
  printf '%s\n' "$path"
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dest)
      [[ $# -ge 2 ]] || die "--dest needs a value"
      DESTS+=("$(expand_dest "$2")")
      shift 2
      ;;
    --copy)
      MODE="copy"
      shift
      ;;
    --link)
      MODE="link"
      shift
      ;;
    --force)
      FORCE=1
      shift
      ;;
    --dry-run)
      DRY_RUN=1
      shift
      ;;
    --list)
      LIST=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      die "unknown option: $1"
      ;;
  esac
done

[[ -d "$SKILLS_DIR" ]] || die "skills directory not found: $SKILLS_DIR"

SKILL_DIRS=()
for skill_dir in "$SKILLS_DIR"/*/; do
  [[ -d "$skill_dir" ]] || continue
  SKILL_DIRS+=("${skill_dir%/}")
done

[[ ${#SKILL_DIRS[@]} -gt 0 ]] || die "no skills found in $SKILLS_DIR"

if (( LIST )); then
  for skill_dir in "${SKILL_DIRS[@]}"; do
    basename "$skill_dir"
  done
  exit 0
fi

[[ ${#DESTS[@]} -gt 0 ]] || die "no destination given; pass --dest PATH (see --help)"

install_local() {
  local dest="$1" mode="$2"
  local skill_dir name target installed_mode

  run mkdir -p "$dest"

  for skill_dir in "${SKILL_DIRS[@]}"; do
    name="$(basename "$skill_dir")"
    target="$dest/$name"
    installed_mode="$mode"

    if [[ -e "$target" && ! -L "$target" && "$FORCE" -ne 1 ]]; then
      note "skip $target (exists, use --force to replace)"
      continue
    fi

    run rm -rf "$target"
    if [[ "$mode" == "copy" ]]; then
      run cp -R "$skill_dir" "$target"
    elif (( DRY_RUN )); then
      printf '  ln -s %s %s\n' "$skill_dir" "$target"
    elif ! ln -s "$skill_dir" "$target" 2>/dev/null; then
      note "symlink unavailable; copying $name instead"
      cp -R "$skill_dir" "$target"
      installed_mode="copy"
    fi

    note "$installed_mode $name -> $dest"
  done
}

for dest in "${DESTS[@]}"; do
  install_local "$dest" "$MODE"
done

note ""
note "Installed from $REPO_ROOT"
note "Restart the target agent or start a new session so it discovers the skills."
