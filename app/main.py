import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result = {key: 0.0 for key in range(11)}
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            heads += random.choice([0, 1])
        result[heads] += 1
    #  turn numbers to %
    for key in result:
        result[key] = round(result[key] / 10000 * 100, 2)
    return result


def draw_gaussian_distribution_graph(points_dict: dict) -> None:
    y_points = np.array([val for val in points_dict.values()])
    x_points = np.array([key for key in points_dict.keys()])
    plt.plot(x_points, y_points)

    #  add text
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.grid(axis="y")
    plt.ylim(0, 100)
    plt.show()
