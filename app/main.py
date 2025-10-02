import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict[int, float]:
    results = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }

    for _ in range(10000):
        heads = 0

        for _ in range(10):
            if random.randint(0, 1) == 0:
                heads += 1

        results[heads] += 0.01

    return results


def draw_gaussian_distribution_graph() -> None:
    values = flip_coin()
    xpoints = np.array(list(values.keys()))
    ypoints = np.array(list(values.values()))
    plt.plot(xpoints, ypoints)
    plt.show()


draw_gaussian_distribution_graph()
