from __future__ import annotations

import random
from typing import Dict, List

try:
    import matplotlib.pyplot as plt
except Exception:
    plt = None


def flip_coin(
    trials: int = 100_000,
    flips_per_trial: int = 10
) -> Dict[int, float]:
    if trials <= 0:
        raise ValueError("trials must be positive")
    if flips_per_trial <= 0:
        raise ValueError("flips_per_trial must be positive")

    results: List[int] = [0] * (flips_per_trial + 1)

    for _ in range(trials):
        heads_count = 0
        for _ in range(flips_per_trial):
            heads_count += 1 if random.random() < 0.5 else 0
        results[heads_count] += 1

    distribution: Dict[int, float] = {}
    for head_count, occurrence in enumerate(results):
        percentage = (occurrence / trials) * 100.0
        distribution[head_count] = round(percentage, 2)
    return distribution


def draw_gaussian_distribution_graph(distribution: Dict[int, float]) -> None:

    if plt is None:
        raise RuntimeError(
            "matplotlib is not available. Install it to draw the graph."
        )

    x_values = sorted(distribution.keys())
    y_values = [distribution[x] for x in x_values]

    plt.figure()
    plt.plot(x_values, y_values, marker="o")
    plt.title("Distribution of Heads in 10 Coin Flips")
    plt.xlabel("Number of Heads (0..10)")
    plt.ylabel("Percentage of Trials (%)")
    plt.xticks(x_values)
    plt.grid(True, linestyle="--", linewidth=0.5, alpha=0.6)
    plt.tight_layout()
    plt.show()
