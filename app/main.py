import random


def flip_coin():
    coin_dict = {i: 0 for i in range(11)}
    for j in range(10000):
        count = 0
        for _ in range(10):
            if random.randint(1, 2) == 1:
                count += 1
        coin_dict[count] += 1
    coin_dict = {k: v / 100 for k, v in coin_dict.items()}
    return coin_dict
