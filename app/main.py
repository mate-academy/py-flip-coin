import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin(runs: int = 10000, flips: int = 10) -> dict:
    result = {key: 0 for key in range(flips + 1)}

    for _ in range(runs):
        count = sum(random.getrandbits(1) for _ in range(flips))
        result[count] += 1

    return {key: round(value / runs * 100, 2) for key, value in result.items()}


def draw_gaussian_distribution_graph(flips: dict) -> None:
    x_axis = np.array(range(len(flips)))
    y_axis = np.array(list(flips.values()))

    plt.plot(x_axis, y_axis)

    plt.title("Gaussian Distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.xlim(0, len(flips) - 1)
    plt.ylim(0, 100)

    plt.xticks(range(0, len(flips)))
    plt.yticks(range(0, 101, 10))

    plt.show()
