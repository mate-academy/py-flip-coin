import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:

    counts = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                heads += 1
        counts[heads] += 1

    for key in counts:
        counts[key] = round(counts[key] / 10000 * 100, 2)

    return counts


def draw_gaussian_distribution_graph(points: dict) -> None:

    x_points = np.array([key for key in points.keys()])
    y_points = np.array([value for value in points.values()])
    plt.plot(x_points, y_points)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()


draw_gaussian_distribution_graph(flip_coin())
