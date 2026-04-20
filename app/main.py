import random


def flip_coin() -> dict:
    result = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }
    for i in range(10000):
        quantity = 0
        for ii in range(10):
            heads = random.randint(0, 1)
            if heads == 0:
                quantity += 1
        result[quantity] += 1
    for key, value in result.items():
        result[key] = round(value / 10000 * 100, 2)
    return result
