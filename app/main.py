from typing import Callable

import numpy as np
import matplotlib.pyplot as plt
import random


def flip_coin() -> dict:
    all_series = []
    result_dict = {}
    result_stats = {}
    for _ in range(10000):
        flip_series = {}
        for i in range(10):
            flip_series[i] = random.choice([0, 1])
        all_series.append(flip_series)

    for series in all_series:
        count = sum(1 for heads in series.values() if heads == 1)
        for i in range(11):
            if count == i:
                if i not in result_dict:
                    result_dict[i] = 1
                else:
                    result_dict[i] += 1

    for i in result_dict:
        result_stats[i] = result_dict[i] / 100

    return result_stats


def draw_gaussian_distribution_graph(func: Callable) -> None:
    result = func()
    x_axis = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y_axis = np.array(
        [
            result[0],
            result[1],
            result[2],
            result[3],
            result[4],
            result[5],
            result[6],
            result[7],
            result[8],
            result[9],
            result[10]
        ]
    )
    plt.plot(x_axis, y_axis)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
