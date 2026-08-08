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
    for _ in range(1, 10001):
        heads = 0
        for i in range(10):
            coin = random.randint(0, 1)
            if coin == 1:
                heads += 1
        result[heads] += 1

    for key, value in result.items():
        result[key] = value / 100

    return result
