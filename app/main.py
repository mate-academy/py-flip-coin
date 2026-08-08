import random


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    for _ in range(10000):
        count = 0
        for _ in range(10):
            if random.randint(0, 1) == 0:
                count += 1
        result[count] += 1
    for key in result:
        result[key] = round(result[key] / 100, 2)
    return result
