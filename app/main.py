import random


def flip_coin() -> dict:
    out_dict = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0
    }
    new_dict = {}
    for _ in range(10000):
        xy = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                xy += 1
        out_dict[xy] += 1

    for key, value in out_dict.items():
        value = value / 10000 * 100
        new_dict[key] = value
    return new_dict
