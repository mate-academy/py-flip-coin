from random import randrange


def flip_coin() -> dict:
    dict1 = {i: 0 for i in range(0, 11)}
    for case in range(10000):
        heads = 0
        for _ in range(10):
            heads += 1 if randrange(2) == 1 else + 0
        dict1[heads] += 1

    for i2 in range(11):
        percent = dict1.get(i2) / 10000 * 100
        rounded_percent = round(percent, 2)
        dict1[i2] = rounded_percent
    return dict1
