import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}
    for _ in range(10000):
        current_flip_sum = 0
        for _ in range(10):
            current_flip_sum += random.randint(0, 1)
        results[current_flip_sum] += 1

    for index in range(11):
        results[index] = (results[index] / 10000) * 100
    return results


def draw_gaussian_distribution_graph(statistic: dict) -> None:
    xpoints = np.array(list(statistic.keys()))
    ypoints = np.array(list(statistic.values()))
    plt.plot(xpoints, ypoints, marker="o")
    plt.ylim(0, 100)
    plt.xlabel("Gaussian distribution")
    plt.ylabel("Percentage %")
    plt.show()


draw_gaussian_distribution_graph(flip_coin())
