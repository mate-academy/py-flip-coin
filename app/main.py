import random
from collections import Counter


def flip_coin(trials: int = 10000, flips: int = 10) -> dict:
    results = [
        sum(random.choice([0, 1]) for _ in range(flips))
        for _ in range(trials)
    ]
    counts = Counter(results)
    total_cases = sum(counts.values())
    return {
        k: round(v / total_cases * 100, 2)
        for k, v in sorted(counts.items())
    }
