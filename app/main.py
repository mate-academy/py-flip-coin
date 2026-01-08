import random


def flip_coin() -> dict:
    result = {}
    for _ in range(10000):
        flips = sum([random.choice([0, 1]) for _ in range(10)])

        result[flips] = result.get(flips, 0) + 1

    for key, value in result.items():
        result[key] = (value / 10000) * 100
    return result
