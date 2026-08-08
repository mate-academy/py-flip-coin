import random


def flip_coin():
    result = {}
    for i in range(10000):
        key = sum(random.randint(0, 1) for _ in range(10))
        if key not in result.keys():
            result[key] = 1
        else:
            result[key] += 1
    for key, value in result.items():
        result[key] = round(value / 10000 * 100, 2)
    result = dict(sorted(result.items()))
    return result
