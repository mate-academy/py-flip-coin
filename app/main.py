"""Simulate repeated coin tosses and visualize the results."""

import random


def flip_coin() -> dict[int, float]:
    """Return the percentage of outcomes for 10 tosses over 10,000 trials."""
    tosses_count = 10
    trials_count = 10_000
    heads_counts = [0] * (tosses_count + 1)

    for _ in range(trials_count):
        heads = sum(random.choice((0, 1)) for _ in range(tosses_count))
        heads_counts[heads] += 1

    return {
        heads: count / trials_count * 100
        for heads, count in enumerate(heads_counts)
    }


def draw_gaussian_distribution_graph() -> None:
    """Plot the simulated distribution of heads for 10 coin tosses."""
    import matplotlib.pyplot as plt

    distribution = flip_coin()
    outcomes = list(distribution)
    percentages = list(distribution.values())

    plt.bar(outcomes, percentages)
    plt.title("Distribution of heads in 10 coin tosses")
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage of trials (%)")
    plt.xticks(outcomes)
    plt.show()


if __name__ == "__main__":
    print(flip_coin())
