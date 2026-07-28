import random

import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    """Simulate flipping a coin 10 times in at least 10000 experiments."""
    experiments = 10000

    results = {heads: 0 for heads in range(11)}

    for _ in range(experiments):
        heads = 0

        for _ in range(10):
            if random.choice([True, False]):
                heads += 1

        results[heads] += 1

    return {
        heads: round(count * 100 / experiments, 2)
        for heads, count in results.items()
    }


def draw_gaussian_distribution_graph() -> None:
    """Draw the distribution of heads percentages."""
    distribution = flip_coin()

    plt.figure(figsize=(8, 5))
    plt.plot(
        list(distribution.keys()),
        list(distribution.values()),
        marker="o",
    )

    plt.title("Gaussian Distribution of Coin Flips")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.xticks(range(11))
    plt.grid(True)

    plt.show()


if __name__ == "__main__":
    print(flip_coin())
    draw_gaussian_distribution_graph()
