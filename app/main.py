import random
from collections import Counter


def flip_coin(num_cases: int = 10000, num_flips: int = 10) -> dict:
    results = Counter()

    for _ in range(num_cases):
        heads_count = sum(random.randint(0, 1) for _ in range(num_flips))
        results[heads_count] += 1

    percentage_results = {
        key: (value / num_cases) * 100 for key, value in results.items()}

    return percentage_results
