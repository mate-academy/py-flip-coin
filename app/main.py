import random

from matplotlib import pyplot as plt


def flip_coin() -> dict:
    counts = {key: 0 for key in range(11)}

    for _ in range(10000):
        heads = sum(random.randint(0, 1) for _ in range(10))
        counts[heads] += 1

    return {
        key: round(value / 10000 * 100, 2)
        for key, value in counts.items()
    }


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    plt.figure(figsize=(10, 6))
    plt.plot(
        list(data.keys()),
        list(data.values()),
        marker="o",
        color="blue",
        linewidth=2
    )
    plt.fill_between(
        list(data.keys()),
        list(data.values()),
        alpha=0.2,
        color="blue"
    )

    plt.title("Gaussian Distribution (10 Coin Flips, 10,000 Cases)")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.xticks(range(11))
    plt.grid(True, linestyle="--", alpha=0.5)

    plt.savefig("gaussian_distribution.png", dpi=150)
    plt.show()
