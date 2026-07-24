import random

import matplotlib.pyplot as plt


def flip_coin(cases: int = 10000, flips: int = 10) -> dict[int, float]:
    """Flip a coin `flips` times, `cases` times in a row.

    Returns a dict where keys are numbers of heads (0 to `flips`)
    and values are percentages of such outcomes.
    """
    counters = {heads: 0 for heads in range(flips + 1)}

    for _ in range(cases):
        heads = sum(random.randint(0, 1) for _ in range(flips))
        counters[heads] += 1

    return {
        heads: round(count / cases * 100, 2)
        for heads, count in counters.items()
    }


def draw_gaussian_distribution_graph() -> None:
    """Draw a graph of the heads distribution."""
    distribution = flip_coin()

    plt.plot(list(distribution.keys()), list(distribution.values()))
    plt.title("Gaussian distribution")
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage, %")
    plt.show()
