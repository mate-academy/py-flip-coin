import random


def flip_coin() -> dict[int, float]:

    result_dict = {i: 0 for i in range(0, 11)}

    for i in range(10000):
        counter = 0
        for _ in range(10):
            if random.choice([0, 1]) == 0:
                counter += 1
        result_dict[counter] += 1

    result_dict = {i: value / 100 for i, value
                   in enumerate(result_dict.values())}

    return result_dict
