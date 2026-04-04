import random
from typing import Dict

import matplotlib.pyplot as plt


def flip_coin() -> Dict[int, float]:
    cases = 10000
    flips = 10

    counts = {heads_count: 0 for heads_count in range(flips + 1)}

    for _ in range(cases):
        heads = 0
        for _ in range(flips):
            if random.random() < 0.5:
                heads += 1
        counts[heads] += 1

    result = {}

    for heads_count, count in counts.items():
        result[heads_count] = round((count / cases) * 100, 2)

    return result


def draw_gaussian_distribution_graph(distribution: Dict[int, float]) -> None:
    heads_counts = list(distribution.keys())
    percentages = list(distribution.values())

    plt.plot(heads_counts, percentages)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()


if __name__ == "__main__":
    data = flip_coin()
    print(data)
    draw_gaussian_distribution_graph(data)
