import random

import numpy as np
from matplotlib import pyplot as plt


def flip_coin() -> dict:
    result = {key: 0 for key in range(11)}
    for _ in range(10000):
        heads = [random.randint(0, 1) for _ in range(10)]
        result[heads.count(1)] += 1
    return {
        key: round((value / 10000) * 100, 2) for key, value in result.items()
    }


def draw_gaussian_distribution_graph() -> None:
    head_dict = flip_coin()

    xpoints = np.array(list(range(11)))
    ypoints = np.array([head_dict[i] for i in range(11)])

    plt.plot(xpoints, ypoints)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.show()
