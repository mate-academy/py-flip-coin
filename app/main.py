import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    count = {i: 0 for i in range(11)}
    for _ in range(10000):
        flips = []
        for _ in range(10):
            flips += [random.randint(0, 1)]
        count[flips.count(1)] += 1
    result = {}
    for key, value in count.items():
        result[key] = round(value / 100, 2)
    return result


experiment = flip_coin()


def draw_gaussian_distribution_graph() -> None:
    x_value = np.array(list(experiment.keys()))
    y_value = np.array(list(experiment.values()))
    plt.plot(x_value, y_value)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.ylim(0, 100)
    plt.show()


draw_gaussian_distribution_graph()
