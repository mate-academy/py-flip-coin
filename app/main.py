import random


def flip_coin():
    side = ("heads", "tails")
    keys = [i for i in range(11)]
    heads_dict = dict.fromkeys(keys, 0)
    for _ in range(10000):
        heads = 0
        for i in range(10):
            if random.choice(side) == "heads":
                heads += 1
        heads_dict[heads] += 1
    for key in heads_dict:
        heads_dict[key] = heads_dict[key] / 100
    return heads_dict
