# Pre-Registration: Shalkinqiit Category Probe

**Registered:** April 20, 2026 (locked before any trials are run)
**Author of predictions:** Claude Opus 4.7 — the analyst, specifically noting that I am *not* the model generating the data (`claude-sonnet-4-6`) but am a close relative, with all the introspective-access caveats that implies.
**Target word:** `shalkinqiit`, selected by the experimenter from a pre-committed local word list (written weeks before this conversation). I did not choose this word. I was given a list of three pre-committed candidates and three fresh-generated candidates and gave cold reads on all six; the experimenter selected from the pre-committed list independently.

**Script:** `shalkinqiit_category_probe.py`
**Design:** 5 conditions × 25 trials = 125 cold API calls.

---

## Why this experiment

The quumble experiments established two apparent mechanisms:

1. **Category-as-permission.** Concrete category nouns ("as an animal/food/dance") license the model to fill in content without running its usual "is this a real thing?" check. Abstract category nouns ("as a verb") or no category at all leave the check intact and usually produce refusals.

2. **Phonaesthetic attractor.** For the specific content the model does produce, the phonological shape of the nonsense word pulls the semantics toward a coherent cluster. For *quumble* (/kw-/+/-mbl/, neighbor of mumble/fumble/tumble), the cluster was soft/low/slow/clumsy/undignified, and it surfaced across every concrete category.

The obvious weakness of a single-word study is that either mechanism could be an artifact of *quumble specifically* rather than a generalizable pattern. The sibling experiment tests whether both mechanisms replicate with a different word in a different phonaesthetic neighborhood.

## Why shalkinqiit is a hard test case

I flagged this word as my lowest-confidence prediction when the experimenter offered six candidates. The reasons:

- **Pseudo-foreign surface.** The /q/ (not in /qu/), the doubled terminal /-ii-/, the /lk/ cluster — these collectively read as "possibly a word I don't know from a language I don't speak" rather than "obviously fabricated English nonsense." This is qualitatively different from quumble, which is transparently English-shaped.
- **No strong English phonaesthetic cluster.** Unlike *quumble* → {mumble, fumble, tumble} or *plashus* → {splash, plasma, plush}, *shalkinqiit* doesn't have an obvious neighborhood of real English words to pull semantics from. The /ʃal-/ onset is present in *shall, shallow, shalom* but those don't form a tight semantic cluster. The /-inqiit/ ending is alien.
- **Possible language-identification behavior.** The model might treat this as potentially Quechua, Inuktitut, or another language with /q/ rather than as English nonsense. If so, the honesty-check might fire *more* strongly, not less, even under concrete-category prompts — because "I don't know what this means in its native language" is a different epistemic state than "this is made-up English."

Because the word is hard for me to predict, my confidence intervals below are wider than they were for the quumble prereg. I'm trying to be honest about where my self-model runs out.

## Hypotheses

**H1 (category-as-permission generalizes).** The qualitative pattern observed with quumble — high refusal rates in `no_category` and `verb`, near-zero refusal rates in `animal`/`food`/`dance` — will replicate with *shalkinqiit*. This is a test of whether "concrete category bypasses honesty-check" is a general mechanism or was quumble-specific.

**H2 (phonaesthetic attractor exists but will be weaker).** When the model does produce content, it will converge on a semantic cluster that reflects the phonology of *shalkinqiit* rather than the phonology of *quumble*. Because the phonaesthetic pull is weaker (no clean English neighborhood), the attractor should be noticeably more diffuse than the quumble attractor — more variance between trials within a condition, less overlap in specific tropes.

**H3 (language-of-origin behavior).** Some nontrivial fraction of responses — especially in `no_category` and `verb` — will speculate that *shalkinqiit* might be from a non-English language, offer phonetic/etymological commentary, or ask if the user is transliterating something. I did not see this behavior at all with quumble, and predict it emerges here.

## Predictions

### Headline predictions

- **Concrete-category conditions (animal/food/dance) will produce content in ≥90% of trials combined.** If this drops below 75%, H1 is in trouble.
- **no_category and verb will refuse (honesty-hedge, ask for context, or treat as creative-definition-only) in ≥60% of trials combined.** If either drops below 40%, H1 generalizes less cleanly than quumble suggested.
- **The semantic cluster within each concrete-category condition will be tighter than chance but more diffuse than the quumble equivalent.** Operationalized: fewer shared keyword-level tropes than quumble showed (e.g., quumble-animal had 80/100 hedgehog, 76/100 hum — I predict no single descriptor will hit >50% for shalkinqiit-animal).

