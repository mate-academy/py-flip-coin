from __future__ import annotations

import random

from matplotlib import pyplot as plt


def flip_coin() -> dict[int, float]:
    cases = 10000
    flips = 10
    results = {heads: 0 for heads in range(flips + 1)}

    for _ in range(cases):
        heads = 0

        for _ in range(flips):
            if random.randint(0, 1) == 1:
                heads += 1

        results[heads] += 1

    return {
        heads: round(count * 100 / cases, 2)
        for heads, count in results.items()
    }


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()
    heads = list(distribution.keys())
    percentages = list(distribution.values())

    plt.plot(heads, percentages)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads")
    plt.ylabel("Percentage, %")
    plt.show()
