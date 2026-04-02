import random
from typing import Dict
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {}
    for _ in range(10000):
        count = 0
        for _ in range(10):
            if random.randint(0, 1) == 0:
                count += 1
        result[count] = result.get(count, 0) + 1
    for key, value in result.items():
        result[key] = round(value / 100, 2)
    return dict(sorted(result.items()))


def draw_gaussian_distribution_graph(data: Dict[int, float]) -> None:
    x_values = list(data.keys())
    y_values = list(data.values())
    plt.figure(figsize=(10, 6))
    plt.plot(
        x_values, y_values, marker="o", linestyle="-",
        color="royalblue", linewidth=2
    )
    plt.title("Gaussian Distribution", fontsize=14)
    plt.xlabel("Heads count", fontsize=12)
    plt.ylabel("Percentage", fontsize=12)
    plt.xticks(range(11))
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()
