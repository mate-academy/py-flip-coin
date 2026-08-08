import random


def flip_coin(cases: int = 10000) -> dict:
    dict_of_flips = {}

    for flip in range(10000):
        counts = sum(random.choices([0, 1], k=10))
        dict_of_flips[counts] = dict_of_flips.get(counts, 0) + 1

    for flip in dict_of_flips:
        dict_of_flips[flip] = round((dict_of_flips[flip] / cases) * 100, 2)

    return dict_of_flips
