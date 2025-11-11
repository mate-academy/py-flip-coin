import random
import matplotlib.pyplot as plt
from typing import Dict


def flip_coin(
    trials: int = 10000,
    flips_per_trial: int = 10
) -> Dict[int, float]:
    results: Dict[int, int] = {
        count: 0 for count in range(flips_per_trial + 1)
    }

    for _ in range(trials):
        heads_count = sum(
            random.choice([0, 1]) for _ in range(flips_per_trial)
        )
        results[heads_count] += 1

    percentages: Dict[int, float] = {
        count: round((occurrences / trials) * 100, 2)
        for count, occurrences in results.items()
    }

    return percentages


def draw_gaussian_distribution_graph(
    distribution: Dict[int, float]
) -> None:
    head_counts = list(distribution.keys())
    percentages = list(distribution.values())

    plt.figure(figsize=(10, 6))
    plt.plot(
        head_counts,
        percentages,
        marker="o",
        linestyle="-",
        color="blue"
    )
    plt.title("Distribution of Heads in 10 Coin Flips (10,000 Trials)")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage of Occurrence")
    plt.grid(True)
    plt.xticks(range(11))
    plt.show()
