import random
import matplotlib.pyplot as plt
from typing import Dict


def flip_coin(trials: int = 10000) -> Dict[int, float]:
    results = {i: 0 for i in range(11)}

    for _ in range(trials):
        heads_count = 0
        for _ in range(10):
            if random.random() < 0.5:
                heads_count += 1
        results[heads_count] += 1

    for heads_count in results:
        results[heads_count] = round((results[heads_count] / trials) * 100, 2)

    return results


def draw_gaussian_distribution_graph(distribution: Dict[int, float]) -> None:
    x_values = list(distribution.keys())
    y_values = list(distribution.values())

    plt.figure(figsize=(10, 5))
    plt.plot(x_values, y_values, marker="o")
    plt.title("Gaussian-like Distribution of Coin Flips (10 flips)")
    plt.xlabel("Number of heads (0–10)")
    plt.ylabel("Percentage (%)")
    plt.grid(True)
    plt.show()
