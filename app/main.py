import random


def flip_coin() -> dict:
    slownik = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0,
               5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for experiment in range(10000):
        count = 0
        for flip in range(10):
            if random.choice([0, 1]) == 0:
                count += 1
        slownik[count] += 1
    for key, value in slownik.items():
        slownik[key] = value / 10000 * 100
    return slownik


print(flip_coin())
