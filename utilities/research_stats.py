#!/usr/bin/env python3
"""Produce the Phase 1.5 research quality table automatically.

Walks an echo's references/research/*.md files and reports source counts,
claim-label distribution, and documented/attested ratio so the orchestrator
can flag thin dimensions without eyeballing six files.

Usage:
    python utilities/research_stats.py sun-tzu
    python utilities/research_stats.py sun-tzu --theme   # theme echo
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parent.parent

LABELS = ["documented", "attested", "attributed", "legendary", "modern-scholarly-inference", "absent"]
LABEL_RE = re.compile(r"\[(" + "|".join(LABELS) + r")\]")
WEB_SOURCE_RE = re.compile(r"\[web:\s*[^\]]+\]")
LOCAL_SOURCE_RE = re.compile(r"\[local:\s*[^\]]+\]")

THIN_WORD_THRESHOLD = 300
RATIO_PASS_THRESHOLD = 0.50


def analyze_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    words = len(text.split())
    labels = Counter(LABEL_RE.findall(text))
    web_sources = len(WEB_SOURCE_RE.findall(text))
    local_sources = len(LOCAL_SOURCE_RE.findall(text))
    return {
        "name": path.name,
        "words": words,
        "labels": labels,
        "web_sources": web_sources,
        "local_sources": local_sources,
        "total_sources": web_sources + local_sources,
    }


def format_report(stats: list[dict]) -> str:
    lines = []
    header = f"{'file':<34} {'words':>6} {'srcs':>5} {'doc':>4} {'att':>4} {'atr':>4} {'leg':>4} {'msi':>4}"
    lines.append(header)
    lines.append("-" * len(header))
    total = Counter()
    for s in stats:
        lines.append(
            f"{s['name']:<34} {s['words']:>6} {s['total_sources']:>5} "
            f"{s['labels'].get('documented', 0):>4} "
            f"{s['labels'].get('attested', 0):>4} "
            f"{s['labels'].get('attributed', 0):>4} "
            f"{s['labels'].get('legendary', 0):>4} "
            f"{s['labels'].get('modern-scholarly-inference', 0):>4}"
        )
        total.update(s["labels"])
    lines.append("-" * len(header))

    doc_att = total["documented"] + total["attested"]
    atr_leg = total["attributed"] + total["legendary"]
    grand = sum(total.values()) or 1
    ratio = doc_att / grand
    ratio_mark = "PASS" if ratio >= RATIO_PASS_THRESHOLD else "FAIL"

    lines.append(f"total labels: documented={total['documented']} attested={total['attested']} "
                 f"attributed={total['attributed']} legendary={total['legendary']} "
                 f"MSI={total['modern-scholarly-inference']} absent={total['absent']}")
    lines.append(f"documented+attested ratio: {doc_att}/{grand} = {ratio:.0%}  [{ratio_mark} >=50%]")

    thin = [s["name"] for s in stats if s["words"] < THIN_WORD_THRESHOLD]
    if thin:
        lines.append(f"WARN: thin files (<{THIN_WORD_THRESHOLD} words): {', '.join(thin)}")

    missing_sources = [s["name"] for s in stats if s["total_sources"] == 0]
    if missing_sources:
        lines.append(f"WARN: files with zero source tags: {', '.join(missing_sources)}")

    return "\n".join(lines)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("slug")
    p.add_argument("--theme", action="store_true")
    args = p.parse_args()

    suffix = "-framework" if args.theme else "-echo"
    research_dir = REPO_ROOT / ".claude" / "skills" / f"{args.slug}{suffix}" / "references" / "research"
    if not research_dir.is_dir():
        print(f"error: {research_dir} not found", file=sys.stderr)
        return 1

    files = sorted(research_dir.glob("*.md"))
    if not files:
        print(f"error: no .md files in {research_dir}", file=sys.stderr)
        return 1

    stats = [analyze_file(f) for f in files]
    print(format_report(stats))
    return 0


if __name__ == "__main__":
    sys.exit(main())
