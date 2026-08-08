import matplotlib.pyplot as plt
import numpy as np

import random


def flip_coin() -> dict:
    cases = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for _ in range(10000):
        coin_number = [random.randint(0, 1) for _ in range(10)].count(1)

        cases[coin_number] += 1

    for key in cases:
        cases[key] /= 100

    return cases


def draw_gaussian_distribution_graph(values: dict) -> None:
    ypoints = np.array(list(values.values()))

    plt.plot(ypoints)
    plt.show()


draw_gaussian_distribution_graph(flip_coin())
