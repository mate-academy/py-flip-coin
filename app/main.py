import random
import matplotlib.pyplot as plt
from collections import Counter


def flip_coin(trials: int = 10000) -> dict[int, float]:
    results = []

    for _ in range(trials):
        heads = sum(random.choice(["H", "T"]) == "H" for _ in range(10))
        results.append(heads)

    counts = Counter(results)

    percentages = {k: (counts.get(k, 0) / trials) * 100 for k in range(11)}

    return percentages


def draw_gaussian_distribution_graph(percentages: dict) -> None:
    sorted_keys = sorted(percentages.keys())
    percentages_values = [percentages[k] for k in sorted_keys]

    plt.bar(sorted_keys, percentages_values, color="blue", edgecolor="black")

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xticks(range(0, 11))
    plt.grid(axis="y", alpha=0.3)

    plt.show()
