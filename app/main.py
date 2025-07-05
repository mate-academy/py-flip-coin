import random
<<<<<<< HEAD
from typing import Dict


def flip_coin(trials: int = 10000) -> Dict[int, float]:
    """
    Simulates flipping a fair coin 10 times, repeated `trials` times.
    Returns a dictionary where:
      keys = 0..10 (number of heads)
      values = percentages rounded to 2 decimal places
    """
    counts = {i: 0 for i in range(11)}
    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        counts[heads] += 1

    percentages = {k: round((v / trials) * 100, 2) for k, v in counts.items()}
    return percentages


def draw_gaussian_distribution_graph(percentages: Dict[int, float]) -> None:
    """
    Draws a line chart of the heads distribution and saves as PNG.
    """
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    head_counts = list(percentages.keys())
    percentages_list = list(percentages.values())

    plt.plot(
        head_counts,
        percentages_list,
        color="blue",
        marker="o",
        linestyle="-",
        linewidth=2
    )
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.ylim(0, 100)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.savefig("distribution.png")
    print("Line graph saved as distribution.png")

if __name__ == "__main__":
    results = flip_coin()
    print(results)
    draw_gaussian_distribution_graph(results)
=======
from collections import Counter
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
    results = [
        sum(random.randint(0, 1) for _ in range(num_flips))
        for _ in range(num_trials)
    ]

    # Count occurrences of each number of heads
    counts = Counter(results)

    # Convert counts to percentages
    percentages = {
        k: (v / num_trials) * 100 for k, v in sorted(counts.items())
    }

    return percentages


def draw_gaussian_distribution_graph(data: dict[int, float]) -> None:
    """
    Draws a histogram showing the distribution of heads in 10 coin flips.

    Args:
        data (dict[int, float]): Dictionary with keys as the number of heads
        obtained and values as percentage occurrence.
    """
    plt.figure(figsize=(8, 5))
    plt.bar(
        data.keys(), data.values(), alpha=0.7, color="blue", edgecolor="black"
    )
    plt.xlabel("Number of Heads in 10 Coin Flips")
    plt.ylabel("Percentage Occurrence")
    plt.title("Gaussian Distribution of Coin Flips")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


# Run simulation and generate results
flip_results = flip_coin()
draw_gaussian_distribution_graph(flip_results)

# Print results as a formatted table
print("\nCoin Flip Distribution:")
print(f'{"Heads": <10}{"Percentage": <10}')
print("-" * 20)
for heads, percentage in flip_results.items():
    print(f"{heads: <10}{percentage: .2f}%")
>>>>>>> 86c8142a09fb763be22a45067b034883eeef7375
