import random

import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    distribution = {}
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            heads += random.randint(0, 1)
        if heads not in distribution:
            distribution[heads] = 1
        else:
            distribution[heads] += 1
    for key in distribution:
        distribution[key] /= 100
    distribution = dict(sorted(distribution.items()))
    return distribution


def draw_gaussian_distribution_graph(distribution: dict) -> None:
    y_points = np.array(list(distribution.values()))
    plt.plot(y_points)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.ylim(0, 100)
    plt.yticks(np.arange(0, 105, step=10))
    plt.minorticks_on()
    plt.xlim(0, 10)
    plt.show()
