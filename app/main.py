import random


def flip_coin() -> dict:
    result_dict = {i: 0 for i in range(0, 11)}
    attempts = 10000
    for _ in range(attempts):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        result_dict[heads_count] += 1
    for key in result_dict:
        result_dict[key] = round((result_dict[key] / attempts) * 100, 2)

    return result_dict
