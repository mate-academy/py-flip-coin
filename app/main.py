import random
from collections import defaultdict
import matplotlib.pyplot as plt


def flip_coin(trials: int = 10000) -> dict[int, float]:
    """
    Simulates flipping a coin 10 times in each trial.
    Returns a dict with the percentage of each number of heads.
    """
    results = defaultdict(int)

    for _ in range(trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    return {k: round(v / trials * 100, 2) for k, v in sorted(results.items())}


def draw_gaussian_distribution_graph(distribution: dict[int, float]) -> None:
    """
    Draws a Gaussian distribution graph from the distribution of heads.
    """
    count_heads = list(distribution.keys())
    percentage = list(distribution.values())

    plt.figure(figsize=(10, 5))
    plt.plot(count_heads, percentage, marker="o", linestyle="-", color="blue")
    plt.title("Distribution of Heads in 10 Coin Flips (10,000 trials)")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.grid(True)
    plt.xticks(range(11))
    plt.show()
