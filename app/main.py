import random
from collections import Counter
from typing import Dict, List
import matplotlib.pyplot as plt


def flip_coin(
    num_experiments: int = 10000,
    flips_per_experiment: int = 10,
) -> Dict[int, float]:
    """
    Simulate coin flips and calculate distribution of heads.

    Args:
        num_experiments: Number of experiments to run.
        flips_per_experiment: Number of coin flips per experiment.

    Returns:
        Dict[int, float]: Keys are numbers of heads (0–10), values are
        percentages of occurrence rounded to two decimals.
    """
    results: List[int] = []

    for _ in range(num_experiments):
        heads_count = sum(
            random.choice([0, 1]) for _ in range(flips_per_experiment)
        )
        results.append(heads_count)

    counts = Counter(results)
    distribution = {
        i: round((counts[i] / num_experiments) * 100, 2)
        for i in range(flips_per_experiment + 1)
    }
    return distribution


def draw_gaussian_distribution_graph(
    distribution: Dict[int, float],
    save_path: str | None = None,
) -> None:
    """
    Draw a Gaussian-like distribution graph for coin flips.

    Args:
        distribution Dict with number of heads as keys and percentage as values
        save_path: Optional path to save the figure (e.g., 'dist.png').
    """
    heads_values = list(distribution.keys())
    percentage_values = list(distribution.values())

    plt.figure(figsize=(8, 5))
    plt.plot(heads_values, percentage_values, marker="o", linestyle="-")
    plt.title("Coin Flip Distribution (10 flips)")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.grid(True)

    if save_path:
        plt.savefig(save_path, bbox_inches="tight")

    plt.show()


if __name__ == "__main__":
    # Run a demo when executed as a script
    dist = flip_coin()
    draw_gaussian_distribution_graph(dist, save_path="distribution.png")
