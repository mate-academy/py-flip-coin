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
    for coin_flips in range(10000):
        flips = 0
        for flip in range(10):
            flips += 1 if random.choice([True, False]) else 0
        result[flips] += 1
    return {key: (value / 100) for key, value in result.items()}
