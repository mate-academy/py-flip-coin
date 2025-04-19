import random

from matplotlib import pyplot

import numpy as np


def flip_coin() -> dict[int: float]:
    heads_count = dict()
    for iteration in range(10000):
        count = 0
        for current_try in range(10):
            count += random.randint(0, 1)
        heads = heads_count.get(count, 0)
        heads_count.update({count: heads + 1})
    return {key: heads_count[key] / 100 for key in sorted(heads_count.keys())}


def draw_gaussian_distribution_graph(dictionary: dict[int: float]) -> None:
    x_points = np.array(list(dictionary.keys()))
    y_points = np.array(list(dictionary.values()))

    pyplot.plot(x_points, y_points)
    pyplot.title("Gaussian distribution")
    pyplot.xlabel("Heads count")
    pyplot.ylabel("Drop percentage %")

    pyplot.show()
