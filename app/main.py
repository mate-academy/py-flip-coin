import random


def flip_coin(cases: int = 10000) -> dict:
    result = {}

    for _ in range(cases):
        count = 0
        for _ in range(10):
            if random.random() < 0.5:
                count += 1
        if count in result.keys():
            result[count] += 1
        else:
            result[count] = 1

    for key in result:
        result[key] /= cases
        result[key] *= 100

    return dict(sorted(result.items()))
