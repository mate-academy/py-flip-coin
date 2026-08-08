import random

from collections import defaultdict


def flip_coin() -> dict:
    results = defaultdict(int)
    for _ in range(10000):
        count_head = sum(random.choice([0, 1]) for _ in range(10))
        results[count_head] += 1
    for count_head in results:
        results[count_head] = round((results[count_head] / 100), 2)
    return results
