from __future__ import annotations

import random
from typing import Dict, List, Iterable

try:
    import matplotlib.pyplot as plt
except Exception:
    plt = None


def flip_coin(trials: int = 100_000, flips_per_trial: int = 10) -> Dict[int, float]:

    if trials <= 0:
        raise ValueError("trials must be positive")
    if flips_per_trial <= 0:
        raise ValueError("flips_per_trial must be positive")

    counts: List[int] = [0] * (flips_per_trial + 1)

    for _ in range(trials):
        heads = 0
        for _ in range(flips_per_trial):
            heads += 1 if random.random() < 0.5 else 0
        counts[heads] += 1

    result: Dict[int, float] = {}
    for k, c in enumerate(counts):
        pct = (c / trials) * 100.0
        result[k] = round(pct, 2)
    return result


def draw_gaussian_distribution_graph(dist: Dict[int, float]) -> None:
    if plt is None:
        raise RuntimeError(
            "matplotlib is not available. Install it to draw the graph."
        )

    xs = sorted(dist.keys())
    ys = [dist[x] for x in xs]

    plt.figure()
    plt.plot(xs, ys, marker="o")
    plt.title("Distribution of #Heads in 10 Coin Flips")
    plt.xlabel("Number of Heads (0..10)")
    plt.ylabel("Percentage of Trials (%)")
    plt.xticks(xs)
    plt.grid(True, linestyle="--", linewidth=0.5, alpha=0.6)
    plt.tight_layout()
    plt.show()
