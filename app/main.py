import random
from collections import defaultdict
from typing import Dict
import matplotlib.pyplot as plt


def flip_coin(num_trials: int = 10000) -> Dict[int, float]:
    results: Dict[int, int] = defaultdict(int)

    for _ in range(num_trials):
        head_count = sum(random.randint(0, 1) for _ in range(10))
        results[head_count] += 1

    percentages: Dict[int, float] = {
        count: round((freq / num_trials) * 100, 2)
        for count, freq in results.items()
    }

    for i in range(11):
        percentages.setdefault(i, 0.0)

    return percentages


def draw_gaussian_distribution_graph() -> None:
    distribution_data = flip_coin(10000)

    head_counts = sorted(distribution_data.keys())
    percentages = [distribution_data[count] for count in head_counts]

    plt.figure(figsize=(10, 5))
    plt.plot(head_counts, percentages, marker="o", linestyle="-", color="blue")
    plt.title("Distribution of Heads in 10 Coin Flips (10,000 trials)")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.grid(True)
    plt.xticks(range(11))
    plt.show()
