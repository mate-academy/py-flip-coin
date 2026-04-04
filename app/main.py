import random
from collections import defaultdict


def flip_coin() -> dict:
    experiments = 10000
    coin_flips = 10
    results = defaultdict(float)

    for _ in range(experiments):
        heads = sum(1 for _ in range(coin_flips) if random.random() < 0.5)
        results[heads] += 1

    for heads, count in results.items():
        results[heads] = round((count / experiments) * 100, 2)

    return dict(results)
