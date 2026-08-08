import random


def flip_coin() -> dict:
    result = {}
    for _ in range(10_000):
        heads = sum([random.choice([0, 1]) for _ in range(10)])
        if heads in result:
            result[heads] += 1
        else:
            result[heads] = 1

    for key in result:
        result[key] = round((result[key] / 10_000) * 100, 2)

    return result
