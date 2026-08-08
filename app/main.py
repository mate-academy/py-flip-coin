import random


def flip_coin() -> dict:
    res_dict = {}

    for _ in range(10000):
        heads_count = 0

        for _ in range(10):
            if random.randint(0, 1) == 1:
                heads_count += 1

        res_dict[heads_count] = res_dict.get(heads_count, 0) + 1

    for key in res_dict:
        res_dict[key] = round(res_dict[key] / 10000 * 100, 2)

    return res_dict
