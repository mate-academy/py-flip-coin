import random


def flip_coin(num_trials: int = 10000) -> list:
    res_dict = {i: 0 for i in range(11)}

    for i in range(num_trials):
        flips = [random.choice([0, 1]) for _ in range(10)]
        heads = sum(flips)
        res_dict[heads] += 1

    for key, value in res_dict.items():
        res_dict[key] = value / num_trials * 100

    return res_dict
