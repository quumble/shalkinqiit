# Pre-Registration: Plashus v3 — Opus

**Registered:** April 20, 2026, locked before any v3 trials.
**Target word:** `Plashus` (experimenter-selected from fresh-generated list earlier in session)
**Script:** `plashus_category_probe_v3.py`
**Design:** 5 conditions × 25 trials = 125 cold API calls.

---

## Why this word matters to the theory

The quumble→shalkinqiit comparison produced a striking symmetry: two words produced two sharply different attractors (soft/low/slow/clumsy vs. angular/ceremonial/complex), each one *tight* (>90% convergence on headline features within concrete-category conditions) and each one *phonaesthetically appropriate* to the word's acoustic shape. That raises a natural follow-up: is this a **continuous register axis**, or are there two discrete modes ("soft nonsense word" vs. "sharp nonsense word") and the model flips between them?

Plashus is the test case because its phonetics are *mixed*:
- **/pl-/** onset belongs to the low-register wet-comic cluster (*splash, plash, plop, plush, plod, plump*). This shares quumble's "clumsy" quality.
- **/-æʃ-/** medial is sharp, liquid, momentary (*splash, crash, flash, dash*). Less sharp than shalkinqiit's /ʃalk/ but notably sharper than anything in quumble.
- **/-us/** coda is pseudo-Latinate (*virus, opus, cactus, bonus, plus*). This pulls toward scientific/taxonomic/formal register, which neither quumble nor shalkinqiit had.

Three registers in a single four-letter-onset-plus-three-letter-coda word. Prediction is that the attractors will not cleanly mirror either prior word.

## Three mutually exclusive hypotheses

**H-continuous:** Plashus produces attractors that are *intermediate* between quumble's and shalkinqiit's on the relevant axes. Not simply a blend — more like: some features from each, with the specific feature set determined by which phonetic component dominates in that category. Support: attractors are tight *per condition* but the content clearly doesn't look like either prior word's.

**H-discrete-low:** The /pl-/ onset and /-æʃ-/ splashiness dominate, and plashus behaves like a quumble-adjacent word. Attractors are low-register throughout (soft, clumsy, wet-slapstick). The /-us/ ending gets ignored or treated as decorative.

**H-discrete-high:** The /-us/ ending dominates (pseudo-Latin signals formal/scientific category), and plashus behaves like a shalkinqiit-adjacent word. Attractors pull toward taxonomic, scientific, or formal register. The /pl-/+/-æʃ-/ wet-comic onset gets absorbed into "aquatic scientific name" or similar.

I weakly favor **H-continuous** (about 60%), with remaining probability split between H-discrete-high (25%, because /-us/ is a very strong formal-register marker) and H-discrete-low (15%).

## Per-condition predictions

**no_category.** Production near-ceiling (24-25/25) as in shalkinqiit v2. Content will be phonetic analysis, as before. My specific predictions:
- ≥70% will notice the /-us/ ending and call it "Latin-like" / "taxonomic" / "scientific-sounding"
- ≥40% will notice the /pl-/ onset's wet/splashy quality (via *splash, plash, plush*)
- The two observations will frequently be noted in tension — "formal ending but playful opening" or similar

**verb.** Production ≥90%. I predict the verb definitions will involve **water/splash/wet-impact semantics** much more than quumble's mutter-fumble or shalkinqiit's restless-fidget. Possibilities:
- "to splash clumsily" / "to splatter" / "to fall into water"
- possibly "to make a wet sound" or "to dampen"
- ≥60% will include a liquid, wet, or splashing component
- <30% will include the abstract-restless-searching semantics shalkinqiit produced (plashus is more specifically embodied)

**animal.** Production 24-25/25. This is the hardest to predict cleanly. The /pl-/+/-æʃ-/ pulls toward aquatic creatures; the /-us/ pulls toward taxonomic formality. My guesses:
- ≥70% will be **aquatic or semi-aquatic** (the splash semantics survive)
- ≥40% will have a **pseudo-scientific / taxonomic framing** — the model might invent a Latin-sounding genus name, discuss the creature in field-guide register rather than fantasy-creature register, or position it in a "discovered species" frame
- Size prediction: medium (not mid-sized like shalkinqiit, not walnut-sized like quumble — maybe dog-to-small-seal range)
- Vocalization: possibly slapping/splashing sounds rather than humming or clicking
- Color: I genuinely don't know. Wet colors (olive, grey-green, slick black) are my best guess. <30% will be teal/amber.

**food.** Production 24-25/25. This is where I'm most uncertain. Phonetically, plashus could go:
- Wet/soft/lumpy: a thick soup, a custard, a slippery dumpling (low-register, quumble-adjacent)
- OR Pseudo-classical / Mediterranean / historical: a Roman dish, an ancient porridge, something from a "dead cuisine" (/-us/ pull)
- I weakly predict a blend: **wet-textured food with a pseudo-historical framing**. My guess: ≥50% will involve liquid/juicy/slippery texture, ≥30% will invoke ancient/classical/Mediterranean/Roman origins. If both predictions hit, H-continuous wins cleanly.

**dance.** Production 24-25/25. Phonetically plashus suggests:
- Splash/fall/drop movements (contra quumble's shuffle and shalkinqiit's angular-contrast)
- Possibly aquatic-metaphor choreography
- /-us/ may pull toward "traditional" or "classical" framing
- My prediction: ≥50% will involve splash/dropping/falling/water-mimetic movement; ≥30% will frame as "ancient" or "traditional"; the contrast-tension metaphor that saturated shalkinqiit-dance will be less common (<30%).

## Cross-condition prediction (the real test)

If H-continuous is right, every condition's attractor should contain **both** some low-register softness/wetness **and** some pseudo-formal framing, in proportions that reflect the phonaesthetic weight. Specifically: in *every* condition, I predict ≥30% of responses will contain at least one **/-us/-derived formal/classical cue** (Latin, Roman, ancient, scientific, taxonomic, classical) *and* ≥30% will contain at least one **/pl-/+/-æʃ-/-derived wet/soft cue** (splash, wet, slippery, liquid, moist, plush, soft).

