import random

import matplotlib.pyplot as plt

from collections import Counter


def flip_coin(trials: int =10000, flips_per_trial: int = 10) -> None:
    results = [sum(random.choice([0, 1]) for i in range(trials))
               for i in range(flips_per_trial)]
    count = Counter(results)
    total_trials = sum(count.values())
    return {k: round(v / total_trials * 100, 2)
            for k, v in sorted(count.items())}


def draw_gaussian_distribution_graph(data):
    plt.bar(data.keys(), data.values(), color='blue', alpha=0.7)
    plt.xlabel("Number of Heads in 10 Coin Flips")
    plt.ylabel("Percentage of Occurrences (%)")
    plt.title("Gaussian Distribution for 10 Coin Flips")
    plt.grid(axis='y', linestely='--', alpha=0.7)
    plt.show()
