import random
from typing import Dict
import matplotlib.pyplot as plt


def flip_coin() -> Dict[int, float]:
    trials = 10000
    heads_counts = {i: 0 for i in range(11)}

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        heads_counts[heads] += 1

    return {
        heads: round((count / trials) * 100, 2)
        for heads, count in heads_counts.items()
    }


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()
    x_values = list(distribution.keys())
    y_values = list(distribution.values())

    plt.plot(x_values, y_values)
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage")
    plt.title("Gaussian Distribution")
    plt.show()
