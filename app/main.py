import random
import matplotlib.pyplot as plt
from typing import Dict


def flip_coin() -> Dict[int, float]:
    """
    Conducts at least 10000 cases of flipping a coin 10 times.
    Returns dict where keys are numbers of possible heads dropped (0 to 10),
    and values are percentage of how many that number of heads
    dropped out of all cases.
    """
    cases = 10000
    results = {i: 0 for i in range(11)}  # 0 to 10 heads possible

    for _ in range(cases):
        heads_count = 0
        for _ in range(10):  # flip coin 10 times per case
            if random.random() < 0.5:  # heads
                heads_count += 1
        results[heads_count] += 1

    # Convert counts to percentages
    for key in results:
        results[key] = round((results[key] / cases) * 100, 2)

    return results


def draw_gaussian_distribution_graph() -> None:
    """
    Draws a graph that shows the distribution from flip_coin function.
    """
    data = flip_coin()
    heads = list(data.keys())
    percentages = list(data.values())

    plt.figure(figsize=(10, 6))
    plt.bar(heads, percentages, color="skyblue", edgecolor="navy", alpha=0.7)
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.title("Gaussian Distribution of Coin Flip Results")
    plt.xticks(heads)
    plt.grid(axis="y", alpha=0.3)

    # Add percentage labels on top of bars
    for i, percentage in enumerate(percentages):
        plt.text(
            i,
            percentage + 0.1,
            f"{percentage}%",
            ha="center",
            va="bottom",
        )

    plt.tight_layout()
    plt.show()
