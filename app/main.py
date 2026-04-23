import random


def flip_coin() -> dict:
    heads_all = []
    coin_sides = ["heads", "tails"]
    for number in range(10000):
        heads_in_range_10 = 0
        for num in range(10):
            side = random.choice(coin_sides)
            if side == "heads":
                heads_in_range_10 += 1
        heads_all.append(heads_in_range_10)

    result_dict = {}
    for chance in heads_all:
        result_dict[chance] = result_dict.get(chance, 0) + 1

    for key, value in result_dict.items():
        result_dict[key] = (value / 10000) * 100

    return result_dict
