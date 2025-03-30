import random


def flip_coin() -> dict:
    result = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }

    for _ in range(10000):
        count = 0
        for _ in range(10):
            count += random.choice((0, 1))

        result[count] += 1

    for key in result.keys():
        result[key] /= 100

    print(result)
    return result
