import random


def flip_coin() -> dict:
    result = {}

    for _ in range(10000):
        occurrence = 0
        for _ in range(10):
            occurrence += random.randint(0, 1)
        result[occurrence] = result.get(occurrence, 0) + 1

    for key, value in result.items():
        result[key] = round((value / 10000) * 100, 2)

    return result
