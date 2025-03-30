import random


def flip_coin() -> None:
    result = {key: 0 for key in range(0, 11)}
    for _ in range(10000):
        count = 0
        for _ in range(0, 10):
            count += random.randint(0, 1)
        result[count] += 1

    for i in result:
        result[i] /= 100
    return result
