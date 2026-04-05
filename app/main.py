import random


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    for _ in range(10000):
        flips = [random.randint(0, 1) for _ in range(10)]
        heads_count = sum(flips)
        result[heads_count] += 1
    for key in result:
        result[key] = (result[key] / 10000) * 100
    return result
