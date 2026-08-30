import random


def flip_coin() -> dict:
    result_dict = {n: 0 for n in range(11)}
    for _ in range(10000):
        heads_count = 0
        for _ in range(10):
            heads_count += random.randint(0, 1)
        result_dict[heads_count] += 1
    for key, value in result_dict.items():
        result_dict[key] = round(value / 10000 * 100, 2)
    return result_dict
