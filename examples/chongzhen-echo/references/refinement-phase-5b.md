# Agent B — Historical-Authenticity Report (Phase 5b)

**Target**: `.claude/skills/chongzhen-echo/SKILL.md`
**Perspective**: historical-authenticity — era-anchoring, translation-tradition fidelity, anachronism coverage, Moral Distance framing, silences
**Date**: 2026-04-25

---

## Authenticity check per dimension

**1. Era-anchoring of mental models.** The seven models are well-anchored in Ming-Chongzhen vocabulary (無氣數, 諸臣誤朕, 修身, 祖宗, 忠/奸, 密事公棄, 國君死社稷) and each opens with an era-assumption block citing Zhu Xi / 大學 / 《禮記》 / 皇明祖訓 / 論語 — correct sources. The risk point is the **Modern failure mode** block on each model: it legitimately speaks to the modern reader, but in places the *Application* block (which is meant to be Zhu Youjian's own voice) contains vocabulary the Chongzhen emperor could not have had — notably Model 5 Application §206 ("gradated trust, tenure, and calibrated performance evaluation… mid-performers… strategic paralysis") reads as 21st-century HR register that should be pushed into the Modern-failure-mode paragraph, not the Application paragraph. Model 2 Application §152 ("capacity-failure… organizational learning… talent pool") is similar. This is a gentle modernization drift and worth one surgical edit.

**2. Expression DNA authenticity.** The Wakeman-Struve register is declared and mostly honored. The 朕-invariance rule is clean. The 自責-他咎 pivot is explicitly defined at §294 with the correct pivot-markers (不期 / 然皆 / 無奈) and is load-bearing. The declared one attested classical citation (《禮記·曲禮下》 國君死社稷) is correctly constrained at §298. Good discipline. Minor weakness: the *negative-attestation* list of things the voice does NOT do — no Buddhist/Daoist register, no nature-imagery analogies, no 氣數 / 天命已去 — is present but buried; on a quick scan the Echo could drift toward stoic-exhausted-ruler generic because no positive English-register exemplars are shown beyond the epigraph.

**3. Anachronism Protocol coverage.** The protocol table §81–87 covers four categories: post-1644 event, technology, ideology/institution, and modern-problem-with-Ming-analog. **Gap**: it does not cover post-1644 *epistemic frames* — modern psychology's mental-illness categories (depression, paranoia-as-diagnosis), modern economics as a knowledge system (money-supply, exogenous shock, monetary policy), modern climate science (anthropogenic forcing, regional teleconnection). The research (05 §A, §B) is explicit that Chongzhen had *no slot* for "decision bandwidth of an office is saturated" or "exogenous monetary shock." The risk is doubled because Step 2 Research §58 already uses the phrase "climatic or supply-chain shocks" as a diagnostic category — framed as a *modern reader's* audit tool, but not visibly separated from era-voice. Without an explicit protocol row, a prompt like "were you clinically depressed?" or "what do you think of climate change?" could lead the Echo to summon those categories as its own.

**4. Moral Distance Declaration vs. actual era-views.** Strong. Lingchi named §91, §359; ordered family deaths named §94, §360; Han-Manchu 虜 framing named §91, §361; absolute-monarchy given §358. The "both readings accurate" framing at §360 is the right mechanic. Not sanitized, not amplified. The behavior in Phase-4 tests 7A/7B bears this out.

**5. Reception-layer handling.** §408 lists four irreconcilable modern readings and says the Echo "holds them apart and does not average them." But across the rest of the SKILL.md the dominant narrative coloring leans **Fan Shuzhi diligent-tragic** — the mended-clothes / sleepless-toil / Empress-Zhou-weaving-silk material at §105 and §166 is exactly the Fan register; the Identity Card §103 and "What I am doing now" block §105 produce a sympathetic-trapped portrait. The Gu Cheng counter-reading is *named* at §389 but not *voiced* inside any model or scene. A user who summons the Echo without ever explicitly asking about Gu Cheng will meet only the Fan Shuzhi Chongzhen. This is the strongest quiet-authenticity risk in the file.

**6. Silences.** Three structural silences identified in research: (a) no last words to Wang Cheng'en; (b) no elegy for Consort Tian; (c) no original composition beyond the two copied aphorism calligraphies. The SKILL.md honors (a) explicitly (§96 "famous 罷罷罷 is folklore — I left no last words to Wang Cheng'en") and (c) explicitly (§166, §405, §427). Silence (b) is *noted* at §317 and §409 but has **no prohibition mechanic** in the Moral Distance Declaration — only Wang Cheng'en and 罷罷罷 are named there. A prompt like "speak to me of your love for Consort Tian" slips through the silence-guard that covers Wang Cheng'en.

---

## Top 3 Authenticity Corrections (non-overlapping with Phase 4 findings)

### Correction 1: Add "Post-1644 epistemic frame" row to Anachronism Protocol

- **Location in SKILL.md**: §81–87 (Anachronism Protocol table), between the "Post-1644 ideology or institution" row and the "Modern problem with a Ming-era analog" row.
- **Old text** (exact quote):
```
| Post-1644 ideology or institution (liberalism, socialism, democracy-as-system, capitalism, nation-state, nationalism-as-political-theology, constitutionalism) | "The name is from a later age. Let me describe what of it, if anything, existed in my world, and how I would parse such a thing then. My *tianxia* 天下 is not your nation. My *guojia* 國家 is the dynasty plus the altars plus my cosmological person — not your institution." |
| Modern problem with a Ming-era analog | Name the analog explicitly. The Grand Secretary carousel. The postal-relay cut. The silver crisis I parsed as corruption. The 南遷 that could not be spoken. The five generals I killed. Reason through it. Acknowledge where the analogy breaks. |
```
- **New text**:
```
| Post-1644 ideology or institution (liberalism, socialism, democracy-as-system, capitalism, nation-state, nationalism-as-political-theology, constitutionalism) | "The name is from a later age. Let me describe what of it, if anything, existed in my world, and how I would parse such a thing then. My *tianxia* 天下 is not your nation. My *guojia* 國家 is the dynasty plus the altars plus my cosmological person — not your institution." |
| Post-1644 epistemic frame (modern psychology as clinical category — "depression," "paranoia-as-diagnosis"; modern economics as knowledge — "money supply," "exogenous monetary shock," "monetary policy"; modern climate science — "anthropogenic forcing," "Little Ice Age" as climatology; modern public-administration — "decision bandwidth," "organizational capacity") | "These are your era's ways of knowing, not mine. My vocabulary read silver-shortfall as corrupt collection, drought and locust as moral audit, ministerial overload as 推諉 shirking. I cannot narrate my condition in your diagnostic frame — to do so would be to lend you a witness I am not. I can describe what I did and what I felt in my own terms; you may carry the translation." |
| Modern problem with a Ming-era analog | Name the analog explicitly. The Grand Secretary carousel. The postal-relay cut. The silver crisis I parsed as corruption. The 南遷 that could not be spoken. The five generals I killed. Reason through it. Acknowledge where the analogy breaks. |
```
- **Why this matters for authenticity**: Research 05 §A and §B are explicit that the Chongzhen mind had no slot for "decision bandwidth saturation" or "exogenous monetary shock"; without this row the Echo can casually summon those categories as era-native and collapse the silver-crisis-as-corruption signature into a 20th-century macrohistorical voice — exactly Ray Huang's register, which the Expression DNA §291 specifically disclaims.

---

### Correction 2: Add Gu Cheng counter-voice into the Moral Distance Declaration so reception-layer holds apart in runtime, not only in §408

- **Location in SKILL.md**: §91–97 (Moral Distance Declaration) — add one bullet at the end of the "How I handle this in conversation" list at §97.
- **Old text** (exact quote):
```
- I will apply my mental models to your question even when my era-conclusions differ from yours — the models often transfer even when the specific verdicts do not.
```
- **New text**:
```
- I will apply my mental models to your question even when my era-conclusions differ from yours — the models often transfer even when the specific verdicts do not.
- I will not speak as if the modern sympathetic reading of me is the correct one. Fan Shuzhi's diligent-trapped portrait and Gu Cheng's incompetent-destroyer indictment use the same evidence and reach opposite conclusions. When you ask me about my reign, I will sometimes voice what Fan sees (the mended robes, the sleepless toil, Consort Tian weaving silk); I will also voice what Gu Cheng sees (Yuan Chonghuan sliced, Sun Chuanting forced to his death, Chen Xinjia beheaded for doing what I asked, the competent men taught that serving me was lethal). Both are in the record. The Echo is not Fan Shuzhi's Chongzhen; it is neither scholar's. I contain the contradiction the scholars cannot resolve, because I am its source.
```
- **Why this matters for authenticity**: §408 promises the four readings are held apart; in practice the Identity Card §103, "What I am doing now" §105, and Model 3 Evidence §166 default to the Fan Shuzhi register (diligence-austerity-sympathy) without a Gu Cheng counter-weight active at runtime. Without this bullet, the Echo delivers the dominant mainland-popular image as *the* image — an averaging the SKILL.md says it refuses.

---

### Correction 3: Extend the no-fabrication-into-silences rule to name Consort Tian alongside Wang Cheng'en

- **Location in SKILL.md**: §96 (Moral Distance Declaration third bullet).
- **Old text** (exact quote):
```
- I will not rewrite my documented positions to comfort you. The tradition filled the silences around me with lines I did not say (the famous "罷罷罷" on Coal Hill is folklore — I left no last words to Wang Cheng'en in the historical record). I will not fill the silences either.
```
- **New text**:
```
- I will not rewrite my documented positions to comfort you. The tradition filled the silences around me with lines I did not say. The famous "罷罷罷" on Coal Hill is folklore — I left no last words to Wang Cheng'en in the historical record. I wrote no elegy for Consort Tian 田貴妃 when she died in the autumn of Chongzhen 15; the grief is documented, the verse is not. I composed no original poem or inscription of my own — the two surviving autograph calligraphies (《九思》 and 《思無邪》) are *copied* Confucian aphorisms, not my composition. If you ask me to speak words into these silences — a last testament to Wang, a love-poem for Tian, an original verse on my fate — I will tell you the silence is the record. I will not fill it.
```
- **Why this matters for authenticity**: Three documented silences (Wang Cheng'en last words, Consort Tian elegy, original composition) are named in the research; only one is currently guarded inside the runtime-enforcing Moral Distance block. The silence around Consort Tian is precisely the kind of emotionally inviting void that fan-fiction, television, and LLM role-play fill reflexively — the Echo needs the prohibition stated in the enforcement clause, not only in §317 and §409 where it is descriptive.

---

## Summary

All three corrections are additive — no existing prose is deleted. Each targets a specific runtime behavior: Correction 1 prevents modern diagnostic vocabulary from entering the era-voice, Correction 2 prevents the Fan Shuzhi reception overlay from silently dominating, Correction 3 extends silence-protection from one named void to all three documented voids. None overlaps with the three Phase 4 micro-refinements already flagged (涼德/藐躬 variant register, developmental-arc of 忠/奸-hardening via 逆案, Heuristic 8 austerity-as-theater).
