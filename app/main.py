import random


def flip_coin() -> dict:
    result_dict = {}

    for _ in range(10000):
        heads = sum(random.choice((1, 0)) for _ in range(10))
        if heads not in result_dict:
            result_dict[heads] = 1
        else:
            result_dict[heads] += 1

    return {
        key: value / 100
        for key, value in result_dict.items()
    }
