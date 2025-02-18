import random
from collections import Counter
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("Agg")  # Use a non-GUI backend for testing


def flip_coin() -> dict[int, float]:
    """
    Simulate flipping a coin 10 times in 10,000 trials.

    Returns:
        dict[int, float]: A dictionary where keys represent the number of heads
        obtained in 10 flips, and values represent the percentage occurrence.
    """
    num_trials = 10000
    num_flips = 10

    # Simulate 10,000 cases of flipping a coin 10 times
    results = [sum(random.randint(0, 1) for _ in range(num_flips))
               for _ in range(num_trials)]

    # Count occurrences of each number of heads
    counts = Counter(results)

    # Convert counts to percentages
    percentages = {k: (v / num_trials) * 100
                   for k, v in sorted(counts.items())}

    return percentages


def draw_gaussian_distribution_graph(data: dict[int, float]) -> None:
    """
    Draws a histogram showing the distribution of heads in 10 coin flips.

    Args:
        data (dict[int, float]): Dictionary with keys as the number of heads
        obtained and values as percentage occurrence.
    """
    plt.figure(figsize=(8, 5))
    plt.bar(data.keys(), data.values(), alpha=0.7,
            color="blue", edgecolor="black")
    plt.xlabel("Number of Heads in 10 Coin Flips")
    plt.ylabel("Percentage Occurrence")
    plt.title("Gaussian Distribution of Coin Flips")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


# Run simulation and generate results
flip_results = flip_coin()
draw_gaussian_distribution_graph(flip_results)

# Create and display a DataFrame
df = pd.DataFrame(list(flip_results.items()),
                  columns=["Number of Heads", "Percentage"])
print(df)
