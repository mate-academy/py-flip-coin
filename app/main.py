import random
from collections import Counter
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("Agg")


def flip_coin(trials: int = 10_000, flips_per_trial: int = 10) -> dict:
    """Simulates coin flips and returns the distribution of heads count."""
    results = [
        sum(random.choice([0, 1]) for _ in range(flips_per_trial))
        for _ in range(trials)
    ]
    counts = Counter(results)
    total = sum(counts.values())
    distribution = {
        key: (value / total) * 100
        for key, value in sorted(counts.items())
    }
    return distribution


def draw_gaussian_distribution_graph() -> None:
    """Draws a Gaussian-like distribution graph for coin flips."""
    data = flip_coin()
    x, y = list(data.keys()), list(data.values())

    plt.plot(x, y, "b-", linewidth=1.5)
    plt.title("Gaussian Distribution")
    plt.xlabel("Heads Count")
    plt.ylabel("Drop Percentage (%)")
    plt.ylim(0, 100)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()


distribution = flip_coin()
print(distribution)
draw_gaussian_distribution_graph()
