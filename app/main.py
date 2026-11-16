import random

import matplotlib.pyplot as plt


CASES = 10000
FLIPS = 10


def flip_coin() -> dict[int, float]:
    counts = {heads: 0 for heads in range(FLIPS + 1)}

    for _ in range(CASES):
        heads = sum(random.randint(0, 1) for _ in range(FLIPS))
        counts[heads] += 1

    return {
        heads: round(count / CASES * 100, 2)
        for heads, count in counts.items()
    }


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()

    plt.plot(list(distribution.keys()), list(distribution.values()))
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage of cases, %")
    plt.title("Gaussian distribution")
    plt.show()
