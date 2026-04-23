import random
import matplotlib.pyplot as plt
from typing import Dict


def flip_coin() -> Dict:
    num_simulations = 10000
    heads_count = {i: 0 for i in range(11)}

    for _ in range(num_simulations):
        heads_in_trial = sum(random.choice([0, 1]) for _ in range(10))
        heads_count[heads_in_trial] += 1

    percentages = {k: round((v / num_simulations) * 100, 2)
                   for k, v in heads_count.items()}

    return percentages


def draw_gaussian_distribution_graph() -> Dict:
    data = flip_coin()

    heads_counts = list(data.keys())
    percentages = list(data.values())

    plt.figure(figsize=(10, 6))
    plt.plot(heads_counts, percentages, "b-", linewidth=2,
             marker="o", markersize=4)

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage, %")
    plt.title("Gaussian distribution")

    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.xticks(range(0, 11))
    plt.yticks(range(0, 101, 10))

    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

    return data
