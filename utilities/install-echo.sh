#!/usr/bin/env bash
# install-echo.sh — install a distilled echo from examples/ into a Claude Code skills directory.
#
# Usage:
#   ./utilities/install-echo.sh <echo-name> [--project | --home]
#
#   --project   install into ./.claude/skills/<echo-name>/   (default; current project only)
#   --home      install into ~/.claude/skills/<echo-name>/   (every project on this machine)
#
# Examples:
#   ./utilities/install-echo.sh nietzsche-echo --project
#   ./utilities/install-echo.sh socrates-echo --home

set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "usage: $0 <echo-name> [--project | --home]" >&2
  echo "available echoes:" >&2
  ls -1 "$(dirname "$0")/../examples" | sed 's/^/  /' >&2
  exit 1
fi

echo_name="$1"
scope="${2:---project}"

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
src="$repo_root/examples/$echo_name"

if [[ ! -d "$src" ]]; then
  echo "error: $src not found" >&2
  echo "available echoes:" >&2
  ls -1 "$repo_root/examples" | sed 's/^/  /' >&2
  exit 1
fi

case "$scope" in
  --project)
    dest_root="$repo_root/.claude/skills"
    ;;
  --home)
    dest_root="$HOME/.claude/skills"
    ;;
  *)
    echo "error: unknown scope $scope (use --project or --home)" >&2
    exit 1
    ;;
esac

dest="$dest_root/$echo_name"

if [[ -e "$dest" ]]; then
  echo "error: $dest already exists — remove it first if you want to reinstall" >&2
  exit 1
fi

mkdir -p "$dest_root"
cp -r "$src" "$dest"
echo "installed: $echo_name → $dest"
echo "activate by opening Claude Code and saying: from ${echo_name%-echo}'s perspective, ..."
