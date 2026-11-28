import random


def flip_coin() -> dict[int, float]:
    dict_of_cases = {}
    for _ in range(10000):
        ex = 0
        for _ in range(10):
            ex += random.randint(0, 1)
        if ex in dict_of_cases:
            dict_of_cases[ex] += 1
        else:
            dict_of_cases[ex] = 1

    for key, value in dict_of_cases.items():
        dict_of_cases[key] = round(((value / 10000) * 100), 2)

    return dict_of_cases
