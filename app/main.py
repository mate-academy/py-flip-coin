import random


def flip_coin() -> dict:
    result = {}
    for _ in range(10000):
        heads = sum(random.choice((1, 0)) for _ in range(10))
        if heads not in result:
            result[heads] = 1
        else:
            result[heads] += 1

    return {
        key: value / 100
        for key, value in result.items()
    }
