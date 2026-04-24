#!/usr/bin/env python3
"""Scaffold a new echo directory under .claude/skills/<slug>-echo/.

Creates the 7-directory + 6-stub layout the Echo workflow expects, so Phase 0.5
is a one-command step instead of seven bash invocations.

Usage:
    python utilities/scaffold_echo.py sun-tzu
    python utilities/scaffold_echo.py marcus-aurelius --theme   # theme echo
    python utilities/scaffold_echo.py <slug> --force             # overwrite

What it does NOT do: fill semantic content. Mental models, era-assumptions,
heuristics, and voice are judgment work that stays with the main orchestrator.
This only creates empty scaffolding so the orchestrator can't forget a folder.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

RESEARCH_STUBS = [
    ("01-primary-works.md", "# Agent 1 — Primary Works\n\n<!-- Populate via research agent. -->\n"),
    ("02-contemporary-records.md", "# Agent 2 — Contemporary Records\n\n<!-- Populate via research agent. -->\n"),
    ("03-letters-sayings.md", "# Agent 3 — Letters / Sayings / Voice\n\n<!-- Populate via research agent. -->\n"),
    ("04-scholarly-biographies.md", "# Agent 4 — Modern Critical Scholarship\n\n<!-- Populate via research agent. -->\n"),
    ("05-era-context.md", "# Agent 5 — Era Context\n\n<!-- Populate via research agent. -->\n"),
    ("06-reception-history.md", "# Agent 6 — Reception History\n\n<!-- Populate via research agent. -->\n"),
]

SOURCE_DIRS = ["primary", "translations", "scholarship"]


def scaffold(slug: str, is_theme: bool, force: bool) -> int:
    suffix = "-framework" if is_theme else "-echo"
    root = REPO_ROOT / ".claude" / "skills" / f"{slug}{suffix}"

    if root.exists() and not force:
        print(f"error: {root} already exists (use --force to overwrite stubs)", file=sys.stderr)
        return 1

    (root / "scripts").mkdir(parents=True, exist_ok=True)
    research_dir = root / "references" / "research"
    research_dir.mkdir(parents=True, exist_ok=True)
    for sub in SOURCE_DIRS:
        (root / "references" / "sources" / sub).mkdir(parents=True, exist_ok=True)

    for fname, body in RESEARCH_STUBS:
        target = research_dir / fname
        if target.exists() and not force:
            continue
        target.write_text(body, encoding="utf-8")

    print(f"scaffolded: {root}")
    print(f"  research stubs: {len(RESEARCH_STUBS)} files in references/research/")
    print(f"  source dirs:    {', '.join(SOURCE_DIRS)}")
    print(f"next: run the 6 research agents, then Phase 2 distillation.")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("slug", help="figure slug, e.g. 'sun-tzu' or 'marcus-aurelius'")
    p.add_argument("--theme", action="store_true", help="create <slug>-framework/ instead of <slug>-echo/")
    p.add_argument("--force", action="store_true", help="overwrite existing stubs")
    args = p.parse_args()
    return scaffold(args.slug, args.theme, args.force)


if __name__ == "__main__":
    sys.exit(main())
