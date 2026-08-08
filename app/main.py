import random
from matplotlib import pyplot
import numpy


def flip_coin() -> dict:
    values = ["head", "tail"]
    result = {}
    for num in range(0, 10000):
        counter = 0
        for _ in range(0, 10):
            i = random.choice(values)
            if i == "head":
                counter += 1
        if counter not in result:
            result[counter] = 1
        else:
            result[counter] += 1
    for key in result:
        result[key] = round(result[key] / 100, 2)
    result = {key: result[key] for key in sorted(result)}
    print(result)
    return result


def draw_gaussian_distribution_graph(times: int) -> None:
    data = flip_coin()
    xpoints = numpy.array([key for key in data])
    ypoints = numpy.array([value for value in data.values()])
    pyplot.plot(xpoints, ypoints)
    pyplot.show()
