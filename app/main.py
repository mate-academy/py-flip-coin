import random


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}
    cases = 10000

    for _ in range(cases):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    for key in results:
        results[key] = round(results[key] / 100, 2)

    return results
