# utilities/

Scripts for installing distilled echoes and for the mechanical parts of the distillation workflow itself.

## Distillation-workflow helpers (Python, stdlib only)

These three scripts cover the mechanical bottlenecks inside the Echo workflow. They do not make judgment calls (model extraction, voice, era-anchoring stay with the orchestrator); they only handle deterministic work that was being done by hand.

| Script | Phase | What it does |
|---|---|---|
| `scaffold_echo.py <slug>` | 0.5 | Creates `.claude/skills/<slug>-echo/` with `scripts/`, `references/research/` (six numbered stubs), `references/sources/{primary,translations,scholarship}/`. Use `--theme` for `<slug>-framework/` instead. |
| `research_stats.py <slug>` | 1.5 | Walks `references/research/*.md` and prints per-file word count, source-tag count, and claim-label distribution (`[documented]`/`[attested]`/`[attributed]`/`[legendary]`/`[modern-scholarly-inference]`/`[absent]`). Flags thin files (<300 words) and reports the documented+attested ratio against the 50% pass bar. |
| `skill_lint.py <slug>` | 4 | Structural lint on a finished SKILL.md. Errors (fail the lint): missing required section, model count outside 3-7, heuristic count outside 5-10, any mental model missing era-assumption/evidence/failure-mode, any heuristic missing era-application/modern-analog, Honest Boundaries with <4 items. Warnings (review, don't fail): label ratio <50% documented+attested, CJK quote in SKILL.md not traceable to any research file (can be a hallucinated quote OR a research-file gap — eyeball it). |

All three pass `--theme` to target `<slug>-framework/` directories. Exit 0 = clean, 1 = errors, 2 = missing file.

```bash
python utilities/scaffold_echo.py marcus-aurelius
python utilities/research_stats.py marcus-aurelius
python utilities/skill_lint.py marcus-aurelius
```

## Install-echo helpers

## install-echo

Copies an echo from `examples/<name>-echo/` into either:
- `.claude/skills/<name>-echo/` (this project only) — default
- `~/.claude/skills/<name>-echo/` (every project on this machine)

### Bash (macOS / Linux / WSL / Git-Bash on Windows)

```bash
./utilities/install-echo.sh nietzsche-echo              # project scope (default)
./utilities/install-echo.sh socrates-echo --home        # user scope
```

### PowerShell (Windows)

```powershell
.\utilities\install-echo.ps1 nietzsche-echo             # project scope (default)
.\utilities\install-echo.ps1 socrates-echo -Scope Home  # user scope
```

## Why this exists

Claude Code auto-discovers skills only at `.claude/skills/<name>/SKILL.md` (project) or
`~/.claude/skills/<name>/SKILL.md` (user). The `examples/` directory is a browseable catalog;
copying is required to activate an echo.

The main Echo workflow skill lives at `.claude/skills/echo/` and is auto-activated
whenever you open Claude Code inside this repository.
