from random import randint


def flip_coin():
    result = {
        i: 0 for i in range(0, 11)
    }

    for _ in range(10_000):
        total = 0
        for _ in range(10):
            total += randint(0, 1)
        result[total] += 1

    for i in result:
        result[i] /= 100

    return result
