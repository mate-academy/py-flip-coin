import random
from typing import Dict


def flip_coin() -> Dict[int, float]:
    trials = 10000
    flips_per_trial = 10
    results: Dict[int, int] = {i: 0 for i in range(11)}

    for _ in range(trials):
        heads_count = sum(
            random.choice([0, 1]) for _ in range(flips_per_trial)
        )
        results[heads_count] += 1

    return {
        heads: round((count / trials) * 100, 2)
        for heads, count in results.items()
    }
