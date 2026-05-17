import random
from typing import Callable

import numpy
from matplotlib import pyplot


def flip_coin() -> dict[int, float]:
    result = {
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
        heads_count = 0
        for _ in range(10):
            if random.randint(0, 1) == 0:
                heads_count += 1
        result[heads_count] += 1

    for key, value in result.items():
        result[key] = (value / 10000) * 100

    return result


def draw_gaussian_distribution_graph(flip_coin: Callable) -> None:
    y_points = numpy.array([flip_coin[key] for key in flip_coin.keys()])
    pyplot.xticks(range(11))
    pyplot.yticks(range(0, 101, 10))
    pyplot.ylim(0, 100)
    pyplot.title("Gaussian distribution")
    pyplot.xlabel("Heads count")
    pyplot.ylabel("Drop percentage %")
    pyplot.plot(y_points)
    pyplot.show()