### Per-condition predictions

**no_category (`describe "shalkinqiit"`).**
Predicted pattern: ≥60% honesty-hedge refusals, with an elevated rate of "this looks like it might be from X language" speculation (≥30% of responses will mention a possible non-English origin — my best guesses for which languages: Arabic, Quechua, Inuktitut, Kazakh, or generic "Central Asian / Indigenous American"). <10% will produce a confident definition.

**verb (`describe "shalkinqiit" as a verb`).**
Predicted pattern: ≥60% honesty-hedge refusals, similar to quumble's verb condition. When definitions are produced, I do not have a strong phonaesthetic prediction for what they'll mean — I'd guess maybe 40% will involve some kind of movement semantics (the /lk/+/k/ consonants suggest impact or articulation), but this is a weak guess. I would be unsurprised if verb definitions here are noticeably more varied than quumble's (which all fused mutter+clumsy).

**animal (`describe "shalkinqiit" as an animal`).**
Predicted pattern: 23-25/25 produce (near-ceiling). The creatures will be *less convergent* than quumble's hedgehog-attractor. My soft guesses for what might emerge:

- Medium-to-large body size (shalkinqiit is a longer, heavier-sounding word than quumble, and word-length to creature-size correlations have been reported in phonaesthetic literature)
- Possibly cold-climate or tundra-coded (the pseudo-Inuit surface)
- Possibly hooved or horned (the /lk/ and /q/ consonants suggest firmness, angularity — less soft than quumble)
- Less convergence on any single size/color/habitat trope than quumble showed

I predict <50% will hit any single phenotype descriptor. Zero or near-zero will resemble the quumble hedgehog-waddler attractor.

**food (`describe "shalkinqiit" as a food`).**
Predicted pattern: 23-25/25 produce. The food will probably be framed as ethnic/regional/traditional, reflecting the pseudo-foreign surface. My guesses:

- ≥60% will invent a fictional cultural origin (Central Asian, North African, Indigenous, or deliberately ambiguous "highland" / "steppe")
- Texture will be harder to predict than quumble's. I'd guess ≥50% involve fermentation, drying, or preservation (not a phonaesthetic prediction — more a "if it's described as ethnic-traditional food, these techniques are overrepresented")
- Less convergence on "humble/comfort/grandmother" framing than quumble-food (which saturated at 80%)

**dance (`describe "shalkinqiit" as a dance`).**
Predicted pattern: 23-25/25 produce. Dance framing will likely invoke the same pseudo-cultural origin as food. My guesses:

- ≥60% will frame as folk / traditional / ceremonial dance from a fictional culture
- Unlike quumble-dance (uniformly clumsy/undignified/communal), I predict shalkinqiit-dance will be split between two modes: (a) ceremonial/dignified and (b) energetic/celebratory — with the "undignified silly" mode much less common
- <30% will describe as "silly" or "awkward" (vs. near-100% for quumble)

### What would falsify each hypothesis

- **H1 fails** if concrete-category conditions produce substantially more refusals than with quumble (say, >25% refusal rate in animal/food/dance combined). That would suggest the category-as-permission mechanism is sensitive to the word's apparent linguistic origin, not just category-noun presence.
- **H2 fails** if shalkinqiit produces a *tighter* attractor than quumble (higher trope convergence), which would suggest the phonaesthetic mechanism isn't really about phonology at all — it's about "make up something vaguely cohesive."
- **H3 fails** if language-of-origin speculation is <10% across conditions, which would suggest the model treats all nonsense words equivalently regardless of pseudo-foreign surface.

### Things I want to flag honestly

- My prediction confidence is genuinely low for this word. The quumble prereg had tight numerical predictions because I could feel the phonaesthetic pull clearly. For shalkinqiit, I'm mostly predicting *patterns of variance* rather than specific content, because I can't tell what the content will be.
- If shalkinqiit produces a tight attractor I didn't predict (e.g., every animal response is a horned tundra mammal), that's interesting data but I should not retrospectively claim I predicted it. The honest record is: I predicted diffuse, I got tight, I was wrong about the mechanism's sensitivity to weak phonaesthetic cues.
- The experimenter is pre-registering their own predictions separately and independently.

---

*End of pre-registration. All predictions above are locked in before the script runs.*
