from random import randint


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    for i in range(10000):
        head = sum([randint(0, 1) for i in range(10)])
        result[head] += round((1 * 100 / 10000), 2)
    return result
