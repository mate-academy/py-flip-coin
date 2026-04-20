import random
from collections import defaultdict


def flip_coin(trials: int = 10000) -> dict:
    results = defaultdict(int)

    for _ in range(trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    return {k: round(v / trials * 100, 2) for k, v in sorted(results.items())}
