from random import randint

import numpy
from matplotlib import pyplot


def flip_coin(case_count: int = 10000) -> dict:
    flip_count = [0] * 11
    for _ in range(case_count):
        heads_count = sum(randint(0, 1) for _ in range(10))
        flip_count[heads_count] += 1
    return {
        i: flip_count[i] * 100 / case_count for i in range(len(flip_count))
    }


def draw_gaussian_distribution_graph() -> None:
    flip_count = flip_coin()
    x_points = numpy.arange(0, 11)
    y_points = numpy.array(list(flip_count.values()))
    pyplot.plot(x_points, y_points)
    pyplot.ylim(0, 100)
    pyplot.xticks(numpy.arange(0, 11, 1))
    pyplot.yticks(numpy.arange(0, 101, 10))
    pyplot.title("Gaussian distribution")
    pyplot.xlabel("Heads count")
    pyplot.ylabel("Drop percentage %")
    pyplot.show()
