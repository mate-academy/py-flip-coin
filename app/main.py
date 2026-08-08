import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    heads_count = [
        [random.choice(["heads", "tails"]) for _ in range(10)].count("heads")
        for _ in range(10_000)
    ]
    return {
        key: heads_count.count(key) / 100
        for key in range(0, 11)
    }


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    plt.bar(data.keys(), data.values())
    plt.xlabel("Heads count")
    plt.ylabel("Drop Percentage %")
    plt.title("Gaussian distribution")
    plt.xticks(range(0, 11))
    plt.grid(axis="y")
    plt.show()
