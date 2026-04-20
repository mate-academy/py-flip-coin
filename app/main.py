import random


def flip_coin() -> dict:
    dict_ = {}
    for _ in range(10000):
        list_ = []
        for _ in range(10):
            list_.append(random.randint(0, 1))

        heads_num = list_.count(1)
        if heads_num not in dict_:
            dict_[heads_num] = 0
        dict_[heads_num] += 1

    return {
        key: (value / 10000) * 100
        for key, value in dict_.items()
    }
