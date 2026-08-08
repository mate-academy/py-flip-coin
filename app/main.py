import random


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        result[heads] += 1
    for key in result:
        result[key] /= 100
    return result
