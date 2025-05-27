import random
from matplotlib import pyplot
import numpy


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                heads += 1
        results[heads] += 1

        total_cases = sum(results.values())

    for key in results:
        results[key] = (results[key] / total_cases) * 100
    return results


def draw_gaussian_distribution_graph(results: dict) -> None:
    head_numbers = numpy.array(list(results.keys()))
    percentage = numpy.array(list(results.values()))
    pyplot.title("Gaussian distribution", loc="left")
    pyplot.xlabel("Heads count")
    pyplot.ylabel("Drop percentage %")
    pyplot.plot(head_numbers, percentage)
    pyplot.show()
