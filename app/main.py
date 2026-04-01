import random
from typing import Dict


def flip_coin(
        trials: int = 10000,
        flips_per_trial: int = 10
) -> Dict[int, float]:
    results = {i: 0 for i in range(flips_per_trial + 1)}

    for _ in range(trials):
        heads_count = sum(
            random.choice([0, 1]) for _ in range(flips_per_trial)
        )
        results[heads_count] += 1

    for key, value in results.items():
        results[key] = (value / trials) * 100

    return results
