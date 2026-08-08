import random


def flip_coin() -> dict:
    res_dict = {i: 0 for i in range(10 + 1)}

    for i in range(10000):
        head = sum(random.randint(0, 1) for _ in range(10))
        res_dict[head] += 1

    for key, value in res_dict.items():
        res_dict[key] = round(value / 100, 2)

    return res_dict
