import random


def flip_coin() -> dict:
    res_dict = {i: 0 for i in range(11)}

    for _ in range(10000):
        key = sum([random.randint(0, 1) for _ in range(0, 10)])
        res_dict[key] += 1

    for key in res_dict:
        res_dict[key] = (res_dict[key] / 10000) * 100

    print(res_dict)
    return res_dict
