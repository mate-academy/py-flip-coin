import random


def flip_coin() -> dict:

    results = {i: 0 for i in range(11)}

    for i in range(10000):
        flip = sum(random.choice([0, 1]) for _ in range(10))
        results[flip] += 1

    for key in results:
        results[key] = round(results[key] / 10000 * 100, 2)

    return results
