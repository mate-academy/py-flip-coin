import random


def flip_coin() -> dict:
    result_dict = {i: 0 for i in range(11)}
    for event in range(10000):
        heads = len([random.choice([0, 1]) for i in range(10)
                     if random.choice([0, 1]) == 1])
        result_dict[heads] += 1
    result_dict = {key: round(result_dict[key] / 10000 * 100, 2)
                   for key in range(11)}
    return result_dict
