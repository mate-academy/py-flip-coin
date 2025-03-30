import random
import matplotlib.pyplot as plt
from typing import Dict


def flip_coin() -> Dict[int, float]:
    trials = 10000
    flips_per_trial = 10
    results = {i: 0 for i in range(flips_per_trial + 1)}

    for i in range(trials):
        heads_count = sum(
            random.choice([0, 1]) for _ in range(flips_per_trial))
        results[heads_count] += 1

    for key in results:
        results[key] = round((results[key] / trials) * 100, 2)

    return results


def draw_gaussian_distribution_graph(results: Dict[int, float]) -> None:
    keys = list(results.keys())
    values = list(results.values())

    plt.bar(keys, values)
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.title("Gaussian Distribution of Coin Flips")
    plt.show()
