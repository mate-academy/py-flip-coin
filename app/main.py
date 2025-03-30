import random


def flip_coin() -> dict:
    itterations = 10000
    result = {i: 0 for i in range(11)}

    for i in range(10000):
        count = sum(random.choice([0, 1]) for i in range(10))
        result[count] += 1

    for key in result:
        result[key] = (result[key] / itterations) * 100

    return result
