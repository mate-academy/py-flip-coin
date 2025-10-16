import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    results = {}
    for _ in range(10000):
        temp_results = []
        for time in range(10):
            result = random.choice(["head", "tail"])
            temp_results.append(result)
        value = temp_results.count("head")
        if not results.get(value):
            results[value] = 1
        else:
            results[value] += 1
    for key, value in results.items():
        results[key] = round(value * 100 / 10000, 2)
    return results


def draw_gaussian_distribution_graph() -> None:
    results = flip_coin()
    sorted_results = dict(sorted(results.items()))
    x_values = np.array(list(sorted_results.keys()))
    y_values = np.array(list(sorted_results.values()))

    plt.plot(x_values, y_values)
    plt.plot(grid=True)
    plt.show()
