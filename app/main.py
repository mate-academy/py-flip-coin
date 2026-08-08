import random
import matplotlib.pyplot as plt
from typing import Dict


def flip_coin(num_trials: int = 10_000) -> Dict[int, float]:
    results: Dict[int, int] = {heads: 0 for heads in range(11)}

    for _ in range(num_trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    percentages: Dict[int, float] = {
        heads: round(count * 100 / num_trials, 2)
        for heads, count in results.items()
    }

    return percentages


def draw_gaussian_distribution_graph(distribution: Dict[int, float]) -> None:
    x_values = list(distribution.keys())
    y_values = list(distribution.values())

    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, marker="o", linestyle="-", color="blue")
    plt.title("Gaussian Distribution of 10 Coin Flips")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.grid(True)
    plt.xticks(range(11))
    plt.show()
