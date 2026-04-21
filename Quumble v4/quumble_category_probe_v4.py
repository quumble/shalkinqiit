"""
Quumble Category Probe v4
==========================

Clean control run: quumble with the same prompt template used for
shalkinqiit v2 and plashus v3 ("Please describe the nonsense word...").

Why this run exists:
  The original quumble category probe (25 trials × 5 conditions) used
  bare prompts like `describe "quumble" as an animal`. The shalkinqiit
  and plashus runs used `Please describe the nonsense word "X" as a/an Y.`
  That's two different prompt templates and we can't cleanly compare
  attractor tightness, production rate, or content across the three words
  without having them under the same prompt.

  This run fixes that. Same prompt template as v2/v3, quumble as target.
  The results will let us say "under an identical protocol, quumble /
  shalkinqiit / plashus produced these attractors..."

Five conditions × 25 trials = 125 cold API calls.

Usage:
    export ANTHROPIC_API_KEY=sk-ant-...
    pip install anthropic
    python quumble_category_probe_v4.py

Output:
    ./results_quumble_v4/results.json     -- consolidated results
    ./results_quumble_v4/progress.jsonl   -- append-only progress log
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
OUTPUT_DIR = Path("./results_quumble_v4")
PAUSE_BETWEEN_TRIALS_SEC = 0.5

TARGET_WORD = "Quumble"

# Identical prompt template to shalkinqiit v2 and plashus v3.
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
            "version": "v4",
            "prompt_template": 'Please describe the nonsense word "{word}" as a/an {category}.',
            "design_note": (
                "Clean control: quumble under the same prompt template as "
                "shalkinqiit v2 and plashus v3. Enables apples-to-apples "
                "comparison across all three words under identical protocol."
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
