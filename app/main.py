import random

import matplotlib
import matplotlib.pyplot


def flip_coin() -> dict:
    test_times = 10000

    result_of_flips = {i: 0 for i in range(0, 11)}

    for _ in range(0, test_times):
        count = 0

        for _ in range(0, 10):
            count += random.randint(0, 1)

        result_of_flips[count] += 1

    for key in result_of_flips:
        result_of_flips[key] /= test_times / 100

    return result_of_flips


def draw_gaussian_distribution_graph(result_of_flips: dict) -> None:
    dpi = 80
    fig = matplotlib.pyplot.figure(
        dpi=dpi,
        figsize=(512 / dpi, 384 / dpi)
    )
    matplotlib.rcParams.update({"font.size": 10})

    matplotlib.pyplot.axis([0, 10, 0, 100])

    matplotlib.pyplot.title("Gaussian distribution")
    matplotlib.pyplot.xlabel("Heads count")
    matplotlib.pyplot.ylabel("Drop perceptron %")

    matplotlib.pyplot.plot(
        result_of_flips.keys(),
        result_of_flips.values(),
        color="blue",
        linestyle="solid"
    )

    fig.savefig("trigan.png")
