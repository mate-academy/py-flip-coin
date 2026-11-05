import random


def flip_coin() -> dict:
    dicts = {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0,
             6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0, 10: 0.0}
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                heads += 1
        dicts[heads] += 1
    for key in dicts:
        dicts[key] = round(dicts[key] / 100, 2)

    return dicts
