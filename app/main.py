import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    cases = 10000
    flips = 10
    counts = {heads: 0 for heads in range(flips + 1)}

    for _ in range(cases):
        heads = sum(random.randint(0, 1) for _ in range(flips))
        counts[heads] += 1

    return {
        heads: round(count / cases * 100, 2)
        for heads, count in counts.items()
    }


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()
    plt.plot(
        list(distribution.keys()),
        list(distribution.values()),
        color="blue",
    )
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.show()
