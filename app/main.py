from __future__ import annotations

import random
import matplotlib.pyplot as plt


def flip_coin(trials: int = 10_000, flips: int = 10) -> dict[int, float]:
    """Simulate coin flips and return distribution of heads count."""
    results: dict[int, int] = {i: 0 for i in range(flips + 1)}

    for _ in range(trials):
        heads = sum(random.randint(0, 1) for _ in range(flips))
        results[heads] += 1

    return {k: (v / trials) * 100 for k, v in results.items()}


def draw_gaussian_distribution_graph(distribution: dict[int, float]) -> None:
    """Draw a Gaussian-like distribution graph using matplotlib."""
    plt.plot(
        list(distribution.keys()),
        list(distribution.values()),
        color="blue",
        marker="o",
    )
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    data = flip_coin()
    print(data)
    draw_gaussian_distribution_graph(data)
