import random


def flip_coin() -> dict:
    results = {}

    for _ in range(10000):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] = results.get(heads_count, 0) + 1

    results_percentage = {k: round(v / 10000 * 100, 2)
                          for k, v in results.items()}
    return results_percentage
