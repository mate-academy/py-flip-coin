import random


def flip_coin() -> dict:
    drops = {
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
    for _ in range(10000):
        count = 0
        for _ in range(10):
            count += random.randint(0, 1)
        drops[count] += 1
    for key in drops:
        drops[key] = drops[key] / 100
    return drops
