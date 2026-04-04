import random

import numpy as np
from matplotlib import pyplot as plt


def flip_coin() -> dict:
    coins = ["orel", "reshka"]
    dict_ = {
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
    for _ in range(10001):
        counter = 0
        for i in range(10):
            coin = random.choice(coins)
            if coin == "orel":
                counter += 1
        dict_[counter] += 1
    for i in range(11):
        dict_[i] = dict_[i] / 100
    return dict_


def draw_gaussian_distribution_graph() -> None:
    dict_ = flip_coin()
    xcord = np.array(list(dict_.keys()))
    ycord = np.array(list(dict_.values()))
    plt.plot(xcord, ycord)
    plt.show()