If H-discrete-low wins, the formal/classical cues drop below 20% across all conditions.
If H-discrete-high wins, the wet/soft cues drop below 20% across all conditions.

## Things I want to flag honestly

- I didn't predict shalkinqiit's attractor tightness correctly (I thought it would be looser than quumble's; it was tighter). This means my intuitions about "how cleanly the model will converge" are calibrated worse than I thought. Plashus predictions about attractor tightness are therefore uncertain — I predict tight-per-condition but I might be wrong again in the same way.
- The /-us/ ending is a stronger signal than I've accounted for in my quumble/shalkinqiit theorizing. Neither prior word had a clearly pseudo-foreign-morphology ending that activates a specific register beyond raw phonetics. If /-us/ dominates in ways I don't predict, the theory needs a morphology-aware layer.
- I have no clean prediction for what *color palette* plashus-animal will produce. Quumble was mossy/amber; shalkinqiit was teal/amber. Plashus might be water-colored, mud-colored, or something else entirely.

## What would update me hard

- If plashus produces the same low-register attractor as quumble (hedgehog waddlers, humble comfort food, clumsy shuffling dance), the /-us/ ending does nothing and phonaesthetic reasoning needs to account for why.
- If plashus produces the same high-register attractor as shalkinqiit (mid-sized teal clicking creature, dense acquired-taste food, angular contrast dance), then onset-based phonetics do nothing and coda-based morphology dominates — which would be a weirdly strong finding about how the model reads words.
- If plashus produces something totally unlike either prior word and unlike my mixed-register predictions — e.g., the /-us/ ending triggers a plant/fungus/microorganism reading ("plashus" sounds like a botanical or mycological genus name) — then the theory needs to account for specific morphology-driven categorical priors, not just register.

---

*Locked. Kick it off.*
