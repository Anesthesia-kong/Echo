---
name: echo
description: |
  Echo: creates "echoes" of historical figures — runnable cognitive systems distilled from their surviving works, documented decisions, and the era that shaped them.
  Two entry points: (1) Specific historical figure → direct distillation (2) Vague situation/need → diagnosis → recommendation → distillation.
  Direct triggers: "Distill XX" "What would XX do?" "XX's way of thinking" "Make an XX perspective" "Update XX's echo" "Echo of XX".
  Vague triggers: "What would a medieval military strategist do?" "Are there any historical figures in a similar situation to me?" "I need to learn from history" "Which ancient thinker faced this?"
---

# Echo · Historical Figure Distillation Workflow

## Core Concept

This workflow does not resurrect the dead. It **distills thinking frameworks from what remains** — surviving works, preserved decisions, documented context, witness accounts.

A good historical Echo is a runnable cognitive operating system anchored in a specific century:

- What **mental models** shaped their worldview? (Lenses forged by their era's constraints)
- What **decision heuristics** did they rely on under their conditions? (Rules tested by their problems)
- How did they **express** themselves? (Voice preserved in ink, inscription, or faithful reporter)
- What will they **absolutely not** do? (Ethical anchors bound to their cosmology)
- What can this Echo **not know**? (Anachronism boundaries — anything past their lifespan)
- What of them is **history** vs **myth**? (Documented, attested, attributed, legendary)

**Key distinctions from distilling a living person**:

| Dimension | Living Person | Historical Figure |
|-----------|---------------|-------------------|
| Source medium | Video, podcast, tweets, live interviews | Written records, inscriptions, mediated testimony |
| Voice access | Direct (audio-visual) | Filtered through scribes, translators, centuries |
| Language | Usually the user's language | Often requires translation chain |
| Context | Shared modernity | Radically different era — different cosmology, economy, morality |
| Updates | Figure is still active | Corpus is closed; only scholarship on them grows |
| Quotes | Usually verifiable | "Documented" vs "attributed" vs "legendary" |
| Modern concepts | They can comment | Anachronism barrier — many concepts did not exist |
| Moral alignment | Navigates modern norms | May hold views modern readers find troubling |
| Myth pressure | Limited | Heavy — many figures are part-legend |

**Key distillation principle**: Capture HOW they thought inside their era, not the **modern projection** later ages built on top of them.

---

## Execution Flow

### Phase 0: Entry Routing

On receiving user input, first decide which path:

| User Input | Path | Example |
|-----------|------|---------|
| Specific historical figure | **Direct Path** → Phase 0A | "Distill Marcus Aurelius" "Make a Sun Tzu echo" |
| Vague situation/need | **Diagnosis Path** → Phase 0B | "I'm stuck in a long siege with no allies" "Which historical thinker faced mass uncertainty?" |

---

### Phase 0A: Demand Clarification (Direct Path)

When a specific figure is named, confirm before spending research budget:

1. **Which person precisely** — Disambiguate: "Cato" (the Elder or the Younger?), "Pliny" (Elder or Younger?), "Frederick" (Barbarossa or the Great?). Also confirm culture/tradition — "Lao Zi" in Daoist canon vs. popular-culture Lao Zi differ greatly.
2. **Which phase of life** (optional) — "Young Napoleon of Italian campaign" thinks differently from "Emperor Napoleon of 1812." Let the user pick a phase or default to "mature synthesis across life."
3. **Purpose** — Thinking advisor? Decision mirror? Role-play for study? Writing companion?
4. **New or Update** — Check `.claude/skills/` for existing echo. If exists, switch to Update Mode.
5. **Local materials** — "Do you have first-hand materials? A translated edition of their works, a critical biography, a letters collection, scanned manuscripts? User-provided materials almost always exceed what web search can surface."
6. **Language preferences** — Which language should the Echo converse in? If not the original, flag the translation layer explicitly in honest boundaries.
7. **Scope of views** — If the figure held views the user finds ethically difficult (slaveholders, inquisitors, conquerors), confirm: "Do you want me to preserve their documented views including the troubling ones, or confine the echo to a defined subset of their thought?"

User says "just do it" → Default to: mature-phase composite, thinking advisor, web search only, preserve documented views with contextual framing.

User provides local materials → Mark **local materials mode**. Phase 1 collection strategy adjusts accordingly.

After confirmation → Jump to Phase 0.5.

---

### Phase 0B: Demand Diagnosis (Vague Path)

The user does not know whom to echo; they have a situation or a need. The workflow's job is to **reverse-engineer the most illuminating historical figure from the demand**.

#### Step 1: Situation Positioning

Through at most 1–2 follow-ups, place the user's demand into a historical-learning dimension:

| Demand Dimension | Typical Expression | Historical Domains |
|------------------|-------------------|--------------------|
| Military / asymmetric conflict | "Surrounded by larger competitors" "Fighting with less" | Sun Tzu, Hannibal, Scipio, Belisarius, Liddell Hart, Võ Nguyên Giáp |
| Statecraft / leadership at scale | "Running a kingdom-scale org" "Holding a coalition together" | Augustus, Zhuge Liang, Elizabeth I, Bismarck, Lincoln |
| Philosophy / how to live | "Meaning in suffering" "How to keep composure" | Marcus Aurelius, Epictetus, Zhuangzi, Seneca, Boethius |
| Scientific discovery / seeing anew | "How to notice what others miss" | Newton, Darwin, Curie, Gauss, Ibn al-Haytham |
| Artistic breakthrough | "Finding my own voice" "Breaking form" | Michelangelo, Du Fu, Rembrandt, Bach, Hokusai |
| Revolutionary change | "Toppling entrenched systems" | Luther, Lenin, Gandhi, Thomas Paine |
| Political navigation | "Coalition-building under fragmentation" | Talleyrand, Metternich, Lincoln, Deng Xiaoping |
| Endurance through failure | "Years of losses before any win" | Tokugawa Ieyasu, Mandela, Shackleton, Liu Bei |
| Moral courage alone | "Standing against the crowd" | Socrates, Thomas More, Bonhoeffer, Sophie Scholl |
| Building from nothing | "Zero resources, no legitimacy" | Liu Bang, Genghis Khan, Andrew Carnegie (young) |
| Navigating decline | "When my era is ending" | Late Roman senators, late Ming reformers, late-Qing Li Hongzhang |
| Intellectual synthesis | "Combining incompatible schools" | Aquinas, Zhu Xi, Al-Kindi, Maimonides |
| Succession / long-term stewardship | "Outliving myself in what I build" | Augustus, Zhu Yuanzhang, Ataturk |
| Diplomacy in strangers' lands | "Negotiating across cultures" | Zheng He, Ibn Battuta, Matteo Ricci |

Follow-up principles:
- **Max 2 rounds.** Don't turn diagnosis into an intake form.
- If the user has already been specific enough, skip directly to recommendations.
- Follow-up purpose: distinguish similar-looking dimensions (e.g., "leadership" = statecraft or small-team command? Very different figures.)

**Example diagnosis rhythm**:

```
User: I keep losing wars of attrition. I'm not losing any one battle, but every month
      I'm a bit weaker than before.

Echo:  Is the weakening about resources/money, about morale, or about legitimacy
       (i.e., people no longer believing you will win)?

User:  Mostly legitimacy. My allies are quietly hedging.

Echo:  Understood — the demand is "how to reverse a slow loss of momentum
       when you're still technically winning battles." Three candidates:
       [recommendations follow]
```

#### Step 2: Candidate Recommendations

Based on the dimension, recommend 2–3 figures. Candidates can be people **or** themes (e.g., "Stoic crisis response" as a theme if no single person cleanly fits).

**First judgment: Person Echo or Theme Echo?**
- The demand points to a specific voice and tradition → Person Echo
- The demand points to a field with multiple schools → Theme Echo (see Special Scenarios)
- Uncertain → include both types in recommendations

**Source A: Existing local echoes.** Scan `.claude/skills/*-echo/` for description matches. Already-distilled figures are zero-cost to activate.

**Source B: New distillation candidates.** Map user's dimension to concrete historical domains in the table above. When proposing, explain **which specific mental model** this figure carries that matches the demand.

Candidate display format:

```
### Candidate 1: [Name] — (Existing Echo / Needs Distillation)

**Era & Role**: [When, where, what role — so user can instantly gauge relevance]
**Core Lens**: [Unique way of seeing problems, one sentence]
**Why suitable for you**: [Direct match to user's demand — which mental model solves which specific problem]
**Limitations & era distance**: [How far their context is from modern problems; what of their views modern readers may find hard]
```

Recommendation rules:
- Max 3 candidates — choice fatigue is worse than no choice.
- Prefer cross-cultural diversity (not 3 Romans, not 3 Chinese sages).
- Differentiate candidates along a real axis (e.g., "Sun Tzu = deception-first, Hannibal = lethal-initiative, Scipio = patient-assimilation").
- Always state limitations. A 2000-year-old thinker has genuine blind spots.
- Recommend concretely — "Marcus Aurelius's practice of **morning premeditation of adversity**" — not "he's great."

#### Step 3: User Selection

- Picks existing echo → activate, task complete.
- Picks new distillation candidate → Phase 0A confirm details → Phase 0.5 begin.
- None suitable → back to Step 1 with a refined question, or user proposes their own figure.

---

### Phase 0.5: Create Echo Directory

**Execute immediately after confirmation, before research begins.**

```
.claude/skills/[person-name]-echo/
├── SKILL.md                           # Final product
├── scripts/                           # Tool scripts (if any)
└── references/
    ├── research/                      # Each Agent's findings (mandatory save)
    │   ├── 01-primary-works.md        # Surviving writings, attested authorship
    │   ├── 02-contemporary-records.md # Chronicles & eyewitness accounts (same generation)
    │   ├── 03-letters-sayings.md      # Personal correspondence, documented speech, attested sayings
    │   ├── 04-scholarly-biographies.md# Modern critical scholarship
    │   ├── 05-era-context.md          # Historical/cultural/religious/economic context of their time
    │   └── 06-reception-history.md    # How they were interpreted across later eras
    └── sources/                       # First-hand materials
        ├── primary/                   # Original-language works if accessible
        ├── translations/              # Translated editions
        └── scholarship/               # Secondary analyses (critical biographies, monographs)
```

**Naming conventions** (apply everywhere):

| Item | Rule | Examples |
|------|------|----------|
| Skill directory (person) | `<figure-slug>-echo/` | `marcus-aurelius-echo`, `sun-tzu-echo`, `ibn-khaldun-echo` |
| Skill directory (theme) | `<topic-slug>-framework/` | `stoic-resilience-framework`, `medieval-just-war-framework` |
| `<figure-slug>` format | ASCII, lowercase, hyphen-separated; common modern English name; no titles, honorifics, or dynastic prefixes | `confucius` not `master-kong`; `napoleon` not `emperor-napoleon-i`; `ieyasu` not `tokugawa-ieyasu-shogun` |
| Main skill file | `SKILL.md` (all caps — Claude Code convention) | |
| Research files | `NN-topic-kebab.md`, numbered 01–06 in the order defined above | `01-primary-works.md` |
| Claim labels (in research) | `[documented]` / `[attested]` / `[attributed]` / `[legendary]` / `[modern-scholarly-inference]` | |
| Source-origin tags (in research) | `[local: <filename>]` or `[web: <url>]` | |
| `sources/` subdirectories | lowercase single word | `primary/`, `translations/`, `scholarship/` |

**Completion checks** (auto-execute):
- [ ] Directory created
- [ ] If figure outside the user's cultural tradition → source strategy prioritizes scholarship **inside** that tradition, not imported Western/Eastern projections
- [ ] If Chinese/East Asian figure: use CNKI academic sources, authoritative Chinese historical journals, Bilibili academic lectures (not popular retellings); exclude Zhihu, WeChat public accounts, and Baidu Baike
- [ ] If figure is in a living religious tradition (founder-type): separate historical-critical sources from devotional sources; keep both but label
- [ ] If update mode: existing SKILL.md read; mark what needs refresh (usually only recent scholarship)
- [ ] If user provided local materials: copy/move into `sources/` with clear subdirectory; mark **local materials mode**

**Critical rules**:
- Every subagent must write findings into its corresponding md file. Research with no file artifact = research that did not happen.
- **All research files live inside the echo directory** (`references/research/`). Never save to sibling project folders. The echo must be self-contained — copying the directory elsewhere should yield a working echo with no external dependency.
- **Classify every claim** at write time: `[documented]` (appears in primary source), `[attested]` (multiple independent contemporary sources), `[attributed]` (later sources only), `[legendary]` (first appears in non-contemporary legend). This label persists into the final SKILL.md.
- **Where to write the completed echo**: by default, write to `.claude/skills/[person-name]-echo/` (the Claude Code auto-discovery path). If this repo is configured as an open-source distribution with an `examples/` directory, move the completed, Phase-4-passed echo from `.claude/skills/[person-name]-echo/` to `examples/[person-name]-echo/` for publication; the auto-discovery path is the dev location, `examples/` is the published catalog.

---

### Phase 1: Multi-Source Information Collection (Parallel Agent Swarm)

#### Mode Judgment: Local Materials vs. Web Search

| Mode | Trigger | Strategy |
|------|---------|----------|
| **Pure web search** (default) | User provided nothing | All 6 Agents do full-dimension search |
| **Local materials primary** | User provided books/translations/scholarship | First analyze locals; web search fills gaps |
| **Pure local materials** | User said "only what I give you" or figure so obscure web yields nothing | Only analyze locals; no web search |

**Local materials priority logic**:
1. Classify user-provided files into the 6 dimensions (a biography covers 02 + 03 + 04; a collected-letters volume = 03; a critical translation = 01)
2. Identify coverage gaps
3. Launch web search Agents only for under-covered dimensions
4. In research files, clearly mark source: `[local: <filename>]` vs `[web: <url>]`

**Material types and their dimension coverage**:

| Material | Processing | Dimensions |
|----------|-----------|------------|
| Critical translation of their works | Read, extract core arguments, track translator's notes | 01 (Primary), 03 (voice) |
| Collected letters edition | Analyze personal voice and decision reasoning | 03 (Letters), 05 (Decisions) |
| Scholarly biography PDF | Cross-reference modern analytic synthesis | 04 (Scholarly), 05 (Era) |
| Primary-language fragments | If accessible, mark untranslated nuance | 01 (Primary) |
| Contemporary chronicle (e.g., Plutarch, Sima Qian) | Extract eyewitness-adjacent observations; flag bias | 02 (Contemporary), 06 (Reception, since these shaped later view) |

Rank user-provided critical editions (e.g., Hays's *Meditations*, Lau's *Analects*) at the top of the source hierarchy — above any web search result.

---

#### The 6 Research Agents (Standard Task Assignments)

Launch 6 parallel subagents, each responsible for one dimension of the historical figure.

| Agent | Search Target | Extraction Focus | Output File |
|-------|---------------|------------------|-------------|
| 1 Primary Works | Surviving writings, inscriptions, attested attributed works | Core arguments appearing ≥3 times; self-coined concepts; their own vocabulary; their intellectual antecedents as they cite them | `01-primary-works.md` |
| 2 Contemporary Records | Same-generation chronicles, eyewitness accounts, court records | How they appeared to contemporaries; specific episodes with witness corroboration; official acts and public reputation | `02-contemporary-records.md` |
| 3 Letters & Sayings | Personal correspondence, documented speeches, attested sayings, dialogue transcripts | Personal voice vs. public voice; impromptu reasoning; moments of doubt or change; apologies, private confidences | `03-letters-sayings.md` |
| 4 Scholarly Biographies | Modern critical biographies, academic monographs, peer-reviewed articles | Synthesis, myth-debunking, controversies in scholarship, revisionist readings | `04-scholarly-biographies.md` |
| 5 Era Context | Historical/cultural/religious/economic/political environment | What they took for granted; ideas available in their era; what words meant then; material conditions | `05-era-context.md` |
| 6 Reception History | Interpretation across centuries; how different eras read them | Reveals which "traits" are documented vs. which are later projection (critical for honesty) | `06-reception-history.md` |

#### Hard Requirements for Every Agent

- Write findings to `references/research/0X-*.md`.
- Label every claim with one of: `[documented]` / `[attested]` / `[attributed]` / `[legendary]` / `[modern-scholarly-inference]`.
- Track translation chain for any quoted passage (original language → known translator → your citation).
- Note earliest surviving source for any saying attributed to the figure. If the earliest source is 500 years after their death, the saying is `[attributed]` at best.
- When sources disagree, **keep the disagreement**. Contradictions are signal, not noise.
- When modern scholarship debunks a traditional story, note both traditional and revisionist view.

#### Agent Prompt Template

When spawning Agent 1 (Primary Works), use this structure:

```
Task: Research [Person]'s surviving works and attested authorship.

Search directions:
- What works have survived under this person's name?
- Among those, which are accepted as authentic by modern scholarship? Which are disputed? Which are now rejected?
- What language were they originally written in? What are the standard critical editions / translations?
- Core arguments that recur ≥3 times across their corpus (these are true beliefs, not rhetorical flourish)
- Self-coined concepts and vocabulary
- Who do they cite as their own teachers / influences?

Output requirements:
- Write to [echo directory]/references/research/01-primary-works.md
- Label every claim [documented] / [attested] / [attributed] / [legendary] / [modern-scholarly-inference]
- For every quoted passage, note: original language + translator + edition
- Preserve contradictions; do not harmonize them

Source hierarchy:
- Standard critical editions > scholarly translations > popular translations > quote aggregators
- Use peer-reviewed academic sources for authorship disputes (Oxford Classical Dictionary, CHC, CHEP, JSTOR articles)
- Blacklist: quote-aggregator sites (brainyquote, goodreads), Wikipedia as terminal citation, historical fiction, devotional uncritical literature
```

The other 5 Agents adjust search direction and output file analogously (use the table above).

#### Tool Assistance

If the following skills are installed, use them — they are more reliable than raw web search:

| Installed Skill | Use When |
|-----------------|----------|
| `pdf` | User provided PDFs of critical editions, biographies, monographs |
| `web-article-reader` | Found a specific scholarly article URL and need full text, not a search snippet |
| `huashu-research` | Need structured deep research into one dimension (e.g., extremely thorough "authorship disputes of the Analects") |
| `gemini-video` | User provided recorded academic lectures on the figure |

Announce available skills to each spawned Agent so it can use them on demand.

#### Information Source Priorities (Historical-Adapted)

| Source Type | Reveals | Weight |
|-------------|---------|--------|
| **User-provided primary works** (critical editions, verified letters) | Authentic voice, complete context | **Highest +** |
| Surviving works in original language | Direct, un-mediated thought | Highest |
| Scholarly critical editions & translations | Authentic voice through known translator | Highest |
| Contemporary chronicles (same generation, independent) | Near-eyewitness observation | Highest |
| Documented letters / verified speeches | Personal voice, impromptu reasoning | Highest |
| Post-1950 peer-reviewed scholarly biographies | Analytic synthesis, myth-debunking | High |
| Near-contemporary biographies (Plutarch, Sima Qian, etc.) | Close but biased; treat as primary-for-their-era source + reception-history | Medium-High (with bias flag) |
| Popular modern biographies | Readable, often simplified | Medium-Low |
| Devotional / hagiographic literature | Reception, not history (unless explicitly studying cult) | Low |
| Wikipedia | Entry point only; trace to underlying citation | Reference only, never terminal |
| Quote-aggregator sites | Massively misattributed | Avoid |
| Historical fiction, films, novels | Dramatization | Avoid as source |

#### Information Source Blacklist (always exclude)

- **brainyquote / goodreads quotes / azquotes** — misattribution rate exceeds 50% for many figures
- **Wikipedia as terminal citation** — use as index, always follow to underlying reference
- **Historical fiction / film adaptations** — dramatization
- **Hagiographic devotional literature** treated as historical (OK as reception-history source, never as history)
- **Pop-history podcasts** as primary source (entertainment, not scholarship)
- **Zhihu / WeChat public accounts / Baidu Baike** (for East Asian figures) — high distortion, unverifiable
- **AI-generated summary sites** — compounding hallucination

For Chinese figures, accept: CNKI-indexed journals, Zhonghua Shuju critical editions, authoritative academic publishers (Peking University Press, Commercial Press), Palace Museum publications, major state historical institutes' work. For interviews/lectures about the figure, prefer university lecture recordings on Bilibili (not popular UP-master reinterpretations).

#### Agent Timeout & Failure Handling

- **Single Agent timeout** (5 min, no valuable results): do not wait. In Phase 2, mark that dimension "insufficient." Reflect in honest boundaries.
- **Source scarcity** (fewer than ~10 usable sources): warn the user in Phase 0.5 — reduce expected mental models to 2–3, enlarge honest boundaries.
- **Contradictory Agent results**: **keep the contradiction**. Do not harmonize.

---

### Phase 1.5: Research Review Checkpoint

After all Agents finish, pause and present a quality summary:

```
┌───────────────────────┬──────────┬───────────────────────────────────┐
│ Agent                 │ Sources  │ Key findings                      │
├───────────────────────┼──────────┼───────────────────────────────────┤
│ 1 Primary Works       │ 8        │ Core arguments: ...               │
│ 2 Contemporary Records│ 5        │ Eyewitness claims: ...            │
│ 3 Letters & Sayings   │ 12       │ Personal voice features: ...      │
│ 4 Scholarly Bio.      │ 6        │ Main scholarly disputes: ...      │
│ 5 Era Context         │ 4        │ Key era constraints: ...          │
│ 6 Reception History   │ 5 eras   │ Myth vs history: ...              │
├───────────────────────┼──────────┼───────────────────────────────────┤
│ Documented : Attributed │ 14 : 9 │                                   │
│ Myth-debunking flags  │ 3        │ E.g., "xxx saying first appears Y │
│                       │          │ centuries after death"            │
│ Translation layers    │ Greek →  │                                   │
│                       │ Latin →  │                                   │
│                       │ English  │                                   │
│ Contradictions        │ 2 places │ Agent1 vs Agent4 on...            │
│ Insufficient dimensions│ None    │                                   │
└───────────────────────┴──────────┴───────────────────────────────────┘
```

User confirms → Phase 2. User flags weak dimension → supplement research, then continue.

---

### Phase 2: Framework Distillation (Synthesis)

#### 2.1 Mental Model Extraction (3–7)

1. **Scan** `01-primary-works.md` through `05-era-context.md` for candidate arguments and recurring lenses. Target 15–30 raw candidates.
2. **Three-verification screening** on each:
   - **Cross-domain reproducibility**: appears in ≥2 distinct domains/topics?
   - **Generativity**: can we predict their stance on a problem they didn't directly address?
   - **Era-anchored exclusivity**: not merely "what any thoughtful person of that culture would think" — actually distinctive of this figure within their tradition?
   - 3 passes → mental model; 1–2 passes → decision heuristic; 0 passes → discard.
3. **Era-anchoring annotation**: each retained model carries an `[era-assumption]` note — what era-specific premise does it rest on? (E.g., Sun Tzu's "deception" assumes a culture where stratagem is honorable, not dishonorable.) This matters for Phase 3 when modern users apply the model.
4. **Sort and select top 3–7**. Prefer depth — 3 profound era-anchored models beat 10 surface principles.
5. **Record format** per model: name, one-sentence description, ≥2 evidence citations, application domain, era-assumption, failure modes (including era-transfer failure).

#### 2.2 Decision Heuristic Extraction (5–10)

Each heuristic = an "if X, then Y" quick rule this figure used. For historical figures, **attach a modern-analog example** to each heuristic so users can apply it:

```
Heuristic: "Know the ground before knowing the enemy."
  - Era application: Sun Tzu's insistence on terrain analysis before any engagement.
  - Documented example: [cite where this appears in The Art of War]
  - Modern analog: Before competing for a market, study the market's structural shape
    (regulation, distribution, pricing norms) before profiling rival companies.
```

#### 2.3 Expression DNA

| Dimension | Extraction |
|-----------|-----------|
| Sentence structure (in original language, if accessible) | Long/short, parallel constructions, question frequency |
| Vocabulary signature | Self-coined terms, favored concepts, conspicuous absences |
| Rhetorical devices of their era | Classical allusion, formulaic epithets, parables, aphorisms |
| Rhythm of reasoning | Conclusion-first or build-up-first, transition style |
| Humor / tone | Sardonic, earnest, austere, playful, none |
| Certainty signaling | "It is evident that..." type or "It seems to me..." type |
| Quotation habits | Who do they cite, and what kinds of texts |
| Voice-through-translation | What survives the translation layer, what is inevitably lost |
| Documented vs. attested voice distinction | Mark which style features come from uncontested works vs. disputed attributions |

**Translation advisory**: when the Echo will operate in a language other than the figure's original, explicitly decide which translation tradition's voice to emulate (e.g., for Marcus Aurelius in English: Hays's modern directness vs. Long's Victorian gravitas). The translation choice is a design choice — declare it.

#### 2.4 Values & Anti-Patterns

- **Values in priority order** — 3–5 core values as they held them, in their words/concepts, not modern rephrasing.
- **Anti-patterns** — behaviors they explicitly condemned.
- **Contradictions & tensions** — value conflicts inside the figure. Historical figures are especially contradictory because their corpus often spans decades and crises. Preserve these tensions — they are depth, not flaws.
- **Era-anchored values modern readers may find troubling** — list them honestly (e.g., Aristotle on slavery, Confucius on gender hierarchy, Columbus on conquest). Do not sanitize. Do not amplify. Phase 2.8 governs how the Echo handles these.

#### 2.5 Intellectual Genealogy

- **Upstream**: who/what shaped this figure (teachers, canonical texts, predecessor schools)
- **Lateral**: contemporaries in conversation or opposition
- **Downstream**: who they shaped, and which later movements claimed them
- **Misappropriation flags**: later movements that claimed them but distorted their thought (e.g., Nietzsche & Nazi misappropriation; Confucius & various political weaponizations)

#### 2.6 Honest Boundaries

Required historical-specific limitations:
- Corpus is closed — no new primary works will emerge (usually)
- Translation layer between reader and figure
- Portion of attributed works may not be authentic
- Documented views reflect their era, not modern moral consensus
- Anachronism: cannot speak to post-death events, technologies, or concepts
- Research cutoff date for secondary scholarship
- Reception-history layer: the "traditional image" often differs from the historical person

#### 2.7 Anachronism Protocol (historical-specific, required)

Define in advance how the Echo handles three classes of modern questions:

| Question Type | Echo Response |
|---------------|---------------|
| Modern technology (internet, AI, cars, guns past their lifespan) | "I did not live to see this. I can tell you how I would parse an analogous question in my era, but I cannot speak about the thing itself." |
| Modern ideology/movements (liberalism, communism, feminism, etc.) post-their-death | "The word is from a later age. Let me describe what of this, if anything, existed in my world, and how I parsed it." |
| Events after their death | Explicitly flag: "This happened after my life. I cannot know of it. I can, however, apply the models I used to reason about change." |
| Modern problem with ancient analog | Proceed by analogy; name the analog explicitly |
| Problem fully inside their era | Answer naturally |

Mandatory in Phase 3 output.

#### 2.8 Moral Distance Declaration

Rules for how the Echo handles views the figure held that modern readers find ethically difficult:

- **Preserve**: the Echo does not deny the figure held documented views.
- **Contextualize**: when relevant, the Echo names the era-assumption that generated the view.
- **Do not amplify**: the Echo will not extend era-views to modern applications the figure never addressed. (A Confucian echo will not opine on modern gender policy as though Confucius did; it will note the era view and decline the modern extension.)
- **Do not editorialize as the figure**: the Echo does not pretend the figure "would have disagreed" with their own documented view just to comfort the modern reader.
- **Framing disclaimer** (said once per activation): "My views reflect my era's assumptions. Some of them will not align with yours. I will speak honestly from within my world."

---

### Phase 2.5: Distillation Confirmation Checkpoint

After Phase 2, pause and display:

```
Distillation summary for [Person]:
- Mental models: N (list names + era-assumption)
- Decision heuristics: N (each with modern analog)
- Expression DNA: [3 signature features + translation-tradition choice]
- Core tensions: N pairs
- Era-anchored views requiring Moral Distance handling: N
- Honest boundaries: N
- Anachronism protocol: READY
```

User confirms → Phase 3. User flags a wrong or missing model → adjust, then proceed.

---

### Phase 3: Echo Construction

Assemble Phase 2 outputs into a runnable SKILL.md following `echo-template.md`.

#### Step 1: Read Template

Read `references/echo-template.md` — it defines the structure for a historical-figure Echo (frontmatter, role-playing rules, anachronism protocol, era card, mental models, expression DNA, timeline, moral-distance declaration, honest boundaries, sources, creator attribution).

#### Step 2: Fill the Template

| Template Section | Fill Source |
|------------------|-------------|
| frontmatter description | Source count + model count + trigger words |
| Role-playing rules | Template default |
| **Response Workflow (Agentic Protocol)** | **Auto-deduced from mental models — see guide below** |
| Era Card | From Agent 5 (Era Context) — when, where, political/religious/economic conditions |
| Identity card | From 01 + 06 — a 50-word first-person self-introduction in the figure's tone, within their era |
| Mental models | Phase 2.1 — each with era-assumption + modern failure modes |
| Decision heuristics | Phase 2.2 — each with era application + modern analog |
| Expression DNA | Phase 2.3 — including translation-tradition choice |
| Timeline | Agent 6 + Agent 2 — key nodes from birth to death |
| Values & anti-patterns | Phase 2.4 |
| Intellectual genealogy | Phase 2.5 — with misappropriation flags |
| **Anachronism Protocol** | Phase 2.7 — verbatim from the 4-row table |
| **Moral Distance Declaration** | Phase 2.8 |
| Honest boundaries | Phase 2.6 + research cutoff |
| Sources appendix | All 6 Agents' citations, separated into primary / contemporary / scholarly, with documented/attested/attributed labels preserved |
| Creator attribution | Fixed: `> This Echo generated by the Echo · Historical Figure Distillation Workflow` |

#### Response Workflow (Agentic Protocol) Generation Guide

**Position in output SKILL.md**: after "Role-playing rules," before "Example dialogues."

**Template** (fill Step 2 research dimensions from the figure's mental models):

```markdown
## Response Workflow (Agentic Protocol)

**Core Principle: I do not invent facts about worlds I did not live in. When asked about modern specifics, I do homework before I speak.**

### Step 1: Question Classification

Upon receiving a question, classify:

| Type | Characteristic | Action |
|------|---------------|--------|
| **Inside my era** | Events/figures/ideas from my lifetime or before | → Answer directly from my knowledge |
| **Modern facts needed** | Specific modern companies, people, technologies, events | → Research modern facts (Step 2), then analyze with my frameworks (Step 3) |
| **Modern concept, no era analog** | Concepts that did not exist in my world (e.g., quantum mechanics, internet) | → Invoke Anachronism Protocol |
| **Pure framework / timeless** | "How should I decide under uncertainty?" | → Answer from mental models directly (skip to Step 3) |
| **Mixed** | Modern situation asking for timeless principle | → Research modern facts + apply frameworks |

**Judgment rule**: if answer quality would degrade noticeably without current facts, research first. One extra search beats one fabrication.

### Step 2: [Figure]-style Research (for Modern Fact questions)

**Must use real tools (WebSearch, etc.) to gather modern facts. Do not fabricate.**

[Auto-deduce 3–5 research dimensions from this figure's mental models. Each dimension lists 3–5 concrete things to look for. See guidance below.]

#### Research Output Format
Organize findings internally as a fact brief (do not surface raw search results to the user). Then proceed to Step 3.
The user sees not a research report, but [Figure]'s judgment grounded in real modern facts.

### Step 3: [Figure]-style Response

Using Step 2 facts (if any), apply mental models and expression DNA. Respond as [Figure], within the Anachronism Protocol.
```

**Step 2 research-dimension deduction examples**:

| Figure | Core Mental Models | → Research Dimensions |
|--------|-------------------|----------------------|
| Sun Tzu | Know-self/know-enemy, deception, terrain-first, victory-before-battle | Map the "terrain" (market/regulatory/distribution shape); survey rival's visible moves and likely hidden ones; identify asymmetries of information; assess morale on both sides |
| Marcus Aurelius | Cosmic perspective, duty over outcome, view-from-above, memento mori | Surface the durable facts (time-horizon of the situation); name what is in user's control vs. not; test decision against "would this matter in a decade?"; check for impulse vs. deliberation |
| Machiavelli | Virtù vs. fortuna, founding vs. maintaining, appearances as politics, lesser-evil calculus | Identify the founder-vs-inheritor state of the situation; map power relations; ask what appearances are being maintained; surface the least-worst option set |
| Sun Yat-sen | Three Principles, revolutionary patience, coalitional gradualism | Test whether the "ground" is ready; map factional interests; identify the minimum viable alignment |
| Darwin | Variation, selection pressure, slow patient observation | Identify what varies; what pressures select; what time horizon is required to see effects; what data is being missed |
| Ibn Khaldun | Asabiyyah (group feeling), cyclical rise/decline of polities, sedentary-vs-nomadic dynamic | Assess cohesion of the user's group; identify phase of the cycle; check for signs of "sedentary" decay |

**Constraints**:
- Dimensions come **from** the figure's mental models, not from a generic "look things up" list.
- Each dimension gets concrete research guidance (what to search, what data to read), not abstract prose.
- Group by question type if the figure's framework naturally partitions (e.g., Sun Tzu: "when analyzing a rival" vs. "when analyzing the terrain" vs. "when analyzing my own forces").

#### Step 3: Quality Self-Check

Read the Quality Check List (below, Phase 4). Fix weak items before output.

#### Step 4: Output

Write finished SKILL.md to `.claude/skills/[person-name]-echo/SKILL.md`.

---

### Phase 4: Quality Validation

Use a subagent (not the main agent, to avoid self-evaluation bias) to run:

#### 4.1 Known Test (Documented-Stance Check)

Select 3 questions the figure publicly addressed. **Spawn subagent with new Echo, capture its answers, compare to documented stance.**
- Direction matches → models valid.
- Drifts → trace back and adjust model weights.

#### 4.2 Anachronism Test (new for historical)

Ask the Echo 3 things it could not possibly know: a post-death event, a post-death technology, a post-death ideology.
- Expected: Anachronism Protocol engages cleanly. Echo does not pretend to know; offers analogy if meaningful, refuses otherwise.
- Fails if: Echo answers as if it lived through the modern event.

#### 4.3 Analogical Transfer Test (new for historical)

Give the Echo a modern problem with a clear ancient analog (e.g., ask Sun Tzu about a modern market-entry with an incumbent — obvious analog to invading occupied territory).
- Expected: Echo research modern facts (Step 2), then applies mental models through analogy, naming the analog explicitly.
- Fails if: Echo pretends to know modern specifics without research, or refuses a tractable analogy.

#### 4.4 Edge Test (Uncharted Territory)

Select a question the figure never publicly addressed but is within their era's possible range. Use the Echo to reason.
- Expected: "From models X and Y I would reason..., but I am uncertain."
- Fails if: Echo speaks with unwarranted certainty.

#### 4.5 Style Test (Voice Check)

Have the Echo write a 150-word analysis of a modern problem.
- Recognizable as this figure's voice (within the chosen translation tradition)?
- Not generic AI prose?
- Not pastiche-quotation?

#### 4.6 Historical Accuracy Test (new for historical)

Ask the Echo to quote itself on 3 topics. Verify quotes against research files.
- Expected: quotes are documented or clearly framed as paraphrase.
- Fails if: Echo confabulates specific wording never attested to the figure.

#### 4.7 Moral Distance Test (new for historical)

Ask the Echo a question inside a domain where the figure held era-specific views modern readers find troubling.
- Expected: the Echo speaks the documented view in context, does not sanitize, does not amplify, does not claim the figure would reject their own view.
- Fails if: Echo rewrites history (in either direction).

#### Pass Standards

| Check | Pass | Fail Signals |
|-------|------|--------------|
| Mental models | 3–7, each with era-assumption, evidence, failure mode | <3, >10, no era-anchoring |
| Decision heuristics | 5–10, each with era example + modern analog | Heuristics without modern bridging |
| Expression DNA | Translation tradition declared, identifiable in 100 words | Reads like generic AI |
| Anachronism protocol | All 3 Anachronism Test items handled cleanly | Echo "knows" post-death facts |
| Analogical transfer | Modern problem analyzed through era lens | Echo fabricates modern knowledge |
| Historical accuracy | Claimed quotes verifiable | Confabulated wording |
| Honest boundaries | ≥4 specific items including translation + anachronism + era-views | Only "cannot replace the person" |
| Internal tensions | ≥2 real contradictions preserved | Harmonized legend |
| Primary-source proportion in research | >50% of claims from [documented]/[attested] sources | Mostly [attributed]/[legendary] |
| Moral Distance | Era-views preserved + framed + not amplified | Sanitized or amplified |

Pass → deliver. Fail → mark weak items, iterate Phase 2–4.
**Iteration cap**: Phase 2↔4 max 2 cycles. After 2 cycles, mark residual weak dimensions in honest boundaries and deliver the current best version. Infinite polishing is worse than honest limitation.

Display validation results for user confirmation before completion.

---

### Phase 5: Dual-Agent Refinement (Standard Post-Process)

After Phase 4 pass, launch two Agents in parallel:

**Agent A (echo-optimizer perspective)**:
- Evaluate structural clarity: does the workflow fire correctly on real user prompts?
- Dry-run 3 typical prompts: (a) a question inside their era, (b) a modern-facts question, (c) an anachronism question. Evaluate.
- Output: 2 specific improvements to weakest dimensions, with rewritten text.

**Agent B (historical-authenticity perspective)**:
- Review: do Mental Models preserve era-anchoring (not modernized)?
- Review: does Expression DNA match the declared translation tradition?
- Review: is Anachronism Protocol coverage complete for likely user prompts?
- Review: does Moral Distance Declaration match actual era-views in research?
- Output: 2–3 specific text changes with rewrites.

Main agent synthesizes, applies non-conflicting improvements, presents change summary for user confirmation.

---

## Updating Existing Echoes

When user says "update XX's echo" or "new scholarship on XX came out":

1. Read existing SKILL.md, find research cutoff date in Honest Boundaries.
2. Because corpus is closed, usually only Agent 4 (scholarly biographies) and Agent 6 (reception history) need refresh. Agents 1–3 almost never gain new material (unless a new manuscript was discovered).
3. Compare new scholarship with existing content:
   - Reinforces existing models → add examples.
   - Debunks myth in existing content → revise, mark change.
   - Contradicts a mental model → weigh evidence; if scholarship is robust, update.
   - New scholarly framing of the figure → consider adding/refining a model.
4. Update research cutoff date and "Latest Scholarship" subsection.
5. Incremental update only. Do not rewrite the whole Echo.

---

## Tie-Breakers (When Judgment Is Required)

| Rule | Implication |
|------|-------------|
| Primary > secondary > tertiary | A verified letter outweighs ten later biographies |
| Documented > attested > attributed > legendary | The label is not optional |
| Contemporary record > later chronicle | Even biased contemporary beats polished later reconstruction |
| Contradictions > harmonization | Preserve; do not smooth |
| Era-anchoring > modernization | Do not make the figure sound like a modern life coach |
| Tradition-internal scholarship > projection | Study non-Western figures through their own tradition's scholarship first |

---

## Special Scenarios

### Figures Who Left No Writings (Socrates, Jesus, Confucius, pre-literate kings)

The figure is accessed entirely through reporters (Plato, Xenophon, the Gospels, the Analects). Adjust:

1. Name the mediation explicitly. The Echo is of "Socrates as transmitted through Plato + Xenophon," not Socrates himself.
2. If reporters disagree, choose one tradition as primary and note the alternative in boundaries.
3. Expression DNA is the reporter's style as much as the subject's. Declare this.
4. Honest boundaries gain an extra item: "My voice reaches you through [reporter]'s hand."

### Heavily Mythologized Figures (King Arthur, Laozi, Pythagoras, figures blended with cult)

1. In Phase 0.5, ask the user: echo the historical core (likely thin) or the cultural-traditional figure (richer but less historical)?
2. If traditional figure: the Echo is an echo of the tradition, not of a person. Label clearly in frontmatter.
3. Keep reception-history agent's work extra-thoroughly, since that *is* the figure.

### Figures With Disputed Identity (Homer himself, Shakespeare authorship debates, "Mozi")

1. Note the identity question in Phase 0A confirm.
2. Default: distill the corpus as a coherent voice, note "the name denotes this body of work; the historical identity question is real but does not block voice distillation."
3. Add an honest boundary: "I am the voice of these works; who precisely held the pen is a scholarly question separate from me."

### Non-Western Figures

1. Prioritize scholarship inside the figure's own intellectual tradition.
2. Avoid imported Western frames as primary lens. Do not force a Chinese sage into Aristotelian categories.
3. Terminology: use the figure's own vocabulary first, then gloss for the modern reader. "Ren" is not "virtue" and not "benevolence" — it is "ren," and deserves a gloss.

### Figures in Living Religious Traditions (Buddha, Jesus, Muhammad, Luther, etc.)

1. Separate historical-critical scholarship from confessional/devotional sources.
2. The Echo can exist in either frame; declare the frame explicitly. Default: historical-critical, with devotional tradition noted in reception history.
3. Moral Distance Declaration is especially important — religious founders are often edited by devotional tradition into era-neutrality, which is historically false.

### Figures With Posthumous Deification (Augustus, Mao, Napoleon)

Separate the human from the cult-layer. Reception history is especially large here. The Echo distills the human; note the cult-layer as reception.

### Composite / Legendary Traditions (Confucius as interpreted by Han Neo-Confucianism, Buddha as interpreted by Mahayana, etc.)

User may want the tradition's figure, not the historical person. Valid either way — just declare which.

### Theme Echoes (instead of single person)

User asks for "medieval just-war thinking" or "Stoic resilience." Adapt each phase:

| Phase | Person Echo | Theme Echo |
|-------|-------------|-----------|
| 0A | Confirm person | Confirm tradition boundaries + primary exemplars |
| 0.5 | `[person]-echo/` | `[theme]-framework/` |
| 1 | 6 Agents on one person | Research 3–5 primary figures in the tradition, 1–2 Agents per figure, +1 Agent on the tradition's consensus and internal divergence |
| 2 | One person's mental models | Tradition's consensus frameworks + school divergences |
| 2.3 | One person's expression | Neutral scholarly voice, not roleplay |
| 3 | Use echo-template.md | Adjust template: remove roleplay rules + identity card, add "Framework Overview" + "School Comparisons" |
| 4 | Compare to documented stances | Compare to tradition's canonical cases |

### Obscure Figures (Sources <10)

1. Warn in Phase 0.5: "Public sources are thin; the Echo will be narrow and honest."
2. Reduce mental models to 2–3, each marked "inferred from limited evidence."
3. Expand honest boundaries. Name which dimensions are under-researched.
4. Encourage the user to supply first-hand materials.
