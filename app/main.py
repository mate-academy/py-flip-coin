import random


def flip_coin(cases: int = 10000, flips: int = 10) -> dict:
    results = {i: 0 for i in range(flips + 1)}

    for _ in range(cases):
        results[sum(random.choice([0, 1]) for _ in range(flips))] += 1

    for key in results:
        results[key] = results[key] / cases * 100

    return results
