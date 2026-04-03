import random
import matplotlib.pyplot as plt
from typing import Dict


def flip_coin() -> Dict[int, float]:
    """Simulate 10000 cases of 10 coin flips and return percentage of heads."""
    results: Dict[int, int] = {i: 0 for i in range(11)}
    trials = 10000

    for _ in range(trials):
        heads_count = 0

        for _ in range(10):
            if random.choice(["head", "tail"]) == "head":
                heads_count += 1

        results[heads_count] += 1

    # Convert counts to percentage
    results_percentage: Dict[int, float] = {
        k: round(v / trials * 100, 2) for k, v in results.items()
    }

    return results_percentage


def draw_gaussian_distribution_graph(results: Dict[int, float]) -> None:
    """Draw bar graph of the distribution of heads in 10 coin flips."""
    num_heads = sorted(results.keys())
    percentages = [results[k] for k in num_heads]

    plt.figure(figsize=(8, 5))
    plt.bar(num_heads, percentages, color="#3b82f6", edgecolor="black")
    plt.xticks(num_heads)
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage (%)")
    plt.title("Distribution of heads in 10 coin flips")
    plt.grid(axis="y", linestyle="--", alpha=0.6)

    for n_heads, pct in zip(num_heads, percentages):
        plt.text(
            n_heads,
            pct + 0.3,
            f"{pct:.2f}%",
            ha="center",
            va="bottom",
            fontsize=8,
        )

    plt.tight_layout()
    plt.savefig("distribution.png")


if __name__ == "__main__":
    res = flip_coin()
    draw_gaussian_distribution_graph(res)
