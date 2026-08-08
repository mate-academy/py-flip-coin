import random

import matplotlib.pyplot as plt
import numpy as np


def flip_coin(flips: int = 10000) -> dict:
    result = {i: 0 for i in range(11)}

    for _ in range(flips):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        result.update({heads: result[heads] + 1})

    for heads in result:
        percent = round((result[heads] / flips) * 100, 2)
        result.update({heads: percent})

    return result


def draw_gaussian_distribution_graph(coin_flips: dict) -> None:
    xpoints = np.array([key for key in coin_flips])
    ypoints = np.array([coin_flips[key] for key in coin_flips])

    plt.plot(xpoints, ypoints)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
