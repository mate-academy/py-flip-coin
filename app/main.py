from random import randint


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
        10: 0,
    }
    for _ in range(10000):
        number = 0
        for num in range(10):
            if randint(0, 1) == 0:
                number += 1
        result[number] += 1

    for key in result:
        result[key] = round(result[key] / 100, 2)

    return result
