import random


def flip_coin() -> dict:
    dicto = {
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
        heads = 0
        for _ in range(10):
            heads += random.randint(0, 1)

        dicto[heads] += 1

    for el in dicto:
        dicto[el] /= 100

    return dicto
