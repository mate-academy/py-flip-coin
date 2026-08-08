import random


def flip_coin() -> dict:
    num_cases = 10000
    num_flips = 10
    results = {}

    for i in range(num_cases):
        heads_count = sum(random.randint(0, 1) for _ in range(num_flips))
        results[heads_count] = results.get(heads_count, 0) + 1

    for key, value in results.items():
        results[key] = (value / num_cases) * 100

    return results
