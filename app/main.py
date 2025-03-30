import random


def flip_coin() -> dict:
    result = {}
    for i in range(10000):
        heads = sum(random.randint(0, 1) for j in range(10))
        result[heads] = result.get(heads, 0) + 1

    for key in result:
        result[key] = (result[key] / 10000) * 100

    return result
