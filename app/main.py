import random
import numpy
from matplotlib import pyplot


def flip_coin() -> dict:
    result = {key: 0 for key in range(11)}
    temp = []
    for attempt in range(10000):
        temp_result = []
        for side in range(10):
            coin = random.choice(["head", "tail"])
            temp_result.append(coin)
        temp.append(temp_result)
    for sides in temp:
        result[sides.count("head")] += 1
    for value in result:
        result[value] /= 100
    return result


def draw_gaussian_distribution_graph() -> None:
    xpoints = numpy.array(list(flip_coin().keys()))
    ypoints = numpy.array(list(flip_coin().values()))

    pyplot.plot(xpoints, ypoints)

    pyplot.title("Gaussian distribution")
    pyplot.xlabel("Head count")
    pyplot.ylabel("Drop percentage %")

    pyplot.show()
