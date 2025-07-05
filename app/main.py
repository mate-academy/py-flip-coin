import random
from typing import Dict
from collections import Counter
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("Agg")

def flip_coin(trials: int = 10000) -> Dict[int, float]:
    """
    Simulate flipping a coin 10 times in 10,000 trials.

    Returns:
        dict[int, float]: keys 0..10 (number of heads),
        values are percentages rounded to 2 decimals
    """
    num_flips = 10

    # Simulate trials
    results = [
        sum(random.randint(0, 1) for _ in range(num_flips))
        for _ in range(trials)
    ]

    counts = Counter(results)

    # guarantee all keys 0..10 exist
    percentages = {
        k: round((counts.get(k, 0) / trials) * 100, 2) for k in range(11)
    }

    return percentages


def draw_gaussian_distribution_graph(percentages: Dict[int, float]) -> None:
    """
    Draws a line chart showing the distribution of heads in 10 coin flips
    and saves as PNG.
    """
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
    plt.title("Gaussian distribution of coin flips")
    plt.xlabel("Number of Heads in 10 Flips")
    plt.ylabel("Percentage (%)")
    plt.ylim(0, 100)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.savefig("distribution.png")
    print("Line graph saved as distribution.png")


if __name__ == "__main__":
    results = flip_coin()
    print("\nCoin Flip Distribution:")
    print(f'{"Heads": <10}{"Percentage": <10}')
    print("-" * 20)
    for heads, perc in results.items():
        print(f"{heads:<10}{perc:.2f}%")

    draw_gaussian_distribution_graph(results)
