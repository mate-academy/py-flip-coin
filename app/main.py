import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from scipy.stats import norm


def flip_coin(n_trials: int = 10000, n_flips: int = 10) -> dict:
    results = []

    for _ in range(n_trials):
        heads_count = np.random.binomial(n_flips, 0.5)
        results.append(heads_count)

    counts = dict(Counter(results))  # Count occurrences of each heads count
    total = sum(counts.values())

    # Convert counts to percentages
    percentages = {k: round((v / total) * 100, 2) for k, v in counts.items()}

    return percentages


def draw_gaussian_distribution_graph(data: dict) -> None:
    xpoint = list(data.keys())  # Number of heads
    ypoint = list(data.values())  # Percentage occurrence
    mu, sigma = np.mean(xpoint), np.std(xpoint)
    x_fit = np.linspace(min(xpoint), max(xpoint), 100)
    y_fit = norm.pdf(x_fit, mu, sigma) * max(ypoint) * 2.5

    # Plot Gaussian fit
    plt.plot(x_fit, y_fit, "r-", label="Gaussian Fit")

    # Labels and title
    plt.xlabel("Number of Heads in 10 Flips")
    plt.ylabel("Percentage")
    plt.title("Coin Flip Distribution (10 Flips per Trial)")

    plt.grid()
    plt.legend()

    plt.show()
    print(data)
