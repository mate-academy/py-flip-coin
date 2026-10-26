import random


def flip_coin() -> dict:
    experiments = 10000
    flips = 10
    result_dict = {n: 0 for n in range(11)}
    for _ in range(experiments):
        heads = 0
        for _ in range(flips):
            if random.randint(0, 1) == 1:
                heads += 1
        result_dict[heads] += 1
    for key, value in result_dict.items():
        result_dict[key] = value / 100
    return result_dict
