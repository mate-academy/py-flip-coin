import random
import matplotlib.pyplot as plt
from typing import Dict


def flip_coin(num_trials: int = 10000) -> Dict[int, float]:
    results: Dict[int, int] = {i: 0 for i in range(11)}

    for _ in range(num_trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    for key in results:
        results[key] = round(results[key] * 100 / num_trials, 2)

    return results


def draw_gaussian_distribution_graph(distribution: Dict[int, float]) -> None:
    xer = list(distribution.keys())
    yer = list(distribution.values())

    plt.figure(figsize=(10, 6))
    plt.plot(xer, yer, marker="o", linestyle="-", color="blue")
    plt.title("Gaussian Distribution of 10 Coin Flips")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.grid(True)
    plt.xticks(range(11))
    plt.show()
