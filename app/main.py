import random

import matplotlib.pyplot as plt

from collections import defaultdict


def flip_coin(trials: int = 10000, flips_per_trial: int = 10) -> dict:
    results = defaultdict(int)

    for _ in range(trials):
        heads_count = sum(
            random.choice([0, 1])
            for _ in range(flips_per_trial)
        )
        results[heads_count] += 1

    probability_distribution = {
        key: round(value / trials * 100, 2) for key, value in results.items()
    }

    return dict(sorted(probability_distribution.items()))


def draw_gaussian_distribution_graph(data: dict) -> None:

    xpoint = list(data.keys())
    ypoint = list(data.values())
    plt.plot(xpoint, ypoint)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xticks(range(11))
    plt.yticks(range(0, 101, 10))

    plt.show()
