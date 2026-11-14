import random

import matplotlib.pyplot as plt


def flip_coin(
    cases: int = 10000,
    flips: int = 10,
) -> dict[int, float]:
    counts = {heads: 0 for heads in range(flips + 1)}

    for _ in range(cases):
        heads = sum(random.randint(0, 1) for _ in range(flips))
        counts[heads] += 1

    return {
        heads: round(count / cases * 100, 2)
        for heads, count in counts.items()
    }


def draw_gaussian_distribution_graph(
    distribution: dict[int, float],
) -> None:
    plt.plot(list(distribution.keys()), list(distribution.values()))
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xticks(range(11))
    plt.grid(True)
    plt.show()
