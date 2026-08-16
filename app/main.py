import random
import matplotlib.pyplot as plt
from collections import defaultdict
from typing import Dict


def flip_coin(
    num_flips: int = 10,
    num_experiments: int = 10000
) -> Dict[int, float]:

    """
    Simulate flipping a coin "num_flips"
    times for "num_experiments" experiments.
    Returns a dictionary where keys
    are the number of heads (0 to num_flips),
    and values are the percentage of experiments
    with that number of heads.
    """

    heads_count = defaultdict(int)

    for _ in range(num_experiments):
        # Simulate flipping a coin "num_flips" times
        heads = sum(
            1 for _ in range(num_flips)
            if random.choice(["heads", "tails"]) == "heads"
        )
        heads_count[heads] += 1

    # Calculate percentages with that number of heads.
    total_experiments = num_experiments
    result = {
        k: (v / total_experiments) * 100
        for k, v in sorted(heads_count.items())
    }
    return result


def draw_gaussian_distribution_graph(distribution: Dict[int, float]) -> None:

    """
    Draw a bar graph of the distribution of heads counts.
    """

    heads = list(distribution.keys())
    percentages = list(distribution.values())

    plt.bar(heads, percentages, color="skyblue")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.title(
        "Gaussian Distribution of Coin Flips (10 flips, 10,000 experiments)"
    )
    plt.xticks(range(0, 11))
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.savefig("gaussian_distribution.png", dpi=300, bbox_inches="tight")
    plt.close()


# Example usage
if __name__ == "__main__":
    distribution = flip_coin()
    print(distribution)
    draw_gaussian_distribution_graph(distribution)
