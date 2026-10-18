import random
import numpy
from matplotlib import pyplot


def flip_coin() -> dict:
    result = {}

    for flips in range(10000):
        ten_flips = 0
        for _ in range(10):
            ten_flips += random.choice([0, 1])
        result[ten_flips] = result.get(ten_flips, 0) + 1

    return {k: result[k] / 100 for k in sorted(result)}


def draw_gaussian_distribution_graph(flips: dict) -> None:
    x_array = numpy.array(list(flips.keys()))
    y_array = numpy.array(list(flips.values()))

    pyplot.plot(x_array, y_array)
    pyplot.xlabel("Heads count")
    pyplot.ylabel("Drop percentage %")
    pyplot.title("Gaussian distribution")
    pyplot.ylim(0, 100)
    pyplot.show()
