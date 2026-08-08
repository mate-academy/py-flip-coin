from typing import Callable

import numpy
from matplotlib import pyplot as plt

from app.experiment import Experiment


def flip_coin(cases: int = 10000) -> dict:
    return {
        heads: round(times * 100 / cases, 2)
        for heads, times in Experiment.do_flips(cases).items()
    }


def draw_gaussian_distribution_graph(
        experiments: Callable[[int], dict],
        cases: int = 10000
) -> None:
    results = experiments(cases)
    x_points = numpy.array(list(results.keys()))
    y_points = numpy.array(list(results.values()))

    plt.plot(x_points, y_points)

    plt.title("Gaussian Distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()


if __name__ == "__main__":
    draw_gaussian_distribution_graph(flip_coin)
