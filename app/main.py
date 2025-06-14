import matplotlib.pyplot as plt
import random
from typing import Dict


def flip_coin(num_trials: int = 10000) -> Dict[int, float]:
    results: Dict[int, float] = {i: 0 for i in range(11)}

    for _ in range(num_trials):
        heads_count = sum(random.randint(0, 1) for _ in range(10))
        results[heads_count] += 1

    for heads_count in results:
        results[heads_count] = round(
            (results[heads_count] / num_trials) * 100, 2
        )

    return results


def draw_gaussian_distribution_graph(data: Dict[int, float]) -> None:
    x_values = list(data.keys())
    y_values = list(data.values())

    plt.figure(figsize=(10, 5))
    plt.bar(x_values, y_values, color="skyblue", edgecolor="black")

    plt.title("Gaussian Distribution of Heads in 10 Coin Flips")
    plt.xlabel("Number of Heads in 10 Flips")
    plt.ylabel("Percentage (%)")
    plt.xticks(x_values)

    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()
