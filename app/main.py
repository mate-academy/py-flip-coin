
import random
from typing import Dict, Optional

import matplotlib.pyplot as plt


def flip_coin() -> Dict[int, float]:

    trials = 10000
    heads_counts = [0] * 11

    for _ in range(trials):
        heads = sum(random.choice((0, 1)) for _ in range(10))
        heads_counts[heads] += 1

    return {
        heads: count / trials * 100
        for heads, count in enumerate(heads_counts)
    }


def draw_gaussian_distribution_graph(
    distribution: Optional[Dict[int, float]] = None,
) -> None:
    if distribution is None:
        distribution = flip_coin()

    outcomes = list(range(11))
    percentages = [distribution.get(outcome, 0) for outcome in outcomes]

    plt.plot(outcomes, percentages, marker="o")
    plt.title("Distribution of heads in 10 coin flips")
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage of trials")
    plt.xticks(outcomes)
    plt.grid(True)
    plt.show()
