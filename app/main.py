import random

import matplotlib.pyplot as plt


def flip_coin(cases: int = 10000, flips: int = 10) -> dict:
    heads_count = {heads: 0 for heads in range(flips + 1)}

    for _ in range(cases):
        heads = sum(random.randint(0, 1) for _ in range(flips))
        heads_count[heads] += 1

    return {
        heads: round(count / cases * 100, 2)
        for heads, count in heads_count.items()
    }


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()

    plt.plot(list(distribution.keys()), list(distribution.values()))
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.axis([0, 10, 0, 100])
    plt.show()
