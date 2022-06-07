import random


def rand():
    result = {i: 0 for i in range(11)}

    for _ in range(10000):
        flips = {1: 0, 0: 0}
        for el in range(10):
            number = random.randint(0, 1)
            flips[number] += 1
        result[flips[1]] += 1

    for el in result:
        result[el] = int((result[el] / 10000) * 100)

    return result
