import random


def flip_coin() -> dict:
    result = {}

    for _ in range(10000):
        head = 0
        for _ in range(10):
            if random.random() < 0.5:
                head += 1

        if head in result:
            result[head] += 1
        else:
            result[head] = 1

    for key in result:
        result[key] = round(result[key] / 10000 * 100, 2)

    return result
