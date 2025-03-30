import random
from collections import Counter


def flip_coin(num_trials: int = 10_000, num_flips: int = 10) -> dict:
    results = [
        sum(random.choice([0, 1]) for _ in range(num_flips))
        for _ in range(num_trials)
    ]
    counts = Counter(results)
    percentages = {k: (v / num_trials) * 100 for k, v in counts.items()}

    for i in range(num_flips + 1):
        percentages.setdefault(i, 0)

    return percentages
