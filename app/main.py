import random


def flip_coin() -> dict:
    dict_cases = {i: 0 for i in range(11)}
    for _ in range(10000):
        count_case = sum(random.randint(0, 1) for _ in range(10))
        dict_cases[count_case] += 1
    return {
        key: round((value / 10000) * 100, 2)
        for key, value in dict_cases.items()
    }
