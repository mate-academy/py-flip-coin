import matplotlib.pyplot as plt
import numpy as np
from random import randint


def flip_coin() -> dict:
    distribution = {k: 0 for k in range(11)}
    for _ in range(10000):
        heads_count = 0
        for _ in range(10):
            if randint(0, 1) == 0:
                heads_count += 1
        distribution[heads_count] += 1

    for key in distribution:
        distribution[key] /= 100

    return distribution


def draw_gaussian_distribution_graph() -> None:
    dict_flip_coin = flip_coin()

    xpoints = np.array(dict_flip_coin.keys())
    ypoints = np.array(dict_flip_coin.values())

    plt.plot(xpoints, ypoints)
    plt.show()
