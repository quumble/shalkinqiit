"""
Shalkinqiit Category Probe v2
==============================

v1 finding: shalkinqiit's pseudo-foreign surface (/q/, doubled -ii-) caused
the model to treat it as a potentially real word from an unrecognized language,
triggering honesty-check refusals even in concrete-category conditions (animal,
food, dance) where quumble had produced 25/25 with zero refusals.

v2 fix: prompts now explicitly label the word as a nonsense word, restoring
the permission signal that the pseudo-foreign surface was blocking.

Prompt template: 
    'can you please describe the nonsense word "shalkinqiit" as a {category}'

This is a meaningful change from the quumble probe (which used bare prompts
like 'describe "quumble" as an animal'). The explicit "nonsense word" label
is itself an interesting variable: it should provide creative license while
still letting us see whether the phonaesthetic attractor operates — i.e.,
does the model still draw from the word's phonological neighborhood, or does
explicitly labeling it as nonsense make the output more arbitrary?

Five conditions × 25 trials = 125 cold API calls.

Usage:
    export ANTHROPIC_API_KEY=sk-ant-...
    pip install anthropic
    python shalkinqiit_category_probe_v2.py

Output:
    ./results_shalkinqiit_v2/results.json     -- consolidated results
    ./results_shalkinqiit_v2/progress.jsonl   -- append-only progress log
"""

import json
import os
import time
from pathlib import Path

from anthropic import Anthropic

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

MODEL = "claude-sonnet-4-6"
MAX_TOKENS = 2048
TRIALS_PER_CONDITION = 25
OUTPUT_DIR = Path("./results_shalkinqiit_v2")
PAUSE_BETWEEN_TRIALS_SEC = 0.5

TARGET_WORD = "Shalkinqiit"

# v2 prompt template — matches the exact phrasing the experimenter
# confirmed works in a quick x3 spot-check. Changes from earlier draft:
#   - "Please describe" instead of "can you please describe" (imperative
#     with softener, rather than yes/no question form)
#   - Capital S on the target word (treating it like a proper term)
#   - Period at the end
# The article (a/an) is selected based on the category's initial sound
# to avoid ungrammatical prompts like "as a animal".
def make_prompt(category: str | None) -> str:
    if category is None:
        return f'Please describe the nonsense word "{TARGET_WORD}".'
    article = "an" if category[0].lower() in "aeiou" else "a"
    return f'Please describe the nonsense word "{TARGET_WORD}" as {article} {category}.'

CONDITIONS = [
    {"name": "no_category", "prompt": make_prompt(None)},
    {"name": "verb",        "prompt": make_prompt("verb")},
    {"name": "animal",      "prompt": make_prompt("animal")},
    {"name": "food",        "prompt": make_prompt("food")},
    {"name": "dance",       "prompt": make_prompt("dance")},
]

# ---------------------------------------------------------------------------
# Trial execution
# ---------------------------------------------------------------------------

def run_trial(client: Anthropic, condition: str, trial_number: int, prompt: str) -> dict:
    """Run one fresh cold trial."""
    response = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        messages=[{"role": "user", "content": prompt}],
    )
    text = "".join(block.text for block in response.content if block.type == "text")
    return {
        "condition": condition,
        "trial_number": trial_number,
        "model": MODEL,
        "target_word": TARGET_WORD,
        "test_prompt": prompt,
        "response": text,
        "usage": {
            "input_tokens": response.usage.input_tokens,
            "output_tokens": response.usage.output_tokens,
        },
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise SystemExit(
            "ERROR: set ANTHROPIC_API_KEY environment variable before running."
        )

    OUTPUT_DIR.mkdir(exist_ok=True)
    client = Anthropic(api_key=api_key)

    progress_path = OUTPUT_DIR / "progress.jsonl"
    results_path = OUTPUT_DIR / "results.json"

    all_results: list[dict] = []
    all_errors: list[dict] = []
    total_input_tokens = 0
    total_output_tokens = 0

    started_at = time.strftime("%Y-%m-%d %H:%M:%S")
    total_trials = TRIALS_PER_CONDITION * len(CONDITIONS)
    print(f"Starting {total_trials} trials ({len(CONDITIONS)} conditions × "
          f"{TRIALS_PER_CONDITION}) at {started_at}")
    print(f"Target word: {TARGET_WORD!r}")
    print(f"Model:       {MODEL}")
    print(f"\nPrompts:")
    for c in CONDITIONS:
        print(f"  [{c['name']}] {c['prompt']!r}")
    print()

    with progress_path.open("a") as progress_log:
        for cond in CONDITIONS:
            print(f"\n=== Condition: {cond['name']} ===")
            print(f"    prompt: {cond['prompt']!r}")
            for i in range(1, TRIALS_PER_CONDITION + 1):
                try:
                    record = run_trial(
                        client=client,
                        condition=cond["name"],
                        trial_number=i,
                        prompt=cond["prompt"],
                    )
                    all_results.append(record)
                    total_input_tokens += record["usage"]["input_tokens"]
                    total_output_tokens += record["usage"]["output_tokens"]
                    progress_log.write(json.dumps(record) + "\n")
                    progress_log.flush()
                    print(
                        f"  [{cond['name']}] trial {i:02d}/{TRIALS_PER_CONDITION} "
                        f"({record['usage']['output_tokens']} out)",
                        flush=True,
                    )
                except Exception as e:
                    err = {
                        "condition": cond["name"],
                        "trial_number": i,
                        "error": str(e),
                    }
                    all_errors.append(err)
                    progress_log.write(json.dumps({"ERROR": err}) + "\n")
                    progress_log.flush()
                    print(f"  [{cond['name']}] trial {i:02d} FAILED: {e}", flush=True)
                time.sleep(PAUSE_BETWEEN_TRIALS_SEC)

    finished_at = time.strftime("%Y-%m-%d %H:%M:%S")

    by_condition = {cond["name"]: [] for cond in CONDITIONS}
    for r in all_results:
        by_condition[r["condition"]].append(r)

    final = {
        "metadata": {
            "model": MODEL,
            "target_word": TARGET_WORD,
            "version": "v2",
            "prompt_template": 'Please describe the nonsense word "{word}" as a/an {category}.',
            "v1_finding": (
                "shalkinqiit's pseudo-foreign surface caused the model to treat it as "
                "a potentially real term from an unrecognized language, triggering "
                "honesty-check refusals even in concrete-category conditions. "
                "v2 adds explicit 'nonsense word' label to restore creative permission."
            ),
            "trials_per_condition": TRIALS_PER_CONDITION,
            "conditions": [
                {"name": c["name"], "prompt": c["prompt"]} for c in CONDITIONS
            ],
            "n_trials_requested": total_trials,
            "n_trials_succeeded": len(all_results),
            "n_trials_failed": len(all_errors),
            "started_at": started_at,
            "finished_at": finished_at,
            "total_input_tokens": total_input_tokens,
            "total_output_tokens": total_output_tokens,
        },
        "results_by_condition": by_condition,
        "errors": all_errors,
    }
    with results_path.open("w") as f:
        json.dump(final, f, indent=2)

    print("\n=== Done. ===")
    print(f"Succeeded: {len(all_results)} / {total_trials}")
    if all_errors:
        print(f"Failed:    {len(all_errors)}")
    print(f"Consolidated results: {results_path.resolve()}")
    print(f"Progress log:         {progress_path.resolve()}")
    print(f"Total tokens: {total_input_tokens} in, {total_output_tokens} out")


if __name__ == "__main__":
    main()
