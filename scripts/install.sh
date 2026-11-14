#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_DIR="$REPO_ROOT/skills/productivity"

TARGETS=()
ALL=0
MODE="link"
DRY_RUN=0
FORCE=0

SERVER_HOME="${OPENCODE_SERVER_HOME:-/home/opencode}"
SERVER_USER="${OPENCODE_SERVER_USER:-opencode}"
SERVER_GROUP="${OPENCODE_SERVER_GROUP:-opencode}"

HERMES_CONTAINER="${HERMES_CONTAINER:-}"
HERMES_CONTAINER_DEST="${HERMES_DEST:-/opt/data/skills/productivity}"
HERMES_HOST_HOME="${HERMES_HOME:-$HOME/.hermes}"
HERMES_CATEGORY="productivity"
HERMES_FORCE_HOST=0

usage() {
  cat <<'EOF'
Install these skills into one or more agent skill directories.

Usage:
  scripts/install.sh [options]

Targets:
  --target opencode       OpenCode global skills (~/.config/opencode/skills)
  --target agents         Shared agent skills (~/.agents/skills)
  --target server         OpenCode server user (default /home/opencode)
  --target hermes         Hermes host or container
  --all                   opencode, agents, hermes, plus server when present

Options:
  --copy                  Copy files instead of symlinking
  --force                 Replace existing folders
  --dry-run               Print the plan without changing anything
  --list                  List the skills in this repo
  -h, --help              Show this help

Server options:
  --server-home PATH      Server user's home (default /home/opencode)
  --server-user NAME      Server user (default opencode)
  --server-group NAME     Server group (default opencode)

Hermes options:
  --hermes-container NAME Install into a running container (default: auto-detect hermes)
  --hermes-dest PATH      Container skills path (default /opt/data/skills/productivity)
  --hermes-home PATH      Host profile home (default $HERMES_HOME or ~/.hermes)
  --hermes-host           Force a host install, skip container detection

Examples:
  scripts/install.sh --target opencode
  scripts/install.sh --target server --server-home /home/opencode
  scripts/install.sh --target hermes --hermes-container hermes
  scripts/install.sh --all --copy
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

as_root() {
  if (( DRY_RUN )); then
    printf '  sudo %s\n' "$*"
  elif [[ $EUID -eq 0 ]]; then
    "$@"
  elif command -v sudo >/dev/null 2>&1; then
    sudo "$@"
  else
    die "root is required for this target, and sudo is not installed"
  fi
}

add_target() {
  local value="$1" item
  IFS=',' read -r -a items <<<"$value"
  for item in "${items[@]}"; do
    case "$item" in
      all)
        ALL=1
        ;;
      opencode|agents|server|hermes)
        TARGETS+=("$item")
        ;;
      *)
        die "unknown target: $item"
        ;;
    esac
  done
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --target)
      [[ $# -ge 2 ]] || die "--target needs a value"
      add_target "$2"
      shift 2
      ;;
    --all)
      add_target all
      shift
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
    --server-home)
      [[ $# -ge 2 ]] || die "--server-home needs a value"
      SERVER_HOME="$2"
      shift 2
      ;;
    --server-user)
      [[ $# -ge 2 ]] || die "--server-user needs a value"
      SERVER_USER="$2"
      shift 2
      ;;
    --server-group)
      [[ $# -ge 2 ]] || die "--server-group needs a value"
      SERVER_GROUP="$2"
      shift 2
      ;;
    --hermes-container)
      [[ $# -ge 2 ]] || die "--hermes-container needs a value"
      HERMES_CONTAINER="$2"
      shift 2
      ;;
    --hermes-dest)
      [[ $# -ge 2 ]] || die "--hermes-dest needs a value"
      HERMES_CONTAINER_DEST="$2"
      shift 2
      ;;
    --hermes-home)
      [[ $# -ge 2 ]] || die "--hermes-home needs a value"
      HERMES_HOST_HOME="$2"
      shift 2
      ;;
    --hermes-host)
      HERMES_FORCE_HOST=1
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
while IFS= read -r -d '' skill_dir; do
  SKILL_DIRS+=("$skill_dir")
done < <(find "$SKILLS_DIR" -mindepth 1 -maxdepth 1 -type d -print0 | sort -z)

[[ ${#SKILL_DIRS[@]} -gt 0 ]] || die "no skills found in $SKILLS_DIR"

if [[ "${LIST:-0}" -eq 1 ]]; then
  for skill_dir in "${SKILL_DIRS[@]}"; do
    basename "$skill_dir"
  done
  exit 0
fi

if [[ "$ALL" -eq 1 ]]; then
  TARGETS+=(opencode agents hermes)
  if [[ -d "$SERVER_HOME" ]]; then
    TARGETS+=(server)
  fi
fi

[[ ${#TARGETS[@]} -gt 0 ]] || TARGETS=(opencode)

dedupe_targets() {
  local -A seen=()
  local target
  local -a unique=()
  for target in "${TARGETS[@]}"; do
    if [[ -z "${seen[$target]:-}" ]]; then
      seen[$target]=1
      unique+=("$target")
    fi
  done
  TARGETS=("${unique[@]}")
}
dedupe_targets

install_local() {
  local dest="$1" mode="$2" root="${3:-0}" owner="${4:-}"
  local skill_dir name target

  if [[ "$root" == "1" ]]; then
    as_root mkdir -p "$dest"
  else
    run mkdir -p "$dest"
  fi

  for skill_dir in "${SKILL_DIRS[@]}"; do
    name="$(basename "$skill_dir")"
    target="$dest/$name"

    if [[ -e "$target" && ! -L "$target" && "$FORCE" -ne 1 ]]; then
      note "skip $target (exists, use --force to replace)"
      continue
    fi

    if [[ "$root" == "1" ]]; then
      as_root rm -rf "$target"
      if [[ "$mode" == "copy" ]]; then
        as_root cp -R "$skill_dir" "$target"
        if [[ -n "$owner" ]]; then
          as_root chown -R "$owner" "$target"
        fi
      else
        as_root ln -s "$skill_dir" "$target"
      fi
    else
      run rm -rf "$target"
      if [[ "$mode" == "copy" ]]; then
        run cp -R "$skill_dir" "$target"
      else
        run ln -s "$skill_dir" "$target"
      fi
    fi

    note "$mode $name -> $dest"
  done
}

install_hermes_container() {
  local container="$1" dest="$2"
  local skill_dir name target

  run docker exec "$container" mkdir -p "$dest"

  for skill_dir in "${SKILL_DIRS[@]}"; do
    name="$(basename "$skill_dir")"
    target="$dest/$name"
    run docker exec "$container" rm -rf "$target"
    run docker cp "$skill_dir" "$container:$target"
    note "copy $name -> $container:$dest"
  done
}

hermes_container_running() {
  local name="$1"
  command -v docker >/dev/null 2>&1 || return 1
  docker ps --format '{{.Names}}' 2>/dev/null | grep -qx "$name"
}

for target in "${TARGETS[@]}"; do
  case "$target" in
    opencode)
      dest="${XDG_CONFIG_HOME:-$HOME/.config}/opencode/skills"
      install_local "$dest" "$MODE"
      ;;
    agents)
      install_local "$HOME/.agents/skills" "$MODE"
      ;;
    server)
      [[ -d "$SERVER_HOME" ]] || die "server home not found: $SERVER_HOME (pass --server-home)"
      install_local "$SERVER_HOME/.config/opencode/skills" "$MODE" 1 "$SERVER_USER:$SERVER_GROUP"
      ;;
    hermes)
      if [[ "$HERMES_FORCE_HOST" -eq 0 ]]; then
        if [[ -z "$HERMES_CONTAINER" ]] && hermes_container_running hermes; then
          HERMES_CONTAINER="hermes"
        fi
        if [[ -n "$HERMES_CONTAINER" ]]; then
          install_hermes_container "$HERMES_CONTAINER" "$HERMES_CONTAINER_DEST"
          continue
        fi
      fi

      dest="$HERMES_HOST_HOME/skills/$HERMES_CATEGORY"
      if [[ -d "$HERMES_HOST_HOME" && ! -w "$HERMES_HOST_HOME" ]]; then
        owner="$(stat -c '%u:%g' "$HERMES_HOST_HOME" 2>/dev/null || printf '')"
        install_local "$dest" "copy" 1 "$owner"
      else
        install_local "$dest" "copy"
      fi
      ;;
  esac
done

note ""
note "Installed from $REPO_ROOT"
note "Restart the target agent or start a new session so it discovers the skills."
