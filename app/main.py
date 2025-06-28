import random

import numpy
from matplotlib import pyplot


def flip_coin() -> dict:
    result_dict = \
        {0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0,
         6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0, 10: 0.0}
    coin_side = ["Heads", "Tails"]
    for _ in range(10001):
        heads_count = 0
        for _ in range(10):
            if random.choice(coin_side) == "Heads":
                heads_count += 1
        result_dict[heads_count] += 1

    for key in result_dict:
        result_dict[key] = round(result_dict[key] / 10001 * 100, 2)

    return result_dict


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
