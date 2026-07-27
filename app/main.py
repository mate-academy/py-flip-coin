import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    landing_on_heads = {}

    for _ in range(10000):
        eagle = 0

        for _ in range(10):
            if random.randint(0, 1) == 1:
                eagle += 1

        if eagle in landing_on_heads:
            landing_on_heads[eagle] += 1
        else:
            landing_on_heads[eagle] = 1

    for key in landing_on_heads:
        landing_on_heads[key] = round(landing_on_heads[key] / 10000 * 100, 2)

    return landing_on_heads


def draw_gaussian_distribution_graph() -> None:
    plt.ylim(0, 100)
    plt.xlim(0, 10)

    plt.xticks(range(0, 11, 1))
    plt.yticks(range(0, 101, 10))

    x_points = np.array([0, 1, 2, 4, 5, 6, 8, 9, 10])
    y_points = np.array([0, 2, 5, 20, 25, 20, 5, 2, 0])

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.plot(x_points, y_points)

    plt.show()
