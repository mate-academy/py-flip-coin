import random


def flip_coin() -> dict:
    result_dict = {key: 0 for key in range(11)}
    for i in range(10000):
        counter = 0
        for i in range(10):
            flip = random.randint(0, 1)
            if flip == 1:
                counter += 1
        result_dict[counter] += 1
    for key, value in result_dict.items():
        result_dict[key] = (value / 10000) * 100
    return result_dict
