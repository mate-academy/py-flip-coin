import random
from collections import defaultdict
import matplotlib.pyplot as plt


def flip_coin(cases: int = 10000, num_flips: int = 10) -> dict:
    results = defaultdict(int)
    for _ in range(cases):
        heads = sum(random.randint(0, 1) for _ in range(num_flips))
        results[heads] += 1

    percentages = {k: (v / cases) * 100 for k, v in results.items()}
    return dict(sorted(percentages.items()))


def draw_gaussian_distribution_graph(results: dict) -> None:
    heads = list(results.keys())
    percentages = list(results.values())

    plt.figure(figsize=(10, 6))
    plt.bar(heads, percentages, color="skyblue")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage of Cases (%)")
    plt.title("Distribution of Heads in 10 Coin Flips")
    plt.xticks(heads)
    plt.grid(axis="y", linestyle="--")
    plt.tight_layout()
    plt.show()
