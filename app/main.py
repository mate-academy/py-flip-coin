import random
from typing import Dict

import matplotlib.pyplot as plt


def flip_coin() -> Dict[int, float]:
    cases = 10000
    results = {i: 0 for i in range(11)}

    for _ in range(cases):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        results[heads] += 1

    return {
        heads: round((count / cases) * 100, 2)
        for heads, count in results.items()
    }


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    heads_counts = list(data.keys())
    percentages = list(data.values())

    plt.plot(heads_counts, percentages)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.show()
