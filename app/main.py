import numpy as np
import matplotlib.pyplot as plt


def flip_coin(num_flips: int = 10, num_cases: int = 10000) -> dict:
    results = np.random.choice([0, 1], size=(num_cases, num_flips)).sum(axis=1)

    distribution = {
        key: (np.sum(results == key) / num_cases) * 100
        for key in range(num_flips + 1)
    }
    return distribution


def draw_gaussian_distribution_graph(distribution: dict) -> None:
    x_values = list(distribution.keys())
    y_values = list(distribution.values())

    plt.bar(x_values, y_values)
    plt.show()
