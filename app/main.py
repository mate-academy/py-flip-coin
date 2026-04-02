import random
from collections import Counter


def flip_coin(num_flips: int = 10, num_trials: int = 10000) -> int:
    results_counter = Counter()

    for _ in range(num_trials):
        num_heads = sum(random.choice([0, 1]) for _ in range(num_flips))
        results_counter[num_heads] += 1

    results_percentage = {
        key: (value / num_trials) * 100
        for key, value in results_counter.items()
    }

    return results_percentage
