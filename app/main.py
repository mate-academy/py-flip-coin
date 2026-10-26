import random


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    for i in range(10000):
        heads = 0

        for _ in range(10):
            heads += random.randint(0, 1)

        result[heads] += 1

    for heads in result:
        result[heads] = result[heads] / 10000 * 100

    return result
