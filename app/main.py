import random


def flip_coin() -> dict[int, float]:
    result = {i: 0 for i in range(0, 11)}
    for flip in range(10000):
        count = 0
        for el in range(10):
            if random.choice([0, 1]) == 0:
                count += 1
        result[count] += 1

    result = {i: value / 100 for i, value in enumerate(result.values())}

    return result
