import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin(times: int = 10000) -> dict:

    result = {}
    for key in range(11):
        result[key] = 0

    for _ in range(times):
        heads = 0
        for _ in range(10):
            random_choice = random.choice(["H", "T"])
            if random_choice == "H":
                heads += 1
        result[heads] += 1

    for key, value in result.items():
        result[key] = (value / times) * 100

    return result


def draw_gaussian_distribution_graph() -> None:

    result = flip_coin(10000)

    x_points = []
    y_points = []

    for key, value in result.items():
        x_points.append(key)
        y_points.append(value)

    x_points = np.array(x_points)
    y_points = np.array(y_points)

    plt.plot(x_points, y_points)
    plt.show()
