from random import randint


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    for _ in range(10000):
        orel = sum([randint(0, 1) for _ in range(10)])
        result[orel] += round((1 * 100 / 10000), 2)
    return result
