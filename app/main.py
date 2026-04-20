import random


def flip_coin() -> dict:
    init_dict = {0: 0,
                 1: 0,
                 2: 0,
                 3: 0,
                 4: 0,
                 5: 0,
                 6: 0,
                 7: 0,
                 8: 0,
                 9: 0,
                 10: 0}
    coin = ["head", "tail"]
    for _ in range(10000):
        count = 0
        for i in range(10):
            if random.choice(coin) == "head":
                count += 1
        init_dict[count] += 1
    for keys, value in init_dict.items():
        init_dict[keys] = round((value / 10000) * 100, 2)
    return init_dict
