import random
from collections import Counter


def flip_coin() -> dict:
    total_cases = 10000
    results = []

    for _ in range(total_cases):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results.append(heads_count)

    counts = Counter(results)

    percentages = {
        heads: (counts.get(heads, 0) / total_cases) * 100
        for heads in range(11)
    }

    return percentages
