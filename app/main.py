import random
from collections import Counter


def flip_coin() -> dict:
    results = []
    for _ in range(10000):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        results.append(heads)
    counter = Counter(results)
    percentages = {k: v / 100 for k, v in counter.items()}
    return percentages


print(flip_coin())
