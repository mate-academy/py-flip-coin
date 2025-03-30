import random
from collections import defaultdict


def flip_coin() -> dict:
    results = defaultdict(int)
    for _ in range(10000):
        heads_count = sum([random.choice([0, 1]) for _ in range(10)])
        results[heads_count] += 1
    for key in results:
        results[key] = round((results[key] / 10000) * 100, 2)
    return dict(sorted(results.items()))
