import matplotlib.pyplot as plt

import random

import numpy as np


sides_of_coins = ["heads", "tails"]
total = 10000


def flip_coin(trials: int = 10000, flips: int = 10) -> dict[int, float]:

    results = {i: 0 for i in range(flips + 1)}

    for _ in range(trials):
        heads_count = sum(
            1 for _ in range(flips)
            if random.choice(["heads", "tails"]) == "heads")
        results[heads_count] += 1

    for key in results:
        results[key] = round(results[key] / trials * 100, 2)

    return results


def draw_gaussian_distribution_graph() -> None:
    results = flip_coin()
    x_points = np.array(list(results.keys()))
    y_points = np.array(list(results.values()))
    plt.bar(x_points, y_points, alpha=0.6, label="Simulation")
    plt.plot(x_points, y_points,
             color="red",
             marker="o",
             label="Gaussian Approximation")
    plt.xlabel("Number of Heads in 10 Flips")
    plt.ylabel("Percentage (%)")
    plt.title("Coin Flip Distribution vs Gaussian Approximation")
    plt.legend()
    plt.show()


print(flip_coin())
draw_gaussian_distribution_graph()
