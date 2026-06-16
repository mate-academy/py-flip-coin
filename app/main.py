import random
import numpy
from matplotlib import pyplot


def flip_coin() -> dict:
    statistics = {amount_head: 0 for amount_head in range(11)}
    for _ in range(10000):
        round_result = 0
        for _ in range(10):
            current_result = random.randint(0, 1)
            round_result += current_result
        statistics[round_result] += 1

    percentage_statistics = {
        amount_head: frequency / 100
        for amount_head, frequency in statistics.items()
    }

    return percentage_statistics


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    xpoints = numpy.array(list(data.keys()))
    ypoints = numpy.array(list(data.values()))

    pyplot.xlim(0, 10)
    pyplot.ylim(0, 100)

    pyplot.title("Gaussian distribution")
    pyplot.xlabel("Heads count")
    pyplot.ylabel("Drop percentage %")

    pyplot.plot(xpoints, ypoints)
    pyplot.show()
