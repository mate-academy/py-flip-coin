import random
from collections import Counter

import matplotlib.pyplot as plt


def flip_coin(num_experiments: int = 10000) -> dict:
    all_results = (
        sum(random.randint(0, 1) for _ in range(10))
        for _ in range(num_experiments)
    )
    counts = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }
    for key, value in Counter(all_results).items():
        counts[key] = round(((value / num_experiments) * 100), 2)

    return counts


def draw_gaussian_distribution_graph(counts: dict) -> None:
    x_values = list(counts.keys())
    y_values = list(counts.values())

    plt.bar(x_values, y_values)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.ylim(0, 100)
    plt.xticks(x_values)
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.show()
