import random


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}
    total_cases = 10000

    for _ in range(total_cases):
        heads_count = sum(random.choices([0, 1], k=10))
        results[heads_count] += 1

    for key in results:
        results[key] = (results[key] / total_cases) * 100

    return results
