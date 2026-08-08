import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    """
    Conducts 10000 cases of flipping a coin 10 times.
    Returns a dictionary with the distribution of heads count.

    Returns:
        dict: Keys are numbers of heads (0-10), values are percentages
    """
    num_cases = 10000
    flips_per_case = 10

    heads_count = {i: 0 for i in range(flips_per_case + 1)}

    for _ in range(num_cases):
        heads_in_case = sum(random.choice([0, 1])
                            for _ in range(flips_per_case))
        heads_count[heads_in_case] += 1

    distribution = {
        heads: round((count / num_cases) * 100, 2)
        for heads, count in heads_count.items()
    }

    return distribution


def draw_gaussian_distribution_graph() -> dict:
    """
    Draws a graph showing the distribution of heads in coin flip simulation.

    Returns:
        dict: Distribution of heads from the coin flip simulation.
    """
    distribution = flip_coin()

    x_values = list(distribution.keys())
    y_values = list(distribution.values())

    plt.figure(figsize=(10, 6))
    plt.bar(x_values, y_values, color="skyblue", edgecolor="navy", alpha=0.7)

    plt.xlabel("Number of Heads", fontsize=12)
    plt.ylabel("Percentage (%)", fontsize=12)
    plt.title(
        "Distribution of Heads in 10 Coin Flips (10000 trials)", fontsize=14)

    plt.grid(axis="y", alpha=0.3, linestyle="--")

    plt.xticks(x_values)

    plt.tight_layout()
    plt.show()

    return distribution
