import random
import matplotlib.pyplot as plt
from typing import Dict


def flip_coin() -> Dict[int, float]:
    """Simulate flipping a coin 10 times for 10,000 trials."""
    results = {i: 0 for i in range(11)}
    num_trials = 10000

    for _ in range(num_trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    # Convert counts to percentages
    for key in results:
        results[key] = round((results[key] / num_trials) * 100, 2)

    return results


def draw_gaussian_distribution_graph() -> None:
    """Draw a Gaussian distribution graph for coin flipping results."""
    coin_flip_results = flip_coin()

    head_counts = list(coin_flip_results.keys())
    drop_percentages = list(coin_flip_results.values())

    plt.plot(head_counts, drop_percentages, color="blue")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.grid(True)
    plt.show()
