import random
from typing import Dict
import matplotlib.pyplot as plt


def flip_coin(
    trials: int = 10000,
    flips_per_trial: int = 10
) -> Dict[int, float]:
    """
    Simulate 10 coin flips multiple times and return heads distribution.
    """
    results: Dict[int, int] = {i: 0 for i in range(flips_per_trial + 1)}

    for _ in range(trials):
        heads = sum(
            random.choice([0, 1]) for _ in range(flips_per_trial)
        )
        results[heads] += 1

    percentages: Dict[int, float] = {
        k: round(v * 100 / trials, 2)
        for k, v in results.items()
    }
    return percentages


def draw_gaussian_distribution_graph(
    distribution: Dict[int, float]
) -> None:
    """
    Draw a Gaussian-like distribution graph for coin flip results.
    """
    plt.figure(figsize=(8, 5))
    plt.bar(
        distribution.keys(),
        distribution.values(),
        color="skyblue"
    )
    plt.title("Coin Flip Distribution (10 flips per trial)")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


if __name__ == "__main__":
    data = flip_coin()
    print(data)
    draw_gaussian_distribution_graph(data)
