import random


def flip_coin() -> dict:
    dropped = {key: 0 for key in range(0, 11)}
    for _ in range(10000):
        total = 0
        for _ in range(10):
            total += random.randint(0, 1)
        dropped[total] += 1

    for i in dropped:
        dropped[i] /= 100
    return dropped
