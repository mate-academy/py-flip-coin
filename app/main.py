import random


def flip_coin() -> dict:
    result_dict = {i: 0 for i in range(11)}

    for coin in range(10000):
        heads_counter = sum(random.choice([0, 1]) for coin in range(10))
        result_dict[heads_counter] += 1

    for key in result_dict:
        result_dict[key] = round((result_dict[key] / 10000) * 100, 2)

    return result_dict


print(flip_coin())
