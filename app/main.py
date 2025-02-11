import random
import numpy
import matplotlib.pyplot


def flip_coin(num_trials: int = 10000, num_flips: int = 10) -> None:
    results = {i: 0 for i in range(num_flips + 1)}

    for _ in range(num_trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(num_flips))
        results[heads_count] += 1

    for key in results:
        results[key] = round((results[key] / num_trials) * 100, 2)
    return results


def draw_gaussian_distribution_graph() -> None:
    matplotlib.use("TkAgg")
    results = flip_coin()
    key_list = list(results.keys())
    values_list = list(results.values())
    x_points = numpy.array(key_list)
    y_points = numpy.array(values_list)
    matplotlib.pyplot.plot(x_points, y_points)
    matplotlib.pyplot.show()
