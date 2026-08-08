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
        10: 0,
    }
    coin = ["H", "T"]
    container = []
    for case in range(10001):
        for drop in range(10):
            container.append(random.choice(coin))
        result[container.count("H")] += 1
        container = []

    for key, value in result.items():
        result[key] = value / 100

    return result
