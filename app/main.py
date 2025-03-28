import random
import matplotlib.pyplot as plt
from collections import Counter
from math import exp, sqrt, pi


def flip_coin(n_trials: int = 10000, n_flips: int = 10) -> dict:
    results = []

    for _ in range(n_trials):
        heads_count = sum(random.choice([0, 1])
                          for _ in range(n_flips))
        results.append(heads_count)

    counts = dict(Counter(results))  # Count occurrences of each heads count
    total = sum(counts.values())

    # Convert counts to percentages
    percentages = {k: round((v / total) * 100, 2) for k, v in counts.items()}

    return percentages


def gaussian_distribution(xpoint: float, mean: float, std_dev: float) -> float:
    """ Compute Gaussian (normal) distribution function """
    return ((1 / (std_dev * sqrt(2 * pi)))
            * exp(-0.5 * ((xpoint - mean) / std_dev) ** 2))


def draw_gaussian_distribution_graph(data: dict) -> None:
    xpoint = list(data.keys())  # Number of heads
    ypoint = list(data.values())  # Percentage occurrence

    # Calculate mean and standard deviation manually
    mean = (sum(k * v for k, v in data.items())
            / sum(data.values()))
    variance = sum(((k - mean) ** 2)
                   * v for k, v in data.items()) / sum(data.values())
    std_dev = sqrt(variance)

    # Generate Gaussian curve manually
    x_fit = [i / 10 for i in range(min(xpoint) * 10,
                                   (max(xpoint) + 1) * 10)]  # More points
    y_fit = [gaussian_distribution(i, mean, std_dev)
             * max(ypoint) * 2.5 for i in x_fit]  # Scale Gaussian

    # Plot bar chart
    plt.bar(xpoint, ypoint, color="b", alpha=0.6, label="Simulation Data")

    # Plot Gaussian fit
    plt.plot(x_fit, y_fit, "r-", label="Gaussian Fit")

    # Labels and title
    plt.xlabel("Number of Heads in 10 Flips")
    plt.ylabel("Percentage")
    plt.title("Coin Flip Distribution (10 Flips per Trial)")

    # Add grid and legend
    plt.grid()
    plt.legend()

    # Show plot
    plt.show()

    # Print the result dictionary
    print(data)
