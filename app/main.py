import random
import matplotlib.pyplot as plt
from collections import Counter


def flip_coin(trials: int = 10000, flips: int = 10) -> dict[int, float]:
    results = []

    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(flips))
        results.append(heads)

    counts = Counter(results)

    percentages = {k: round((v / trials) * 100, 2) for k, v in counts.items()}

    for i in range(flips + 1):
        percentages.setdefault(i, 0.0)

    return percentages


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    plt.bar(data.keys(), data.values())
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage")
    plt.show()
