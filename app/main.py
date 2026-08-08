import random


def flip_coin() -> dict:
    result_dict = {
        key: 0
        for key in range(11)
    }
    for _ in range(10000):
        chance = sum(1 for _ in range(10) if random.randint(0, 1) == 1)
        result_dict[chance] += 1
    return {
        key: value / 100
        for key, value in result_dict.items()
    }
