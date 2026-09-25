import random

import matplotlib.pyplot as plt

FLIPS_PER_CASE = 10
CASES = 100_000


def flip_coin(cases: int = CASES) -> dict:
    heads_count = {heads: 0 for heads in range(FLIPS_PER_CASE + 1)}

    for _ in range(cases):
        heads = random.getrandbits(FLIPS_PER_CASE).bit_count()
        heads_count[heads] += 1

    return {
        heads: round(count / cases * 100, 2)
        for heads, count in heads_count.items()
    }


def draw_gaussian_distribution_graph(cases: int = CASES) -> None:
    distribution = flip_coin(cases)

    plt.plot(list(distribution.keys()), list(distribution.values()))
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xticks(range(FLIPS_PER_CASE + 1))
    plt.yticks(range(0, 101, 10))
    plt.ylim(0, 100)
    plt.grid(True)
    plt.show()
