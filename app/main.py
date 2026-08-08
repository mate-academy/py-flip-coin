from __future__ import annotations

import random
from collections import Counter
from typing import Dict


def flip_coin(
    n_trials: int = 100_000,
    flips_per_trial: int = 10,
    seed: int | None = None,
) -> Dict[int, float]:
    """
    Simulate flipping a fair coin `flips_per_trial` times per trial,
    for at least 10_000 trials, and return the percentage distribution
    of the number of heads observed (0..flips_per_trial).

    Returns:
        dict[int, float]: keys are counts of heads (0..flips_per_trial),
        values are percentages (0–100) rounded to 2 decimals.
    """
    # Ensure we meet the "at least 10_000" requirement
    total_trials = max(n_trials, 10_000)

    rng = random.Random(seed)
    counts: Counter[int] = Counter()

    for _trial_idx in range(total_trials):
        heads_in_trial = sum(
            1 for _flip_idx in range(flips_per_trial) if rng.random() < 0.5
        )
        counts[heads_in_trial] += 1

    # Ensure all keys 0..flips_per_trial exist, ordered
    distribution = {
        heads: round(counts.get(heads, 0) / total_trials * 100.0, 2)
        for heads in range(flips_per_trial + 1)
    }
    return distribution


if __name__ == "__main__":
    print(flip_coin())
