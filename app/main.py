import random
import matplotlib
import numpy


def flip_coin() -> dict:
    chance_dict = {}

    list_of_ten_flips = [sum([random.randint(0, 1)
                              for flips in range(10)])
                         for case in range(10000)]

    for i in range(0, 11):
        chance_dict[i] = round(
            ((list_of_ten_flips.count(i) / len(list_of_ten_flips)) * 100),
            2)

    return chance_dict


def draw_gaussian_distribution_graph(chance_dict: dict) -> None:
    x_points = numpy.array([key for key in chance_dict.keys()])
    y_points = numpy.array([value for value in chance_dict.values()])

    matplotlib.pyplot.plot(x_points, y_points)
    matplotlib.pyplot.show()
