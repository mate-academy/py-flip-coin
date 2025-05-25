import random
from collections import defaultdict
import matplotlib.pyplot as plt


def flip_coin(trials: int = 10000) -> dict:
    """
    Imitates flipping a coin 10 times in each trial, repeated for given number of trials.
    Returns a dictionary with the percentage of how many times each count of heads appeared.
    """
    results = defaultdict(int)

    for _ in range(trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    return {k: round(v / trials * 100, 2) for k, v in sorted(results.items())}


def draw_gaussian_distribution_graph(distribution: dict):
    """
    Draws a Gaussian distribution graph from the distribution of heads.
    """
    x = list(distribution.keys())
    y = list(distribution.values())

    plt.figure(figsize=(10, 5))
    plt.plot(x, y, marker='o', linestyle='-', color='blue')
    plt.title("Distribution of Heads in 10 Coin Flips (10,000 trials)")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.grid(True)
    plt.xticks(range(11))  # 0 through 10
    plt.show()


if __name__ == "__main__":
    result = flip_coin()
    print(result)
    draw_gaussian_distribution_graph(result)
