import random
from typing import Any

import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    coin_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
                 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    coin_sides = [0, 1]
    for _ in range(10000):
        count = 0
        for _ in range(10):
            side = random.choice(coin_sides)
            if side == 0:
                count += 1
        coin_dict[count] += 1

    for value in coin_dict:
        coin_dict[value] = coin_dict[value] / 10000 * 100

    return coin_dict


def draw_gaussian_distribution_graph(coin_dict: dict) -> Any:
    x_axis = np.array(list(coin_dict.keys()))
    y_axis = np.array(list(coin_dict.values()))
    plt.plot(x_axis, y_axis)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads Count")
    plt.ylabel("Drop percentage %")

    plt.show()
