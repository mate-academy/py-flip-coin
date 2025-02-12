import random
from collections import Counter


def flip_coin(trials: int = 10000, flips_per_trial:int = 10) -> dict: 
    results = [
        sum(random.choice(
            [0, 1]
        ) for _ in range(flips_per_trial)) for _ in range(trials)
    ]
    counts = Counter(results)
    total = sum(counts.values())
    return {k: round(v / total * 100, 2) for k, v in sorted(counts.items())}
