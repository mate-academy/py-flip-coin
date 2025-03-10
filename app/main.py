import random
import matplotlib.pyplot as plt
from collections import Counter


def flip_coin(trials: int = 10000, flips: int = 10) -> dict:
    results = [
        sum(random.choice([0, 1]) for _ in range(flips))
        for _ in range(trials)
    ]
    counts = Counter(results)
    total_cases = sum(counts.values())
    return {
        k: round(v / total_cases * 100, 2)
        for k, v in sorted(counts.items())
    }


def draw_gaussian_distribution_graph(data: dict) -> None:
    plt.bar(data.keys(), data.values(), color="blue", alpha=0.7)
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.title("Gaussian Distribution of Coin Flips")
    plt.xticks(range(11))
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.show()
