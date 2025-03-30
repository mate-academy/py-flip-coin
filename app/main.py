import random


def flip_coin() -> dict:
    result = {i: 0 for i in range(10)}

    for _ in range(10000):
        heads_count = sum(random.choice([0, 1]) for _ in range(0, 10))
        result[heads_count] = result.get(heads_count, 0) + 1

    for key, value in result.items():
        result[key] = round((value / 10000) * 100, 2)

    return result
