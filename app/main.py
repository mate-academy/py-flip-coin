import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin(trials: int = 10000, flips: int = 10) -> dict:
    results = {i: 0 for i in range(flips + 1)}

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(flips))
        results[heads] += 1

    for key in results:
        results[key] = results[key] * 100 / trials

    return results


def draw_gaussian_distribution_graph(results: dict) -> None:
    x_point = np.array([key for key in results.keys()])
    y_point = np.array([values for values in results.values()])

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.plot(x_point, y_point)
    plt.show()
