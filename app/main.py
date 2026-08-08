import random
from collections import defaultdict
import matplotlib.pyplot as plt


def flip_coin(num_cases: int = 10000, num_flips: int = 10) -> None:
    results = defaultdict(int)
    for _ in range(num_cases):
        heads_count = 0
        for _ in range(num_flips):
            if random.random() < 0.5:
                heads_count += 1
        results[heads_count] += 1

    percentages = {}
    for heads, count in results.items():
        percentages[heads] = round((count / num_cases) * 100, 2)

    return dict(sorted(percentages.items()))


def draw_gaussian_distribution_graph(probabilities: int) -> int:
    heads = list(probabilities.keys())
    percentages = list(probabilities.values())

    plt.figure(figsize=(10, 6))
    plt.bar(heads, percentages, color="skyblue")
    plt.xlabel("Number of Heads (out of 10 flips)")
    plt.ylabel("Percentage (%)")
    plt.title("Distribution of Heads in 10 Coin Flips")
    plt.xticks(heads)
    plt.grid(axis="y", linestyle="--")
    plt.tight_layout()
    plt.show()
