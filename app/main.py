import random
import matplotlib.pyplot as plt
from typing import Dict


def flip_coin(
    num_trials: int = 10000,
    flips_per_trial: int = 10
) -> Dict[int, float]:
    counts = {count: 0 for count in range(flips_per_trial + 1)}

    for _ in range(num_trials):
        heads_count = sum(
            random.choice([0, 1]) for _ in range(flips_per_trial)
        )
        counts[heads_count] += 1

    percentages = {
        count: round(value / num_trials * 100, 2)
        for count, value in counts.items()
    }
    return percentages


def draw_gaussian_distribution_graph(
    distribution: Dict[int, float]
) -> None:
    heads_counts = list(distribution.keys())
    percentages = list(distribution.values())

    plt.bar(heads_counts, percentages, color="skyblue")
    plt.xlabel("Number of Heads in 10 Flips")
    plt.ylabel("Percentage (%)")
    plt.title("Distribution of Heads Count in 10 Coin Flips")
    plt.xticks(heads_counts)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


distribution = flip_coin()
print(distribution)
draw_gaussian_distribution_graph(distribution)
