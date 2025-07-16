import random


def flip_coin() -> dict:
    result = {i: 0.0 for i in range(11)}

    for _ in range(10000):
        flips = [random.randint(0, 1) for _ in range(10)]
        result[sum(flips)] += 1

    for key in result:
        result[key] = round(result[key] / 10000 * 100, 2)

    return result
