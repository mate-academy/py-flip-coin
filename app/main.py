import random


def flip_coin() -> dict:
    results = {}
    cases = 10000

    for _ in range(cases):
        heads_count = sum(random.randint(0, 1) for _ in range(10))
        results[heads_count] = results.get(heads_count, 0) + 1

    for key in results:
        results[key] = (results[key] / cases) * 100

    return results
