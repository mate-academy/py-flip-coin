import matplotlib.pyplot as plt
import numpy as np
import random


def flip_coin() -> dict:
    dict_flip_coin = {i: 0 for i in range(11)}
    for _ in range(10000):
        list_one_flip = random.choices([0, 1], k=10)
        dict_flip_coin[sum(list_one_flip)] += 1

    for heads in dict_flip_coin:
        dict_flip_coin[heads] = dict_flip_coin[heads] / 100

    return dict_flip_coin


def draw_gaussian_distribution_graph() -> None:
    dict_flip_coin = flip_coin()

    xpoints = np.array(dict_flip_coin.keys())
    ypoints = np.array(dict_flip_coin.values())

    plt.plot(xpoints, ypoints)
    plt.show()
