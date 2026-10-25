import random

import matplotlib.pyplot as plt


FLIPS_PER_CASE = 10
CASES_COUNT = 10_000


def flip_coin() -> dict[int, float]:
    heads_frequency = {
        heads_count: 0 for heads_count in range(FLIPS_PER_CASE + 1)
    }

    for _ in range(CASES_COUNT):
        heads_count = sum(
            random.randint(0, 1) for _ in range(FLIPS_PER_CASE)
        )
        heads_frequency[heads_count] += 1

    return {
        heads_count: frequency * 100 / CASES_COUNT
        for heads_count, frequency in heads_frequency.items()
    }


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()

    plt.plot(
        distribution.keys(),
        distribution.values(),
        marker="o",
    )
    plt.title("Coin flip distribution")
    plt.xlabel("Number of heads in 10 flips")
    plt.ylabel("Cases, %")
    plt.xticks(range(FLIPS_PER_CASE + 1))
    plt.grid()
    plt.show()
