import random
from collections import Counter


def flip_coin() -> dict:

    num_experiments = 10000
    results = []

    for _ in range(num_experiments):
        num_heads = sum(random.choice([0, 1]) for _ in range(10))
        results.append(num_heads)

    counts = Counter(results)
    percentages = {
        k: round((v / num_experiments) * 100, 2) for k, v in counts.items()
    }
    return percentages
