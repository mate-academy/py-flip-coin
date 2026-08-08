import random
from collections import defaultdict


def flip_coin() -> dict:
    results = defaultdict(int)
    trials = 10000
    flips_per_trial = 10

    for _ in range(trials):
        heads_count = sum(random.choice([0, 1])
                          for _ in range(flips_per_trial))
        results[heads_count] += 1

    results_percentage = {k: (v / trials) * 100 for k, v in results.items()}
    return results_percentage
