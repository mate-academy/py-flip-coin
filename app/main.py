import random


def flip_coin() -> dict:
    result = {i: 0.0 for i in range(11)}
    for _ in range(10000):
        heads_count = sum(random.randint(0, 1) for _ in range(10))
        result[heads_count] += 1
    for key in result:
        result[key] = round(result[key] / 100, 2)
    return result
