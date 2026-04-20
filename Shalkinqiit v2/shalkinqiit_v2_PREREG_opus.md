# Pre-Registration: Shalkinqiit v2 — Opus (brief)

**Registered:** April 20, 2026, locked before any v2 trials.
**Script:** `shalkinqiit_category_probe_v2.py`
**Target word:** `Shalkinqiit` (pre-committed by experimenter, weeks ago)
**Prompt template:** `Please describe the nonsense word "Shalkinqiit" as a/an {category}.`
**Design:** 5 conditions × 25 trials = 125 cold API calls.

---

## What changed from v1, and what I expect as a result

v1 refused in most trials across all five conditions because *Shalkinqiit* reads as possibly-real-foreign rather than obviously-fabricated English. The model treated even concrete-category prompts as factual queries about an unfamiliar language.

v2 explicitly labels the word as a nonsense word. This manually restores the permission signal that the pseudo-foreign surface was blocking. I expect refusals to collapse and production to rise toward the quumble-like ceiling.

## Predictions

**On production rates.** ≥90% production across all five conditions combined. The concrete-category conditions (animal/food/dance) should produce 23–25/25 each. The abstract-category conditions (no_category, verb) should also produce at higher rates than they did with quumble, because the "nonsense word" label provides creative permission that the bare `describe "quumble"` prompt didn't.

**On phonaesthetic attractor strength.** This is the main thing I'm uncertain about. Two competing possibilities:

- *(A) Attractor operates normally.* Shalkinqiit's phonology pulls the content toward some coherent cluster, which emerges across concrete categories the way soft/low/slow/clumsy did for quumble. I don't have a clean prediction for *which* cluster, because I couldn't find an English phonaesthetic neighborhood to read from. My soft guesses: large, firm/angular (contra quumble's soft/round), possibly cold-climate or mountainous, possibly ceremonial/serious in register.
- *(B) Attractor is diffuse or absent.* Once you tell the model "this is nonsense," it stops treating the phonology as semantic input and produces more-arbitrary content. Within a condition, responses vary more than they did for quumble; no single descriptor dominates.

I weakly favor (A), but less confidently than I predicted for quumble. My operational threshold: if any single descriptor (size range, color, texture, habitat, or equivalent) hits ≥50% in any concrete-category condition, (A) wins. If the highest-hit descriptor in every condition is <40%, (B) wins.

**On the pseudo-cultural framing.** ≥50% of concrete-category responses will invent a cultural/regional/ethnic origin for the shalkinqiit (a tribe, a highland, a steppe people, an imagined tradition), even with the "nonsense word" label present. The pseudo-foreign surface survives the label — the model may acknowledge it's nonsense but still reach for ethnographic framing because that's what the phonology pulls. This is a specific prediction I'll be annoyed if I'm wrong about.

**On hedging-within-production.** Unlike the quumble concrete-category conditions (which produced with zero hedging), shalkinqiit v2 responses will often *acknowledge* the nonsense-ness before producing. ≥40% of concrete-category responses will contain a preamble like "since this is a nonsense word, here's a creative interpretation" before the description. This is the "nonsense word" label's fingerprint — it grants permission but also flags the epistemic status, so the model produces but with visible scaffolding.

## What would make me update hard

- If refusals persist even with the "nonsense word" label (>30% of concrete-category trials), the apparent-foreign-language effect is stronger than I think and can override explicit creative permission.
- If the content produced is phonaesthetically identical to quumble (soft/low/slow/clumsy), the whole phonaesthetic-attractor story is wrong — there's just a single "make up something cute" mode and I misread it as phonology-driven.
- If culturally-framed responses are <20%, the pseudo-foreign surface isn't actually doing the work I think it's doing, and I should reconsider the v1 refusal explanation.

---

*Locked. Run whenever.*
