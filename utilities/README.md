# utilities/

Scripts that help install distilled echoes from `examples/` into a Claude Code skills directory.

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
