import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result = {i: 0.0 for i in range(11)}

    heads_or_tail = ("head", "tail")
    trials = 10000
    for _ in range(trials):
        heads_count = 0
        for _ in range(10):
            if random.choice(heads_or_tail) == "head":
                heads_count += 1
        result[heads_count] += 1

    for key in result:
        result[key] = (result[key] * 100) / trials

    return result


def write_gaussian_distribution_graph() -> None:
    y_points = np.array(list(flip_coin().values()))
    x_points = np.array(list(flip_coin().keys()))
    plt.plot(x_points, y_points)
    plt.ylim(0, 100)

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage%")
    plt.title("Gaussian distribution")

    plt.show()


write_gaussian_distribution_graph()
