from random import randint


def flip_coin() -> dict:
    dict_ = {k: 0 for k in range(11)}
    for _ in range(10000):
        heads_count = 0
        for i in range(10):
            heads = randint(0, 1)
            if heads:
                heads_count += 1
        dict_[heads_count] += 1
    for key, value in dict_.items():
        dict_[key] = value / 100
    return dict_
