# Echo — Historical Figure Thinking Frameworks for Claude Code

Runnable cognitive operating systems distilled from the works, decisions, and documented
context of historical figures. Built as [Claude Code](https://claude.com/claude-code) skills.

An Echo is not a roleplay gimmick. It is a structured extraction of how someone thought —
their **mental models**, **decision heuristics**, **expression DNA**, **era assumptions**,
**anachronism boundaries**, and the **misappropriations** of their name — assembled into a
single `SKILL.md` file that Claude Code can auto-activate.

## What's in this repo

| Path | What it contains |
|------|------------------|
| `.claude/skills/echo/` | **The Echo workflow** — creates new distilled echoes. Auto-activates in Claude Code inside this repo. |
| `examples/` | Six distilled echoes ready to install: `albert-einstein-echo`, `emerson-echo`, `karl-marx-echo`, `napoleon-echo`, `nietzsche-echo`, `socrates-echo`. |
| `utilities/` | Install scripts (`install-echo.sh`, `install-echo.ps1`). |

## Quick start — use an existing echo

### Recommended: install via `npx skills add`

One command, no clone, cross-platform:

```bash
# Install everything — the Echo workflow + all 6 example echoes
npx skills add <owner>/Echo

# Install just the Echo workflow (so you can build your own echoes)
npx skills add <owner>/Echo/.claude/skills/echo

# Install a single example echo
npx skills add <owner>/Echo/examples/nietzsche-echo
npx skills add <owner>/Echo/examples/socrates-echo
```

`npx skills add` auto-discovers every `SKILL.md` in the path you give it and copies it into your Claude Code skills directory. No manifest or `package.json` is required on this end.

### Alternative: clone + install script

If you've already cloned the repo (e.g. as a contributor), the bundled scripts in `utilities/` give you `--project` vs `--home` scope control:

**Bash**
```bash
git clone https://github.com/<you>/Echo.git
cd Echo
./utilities/install-echo.sh nietzsche-echo          # install into this project's .claude/skills/
./utilities/install-echo.sh socrates-echo --home    # install into ~/.claude/skills/ (all projects)
```

**PowerShell**
```powershell
git clone https://github.com/<you>/Echo.git
cd Echo
.\utilities\install-echo.ps1 nietzsche-echo
.\utilities\install-echo.ps1 socrates-echo -Scope Home
```

### Activate after install

Open Claude Code and use any of an echo's trigger phrases:
- *"From Nietzsche's perspective, how should I think about ..."*
- *"What would Marx say about ..."*
- *"Socratic questioning of ..."*
- *"Einstein mode"* / *"Emerson voice"* / *"Napoleon-style analysis"*

Or force-invoke with a slash: `/<echo-name> <prompt>`.

## Quick start — create a new echo

Open Claude Code anywhere inside this repo. The Echo workflow auto-activates. Say:

> Distill [name] · or · What would [name] do? · or · Make an [name] perspective

## Why these echoes are different from "roleplay as X"

1. **Labeled quote provenance.** Every quoted passage is tagged `[documented]` / `[attested]` /
   `[attributed]` / `[legendary]` / `[modern-scholarly-inference]`. Fabricated or misattributed
   quotations are specifically called out in each echo's appendix.
2. **Era-anchoring.** Mental models carry their era-assumption and a failure mode for when
   that assumption no longer holds. No "timeless wisdom" flattening.
3. **Anachronism protocol.** Each echo explicitly refuses to fabricate post-death facts. It
   reasons about your century by disciplined analogy, and researches modern facts (via
   WebSearch) before applying its era-lens.
4. **Moral distance declaration.** Era-specific views that modern readers find difficult
   are preserved without sanitizing or amplifying, with clear rules for how the figure
   engages modern extensions of those views.
5. **Explicit disowning of misappropriations.** Nazi Nietzsche, Stalinist Marx, Einstein-as-theist,
   Napoleon-as-proto-Hitler, Socrates-as-law-school-questioning, Emerson-as-self-help —
   each echo names and rejects the specific distortions of its name.
6. **Two- or three-register expression DNA.** Public voice (what they wrote for readers) and
   private voice (how they spoke in letters and to friends) are both modeled. No echo is
   thunder start-to-finish.

## Installed echoes at a glance

| Echo | Era | Core lenses |
|------|-----|-------------|
| `albert-einstein-echo` | 1879–1955 | Principle-theory vs. constructive-theory, thought experiment, realist epistemology |
| `emerson-echo` | 1803–1882 | Over-Soul, Self-Reliance, Compensation, Circles, Fate-and-Power, Correspondence |
| `karl-marx-echo` | 1818–1883 | Critique of political economy, commodity fetishism, labour theory of value, class analysis, dialectical method |
| `napoleon-echo` | 1769–1821 | Operational concentration, institutional codification, symbolic register, *coup d'œil* |
| `nietzsche-echo` | 1844–1889 | Genealogy, eternal recurrence test, perspectivism with rank, will-to-power diagnostic, philosophy-as-memoir, ressentiment |
| `socrates-echo` | c. 470–399 BCE | Elenchus, craft-analogy, definitional questioning, care of soul |

## Using an echo without Claude Code

The `SKILL.md` inside each echo is a complete, self-contained prompt. To use with another
LLM or API:

1. Load the echo's `SKILL.md` as system prompt.
2. (Optional) Add the research files as retrieval context.
3. Send your question. The echo will follow the role-playing rules, anachronism protocol,
   and moral distance declaration inside the SKILL.md.

## License

MIT — see [LICENSE](LICENSE).
