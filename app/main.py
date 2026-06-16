import random
from collections import defaultdict


def flip_coin(cases: int = 10000, flips_per_case: int = 10) -> dict:
    """
    Simulates multiple cases of flipping a coin a specified number of times.

    Args:
        cases: Number of cases to simulate (default is 10000).
        flips_per_case: Number of flips per case (default is 10).

    Returns:
        dict: A dictionary where the keys represent the number of heads
        obtained in a case (from 0 to 10), and the values represent
        the percentage of how each outcome occurred across all cases.
    """
    results = defaultdict(int)

    for _ in range(cases):
        heads = sum(random.choice([0, 1]) for _ in range(flips_per_case))
        results[heads] += 1

    results_in_percentages = {
        key: round((value / cases) * 100, 2)
        for key, value in results.items()
    }
    return dict(sorted(results_in_percentages.items()))


def draw_gaussian_distribution_graph(distribution: dict) -> None:
    """
    Draws a Gaussian distribution graph based on the given distribution data.

    Args:
        distribution: A dictionary where keys represent the number of heads
        obtained in a case (from 0 to 10), and the values represent
        the percentage of how each outcome occurred across all cases.

    Returns:
        None: Displays a line plot showing the distribution of coin flips.
    """
    import matplotlib.pyplot as plt

    plt.plot(
        list(distribution.keys()),
        list(distribution.values()),
        color="blue"
    )
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.ylim(0, 100)
    plt.xlim(0, 10)
    plt.yticks(range(0, 101, 10))
    plt.xticks(range(11))
    plt.show()
