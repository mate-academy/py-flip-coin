import random


def flip_coin() -> dict:
    res_dict = {}
    for _ in range(10000):
        counter = sum(random.randint(0, 1) for _ in range(10))
        if counter in res_dict:
            res_dict[counter] += 1
        else:
            res_dict[counter] = 1
    for key, value in res_dict.items():
        res_dict[key] = value / 100
    return res_dict


print(flip_coin())
