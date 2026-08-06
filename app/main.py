import random

import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    """Simulate flipping a coin 10 x 10000 times for distribution."""
    cases = 10000
    counts = {heads: 0 for heads in range(11)}

    for _ in range(cases):
        heads = sum(random.random() < 0.5 for _ in range(10))
        counts[heads] += 1

    return {
        heads: round(counts[heads] / cases * 100, 2)
        for heads in range(11)
    }


def draw_gaussian_distribution_graph() -> None:
    """Draw a line chart showing the distribution of heads in 10 flips."""
    distribution = flip_coin()
    values = list(distribution.values())
    labels = list(distribution.keys())

    plt.figure(figsize=(8, 4))
    plt.plot(labels, values, marker="o", color="royalblue", linewidth=2)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.xticks(labels)
    plt.tight_layout()
    plt.show()
