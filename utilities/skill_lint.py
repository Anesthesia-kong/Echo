#!/usr/bin/env python3
"""Structural lint for a finished SKILL.md against Echo workflow requirements.

Catches mechanical errors before Phase 4 QA: missing sections, wrong model/heuristic
counts, mental models missing the era-assumption/evidence/failure-mode scaffolding,
and (most importantly) CJK passages quoted in SKILL.md that do not appear in any
research file — a common hallucination failure mode.

Usage:
    python utilities/skill_lint.py sun-tzu
    python utilities/skill_lint.py sun-tzu --theme   # theme echo

Exit code 0 = clean, 1 = lint errors, 2 = file missing.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parent.parent

REQUIRED_SECTIONS = [
    "## Role-Playing Rules",
    "## Response Workflow",
    "## Anachronism Protocol",
    "## Moral Distance Declaration",
    "## Identity Card",
    "## Era Card",
    "## Core Mental Models",
    "## Decision Heuristics",
    "## Expression DNA",
    "## Values",
    "## Intellectual Genealogy",
    "## Honest Boundaries",
    "## Appendix",
]

MENTAL_MODEL_HEADING_RE = re.compile(r"^###\s+Model\s+\d+[: ]", re.MULTILINE)
HEURISTIC_ITEM_RE = re.compile(r"^\d+\.\s+\*\*", re.MULTILINE)
CJK_BLOCK_RE = re.compile(r"[一-鿿㐀-䶿][一-鿿㐀-䶿，。；：！？、]{4,}")
LABEL_RE = re.compile(r"\[(documented|attested|attributed|legendary|modern-scholarly-inference)\]")


def find_echo_root(slug: str, is_theme: bool) -> Path:
    suffix = "-framework" if is_theme else "-echo"
    return REPO_ROOT / ".claude" / "skills" / f"{slug}{suffix}"


def check_sections(text: str) -> list[str]:
    errors = []
    for section in REQUIRED_SECTIONS:
        if section not in text:
            errors.append(f"missing required section: {section}")
    return errors


def check_model_count(text: str) -> tuple[int, list[str]]:
    errors = []
    models = MENTAL_MODEL_HEADING_RE.findall(text)
    n = len(models)
    if n < 3:
        errors.append(f"too few mental models: {n} (need 3-7)")
    elif n > 7:
        errors.append(f"too many mental models: {n} (max 7)")
    return n, errors


def check_model_scaffolding(text: str) -> list[str]:
    """Each ### Model N: block must contain era-assumption, evidence, and a failure-mode marker."""
    errors = []
    model_blocks = re.split(r"^###\s+Model\s+\d+", text, flags=re.MULTILINE)[1:]
    for i, block in enumerate(model_blocks, 1):
        # cut the block at the next ## or ### heading
        end = re.search(r"^#{2,3}\s", block, flags=re.MULTILINE)
        if end:
            block = block[: end.start()]
        block_lower = block.lower()
        if "era-assumption" not in block_lower:
            errors.append(f"Model {i}: missing 'Era-assumption'")
        if "evidence" not in block_lower:
            errors.append(f"Model {i}: missing 'Evidence'")
        if "failure mode" not in block_lower and "failure-mode" not in block_lower:
            errors.append(f"Model {i}: missing 'failure mode'")
    return errors


def check_heuristic_count(text: str) -> tuple[int, list[str]]:
    errors = []
    heur_section = re.search(r"## Decision Heuristics\b(.*?)(?=\n##\s)", text, flags=re.DOTALL)
    if not heur_section:
        return 0, ["Decision Heuristics section not found"]
    items = HEURISTIC_ITEM_RE.findall(heur_section.group(1))
    n = len(items)
    if n < 5:
        errors.append(f"too few heuristics: {n} (need 5-10)")
    elif n > 10:
        errors.append(f"too many heuristics: {n} (max 10)")
    return n, errors


