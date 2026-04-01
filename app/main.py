from random import random


def flip_coin() -> dict:
    work_dict = {
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
        10: 0
    }
    for i_thousand in range(9999):
        side_coin_decade = 0
        for j_decades in range(10):
            side_coin = 0
            if random() >= 0.5:
                side_coin = 1
            side_coin_decade += side_coin
        work_dict[side_coin_decade] += 1
    result_dict = {}
    for work in work_dict:
        result_dict[work] = round(work_dict[work] / 100, 2)

    return result_dict
