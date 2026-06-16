import random
import matplotlib.pyplot as pyplot


def flip_coin() -> dict:
    results = []

    for _ in range(10000):
        flips = random.choices(["heads", "tails"], k=10)
        results.append(flips.count("heads"))

    heads_number = {
        i: round(results.count(i) * 100 / len(results), 2)
        for i in range(11)
    }

    return heads_number


def draw_gaussian_distribution_graph() -> None:
    data_for_graph = flip_coin()

    x_axis = list(data_for_graph.keys())
    y_axis = list(data_for_graph.values())

    pyplot.plot(x_axis, y_axis)
    pyplot.xlabel("Heads count")
    pyplot.ylabel("Drop percentage %")
    pyplot.title("Gaussian distribution")

    pyplot.show()
