from random import randint
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    dict_result = Counter(
        [sum([randint(0, 1) for _ in range(10)]) for _ in range(10_000)]
    )
    total = sum(dict_result.values())
    return {
        key: round(value / total * 100, 2)
        for key, value in dict_result.items()
    }


def draw_gaussian_distribution_graph() -> None:
    dict_result = flip_coin()
    dict_result_sorted = {}

    for pos in range(len(dict_result)):
        dict_result_sorted[pos] = dict_result[pos]

    x_point = np.array(list(dict_result_sorted.keys()))
    y_point = np.array(list(dict_result_sorted.values()))

    plt.plot(x_point, y_point)
    plt.show()
