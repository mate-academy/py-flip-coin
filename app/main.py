import random
import numpy
import matplotlib.pyplot as plt


def flip_coin(cases: int = 10000, flips: int = 10) -> dict:
    result = {i: 0 for i in range(flips + 1)}

    for case in range(cases):
        heads_count = sum(random.choice([0, 1]) for _ in range(flips))
        result[heads_count] += 1

    percentage_result = {key: round(value / cases * 100, 2)
                         for key, value in result.items()}

    return percentage_result


def gaussian_graph(flip_dict: dict) -> None:
    x_axis = list(flip_dict.keys())
    y_axis = list(flip_dict.values())

    x_points = numpy.array(x_axis)
    y_points = numpy.array(y_axis)

    plt.plot(x_points, y_points)
    plt.xticks(x_points)
    plt.grid()
    plt.show()


gaussian_graph(flip_coin())
