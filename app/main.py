import random
from typing import Any

import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    flip_coin_attempts = []
    result = {}
    for _ in range(10000):
        eagle_side = 0
        for _ in range(10):
            if random.randint(1, 2) == 1:
                eagle_side += 1
        flip_coin_attempts.append(eagle_side)

    for i in range(0, 11):
        percentage = (flip_coin_attempts.count(i) / 10000) * 100
        result[i] = percentage

    return result


def draw_gaussian_distribution_graph() -> Any:
    x_coord = np.array(list(flip_coin().keys()))
    y_coord = np.array(list(flip_coin().values()))

    plt.ylim(0, 100)
    plt.yticks(range(0, 101, 10))

    plt.xlim(0, 10)
    plt.xticks(range(0, 11, 1))

    plt.plot(x_coord, y_coord, marker = "o")

    plt.title("Gaussian distribution")
    plt.xlabel("Heads counts")
    plt.ylabel("Drop percentage %")

    plt.show()

draw_gaussian_distribution_graph()