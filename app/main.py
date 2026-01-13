import random
from collections import defaultdict
import matplotlib.pyplot as plt


def flip_coin(num_flips: int = 10, num_trials: int = 10000) -> dict[int, float]:
    """
    Simulate flipping a coin `num_flips` times for `num_trials` trials.
    Returns a dictionary with number of heads as keys and percentage as values.
    """
    results = defaultdict(int)

    for _ in range(num_trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(num_flips))
        results[heads_count] += 1

    # Convert counts to percentages
    percentages = {k: round(v / num_trials * 100, 2) for k, v in results.items()}

    # Make sure all keys 0-10 exist
    for k in range(num_flips + 1):
        if k not in percentages:
            percentages[k] = 0.0

    return dict(sorted(percentages.items()))


def draw_gaussian_distribution_graph(distribution: dict[int, float]) -> None:
    """
    Draws a bar graph showing the Gaussian-like distribution of heads counts.
    """
    x = list(distribution.keys())
    y = list(distribution.values())

    plt.bar(x, y, color='skyblue')
    plt.xlabel("Number of heads in 10 flips")
    plt.ylabel("Percentage of trials (%)")
    plt.title("Distribution of Heads in 10 Coin Flips")
    plt.xticks(x)
    plt.show()


# Example usage
distribution = flip_coin()
print(distribution)
draw_gaussian_distribution_graph(distribution)
