from random import choice

import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    sides = ["tails", "heads"]
    flip_result = {}

    for i in range(0, 11):
        flip_result[i] = 0

    for case in range(0, 10_000):
        count = 0
        for flip in range(1, 11):
            side = choice(sides)

            if side == "heads":
                count += 1

        flip_result[count] += 1

    return {
        key: round((value / 10_000) * 100, 2)
        for key, value in flip_result.items()
    }


def draw_gaussian_distribution_graph() -> None:
    coins = flip_coin()

    x_points = np.array(list(coins.keys()))
    y_points = np.array(list(coins.values()))

    plt.xlim(0, 10)
    plt.ylim(0, 100)

    plt.xticks(range(0, 11))
    plt.yticks(range(0, 101, 10))

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.plot(x_points, y_points)
    plt.show()
