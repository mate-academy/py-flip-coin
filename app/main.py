import random


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}

    for _ in range(10000):
        count = 0
        for _ in range(10):
            count += random.randint(0, 1)
        result[count] += 1

    for value in result:
        result[value] /= 100
    return result