def check_heuristic_scaffolding(text: str) -> list[str]:
    """Each heuristic must have 'Era application' and 'Modern analog' subfields."""
    errors = []
    heur_section = re.search(r"## Decision Heuristics\b(.*?)(?=\n##\s)", text, flags=re.DOTALL)
    if not heur_section:
        return []
    body = heur_section.group(1)
    era_count = len(re.findall(r"[Ee]ra application", body))
    modern_count = len(re.findall(r"[Mm]odern analog", body))
    items = len(HEURISTIC_ITEM_RE.findall(body))
    if items and era_count < items:
        errors.append(f"{items - era_count} heuristic(s) missing 'Era application'")
    if items and modern_count < items:
        errors.append(f"{items - modern_count} heuristic(s) missing 'Modern analog'")
    return errors


def check_honest_boundaries(text: str) -> list[str]:
    errors = []
    section = re.search(r"## Honest Boundaries\b(.*?)(?=\n##\s)", text, flags=re.DOTALL)
    if not section:
        return ["Honest Boundaries section not found"]
    bullets = re.findall(r"^\s*-\s+", section.group(1), flags=re.MULTILINE)
    if len(bullets) < 4:
        errors.append(f"Honest Boundaries has {len(bullets)} items (need >=4)")
    return errors


def check_label_ratio(text: str) -> list[str]:
    """Non-fatal: warn if documented+attested ratio < 50% of labels in SKILL.md."""
    errors = []
    labels = LABEL_RE.findall(text)
    if not labels:
        return []
    doc_att = sum(1 for label in labels if label in ("documented", "attested"))
    ratio = doc_att / len(labels)
    if ratio < 0.50:
        errors.append(f"label ratio in SKILL.md: {doc_att}/{len(labels)} = {ratio:.0%} documented+attested (want >=50%)")
    return errors


def check_quote_traceability(skill_text: str, research_dir: Path) -> list[str]:
    """Every multi-char CJK passage quoted in SKILL.md should appear in at least one research file.

    Catches hallucinated Chinese quotes that don't trace to source material.
    """
    errors = []
    if not research_dir.is_dir():
        return []
    research_texts = []
    for f in research_dir.glob("*.md"):
        research_texts.append(f.read_text(encoding="utf-8"))
    research_corpus = "\n".join(research_texts)

    # Extract distinct CJK runs from the SKILL.md and check each appears in corpus.
    quotes = CJK_BLOCK_RE.findall(skill_text)
    seen = set()
    for q in quotes:
        # normalize by collapsing punctuation variants; require ≥6 CJK chars for a meaningful check
        core = re.sub(r"[^一-鿿]", "", q)
        if len(core) < 6 or core in seen:
            continue
        seen.add(core)
        # match by a stable 6-char window from the quote (tolerates minor punctuation drift)
        probe = core[:8] if len(core) >= 8 else core
        research_core = re.sub(r"[^一-鿿]", "", research_corpus)
        if probe not in research_core:
            errors.append(f"quote not traceable to research files: {q[:40]}...")
    return errors


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("slug")
    p.add_argument("--theme", action="store_true")
    args = p.parse_args()

    root = find_echo_root(args.slug, args.theme)
    skill_path = root / "SKILL.md"
    research_dir = root / "references" / "research"

    if not skill_path.is_file():
        print(f"error: {skill_path} not found", file=sys.stderr)
        return 2

    text = skill_path.read_text(encoding="utf-8")

    # Structural errors fail the lint.
    errors: list[str] = []
    errors += check_sections(text)
    n_models, errs = check_model_count(text)
    errors += errs
    errors += check_model_scaffolding(text)
    n_heur, errs = check_heuristic_count(text)
    errors += errs
    errors += check_heuristic_scaffolding(text)
    errors += check_honest_boundaries(text)

    # Quote traceability and label ratio are warnings: they flag review-worthy
    # items but may be research-file gaps rather than SKILL.md defects.
    warnings: list[str] = []
    warnings += check_label_ratio(text)
    warnings += check_quote_traceability(text, research_dir)

    print(f"skill_lint: {skill_path}")
    print(f"  mental models: {n_models} (3-7)")
    print(f"  heuristics:    {n_heur} (5-10)")

    if errors:
        print(f"  errors: {len(errors)}")
        for e in errors:
            print(f"    - {e}")
    if warnings:
        print(f"  warnings: {len(warnings)} (review — may be research-file gaps, not defects)")
        for w in warnings:
            print(f"    ~ {w}")
    if not errors and not warnings:
        print("  status: CLEAN")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
