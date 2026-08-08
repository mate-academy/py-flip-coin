import random


def flip_coin() -> dict:
    coin = ["heads", "tails"]
    all_flips = {}
    for flips in range(0, 10000):
        heads = 0
        for i in range(0, 10):
            flip = random.choice(coin)
            if flip == "heads":
                heads += 1
        all_flips[str(flips)] = heads
    result_dict = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }
    for key, value in all_flips.items():
        result_dict[value] += 1
    for key, value in result_dict.items():
        result_dict[key] = round((value / 10000) * 100, 2)
    return result_dict
