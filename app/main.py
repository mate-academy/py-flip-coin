from matplotlib import pyplot
from random import randint


def flip_coin(cases_count: int = 10000) -> dict:
    heads_number_count = [0] * 11
    for _ in range(cases_count):
        count = sum(randint(0, 1) for _ in range(10))
        heads_number_count[count] += 1

    return {
        i: heads_number_count[i] * 100 / cases_count
        for i in range(11)
    }


def draw_gaussian_distribution_graph(flip_result: dict) -> None:
    y_points = flip_result.values()
    pyplot.plot(y_points)
    pyplot.xticks(range(0, 11, 1))
    pyplot.yticks(range(0, 101, 10))
    pyplot.title("Gaussian distribution")
    pyplot.xlabel("Heads count")
    pyplot.ylabel("Drop percentage %")
    pyplot.show()
