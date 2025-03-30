import random


def flip_coin():
    chance_dict = {i: 0 for i in range(11)}

    for _ in range(10000):
        flips = {1: 0, 0: 0}
        for i in range(10):
            num = random.randint(0, 1)
            flips[num] += 1
        chance_dict[flips[1]] += 1

    for option in chance_dict:
        chance_dict[option] = int((chance_dict[option] / 10000) * 100)

    return chance_dict
