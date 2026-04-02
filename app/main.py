import random


def flip_coin() -> dict:
    results_dict = {}

    for _ in range(10000):
        coins_flips_list = [random.choice((0, 1)) for _ in range(10)]
        heads_count = coins_flips_list.count(0)

        if heads_count in results_dict:
            results_dict[heads_count] += 1

        else:
            results_dict[heads_count] = 1

    for key, value in results_dict.items():
        results_dict[key] = (value / 10000) * 100

    return results_dict
