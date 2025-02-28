import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result = {i: 0.00 for i in range(11)}
    for _ in range(10000):
        count = 0
        for i in range(10):
            count += random.choice([0, 1])
        result[count] += 1

    # convertion to percentages
    for key, value in result.items():
        result[key] = round((value / 100), 2)
    return result


def draw_gaussian_distribution_graph(result: dict) -> None:
    xpoints = np.array(list(result.keys()))
    ypoints = np.array(list(result.values()))

    plt.plot(xpoints, ypoints)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage, %")
    plt.show()
