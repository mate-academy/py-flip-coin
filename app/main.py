import random

from matplotlib import pyplot as plt
import numpy as np


def flip_a_coin_10_times() -> int:
    return sum(random.randint(0, 1) for _ in range(10))


def flip_coin() -> dict:
    statistics = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
                  6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for _ in range(10000):
        statistics[flip_a_coin_10_times()] += 1
    for key, element in statistics.items():
        statistics[key] = round(element / 100, 2)
    return statistics


def draw_gaussian_distribution_graph(statistics: dict) -> None:
    x_axis = np.array(statistics.keys())
    y_axis = np.array(statistics.values())

    plt.plot(x_axis, y_axis)

    plt.title("Gaussian distribution")
    plt.xlabel("Drop percentage %")
    plt.ylabel("Heads count")

    plt.show()
