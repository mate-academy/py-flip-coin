import random


def flip_coin() -> dict:
    result_dict = {i: 0 for i in range(11)}
    result_ls = []

    for i in range(10000):
        result_flip = 0
        for _ in range(10):
            result_flip += random.randint(0, 1)
        result_ls.append(result_flip)

    for result in result_ls:
        result_dict[result] = round(result_ls.count(result)
                                    / 10000 * 100, 2)
    return result_dict
