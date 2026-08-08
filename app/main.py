import random


def flip_coin() -> dict:
    coin_dict = dict.fromkeys(range(11))
    heads_count = [sum(random.choices([0, 1], k=10))
                   for item in range(10000)]
    for key in coin_dict.keys():
        coin_dict[key] = round(len([item for item in
                                    heads_count if item == key]) / 100, 2)
    return coin_dict
