import random


def flip_coin() -> dict:
    coin = ["orel", "reshka"]
    out_dict = {}
    erdo_dict = {count: 0 for count in range(11)}
    for i in range(10000):
        count_orel = 0
        for _ in range(10):
            if random.choice(coin) == "orel":
                count_orel += 1
        if count_orel in erdo_dict:
            erdo_dict[count_orel] += 1

    for key, value in erdo_dict.items():
        out_dict[key] = value / 100
    return out_dict
