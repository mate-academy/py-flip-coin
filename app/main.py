import random

import numpy as np
from matplotlib import pyplot as plt

flip_coin_times = 10
cases_of_flipping = 10000


def flip_coin() -> dict[int, float]:
    result = {}
    num_heads_list = []

    for one in range(cases_of_flipping):
        num_heads = sum(
            1
            for _ in range(flip_coin_times)
            if random.choice([1, 0])
        )
        num_heads_list.append(num_heads)
    for i in range(flip_coin_times + 1):
        result[i] = num_heads_list.count(i) / 100

    return result


def draw_gaussian_distribution_graph() -> None:
    x_list, y_list = [], []
    dict_coin = flip_coin()

    for key, value in dict_coin.items():
        x_list.append(key)
        y_list.append(value)

    x_points = np.array(x_list)
    y_points = np.array(y_list)

    plt.ylim(0, 100)
    plt.xlim(0, 10)
    plt.plot(x_points, y_points)
    plt.show()
