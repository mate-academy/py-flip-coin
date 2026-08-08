import random


def flip_coin() -> dict:
    result_flip = {i: 0 for i in range(11)}

    for i in range(10000):
        sum_orel = sum(random.choice([0, 1]) for _ in range(10))
        result_flip[sum_orel] += 1

    for key in result_flip:
        result_flip[key] = round((result_flip[key] / 10000) * 100, 2)

    return result_flip
