import matplotlib.pyplot as plt
import numpy as np
from typing import Dict


def flip_coin(
        num_trials: int = 10000,
        num_flips: int = 10
) -> Dict[int, float]:
    results = {}

    for _ in range(num_trials):
        num_heads = sum(np.random.choice([0, 1], size=num_flips))
        results[num_heads] = results.get(num_heads, 0) + 1

    percentages = {
        key: (value / num_trials) * 100 for key,
        value in results.items()
    }
    return percentages


def draw_gaussian_distribution_graph(
        coin_distribution: Dict[int, float]
) -> None:
    num_heads = list(coin_distribution.keys())
    percentages = list(coin_distribution.values())

    plt.bar(num_heads, percentages, color="blue", alpha=0.7)
    plt.title("Coin Flip Distribution")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.show()


if __name__ == "__main__":
    coin_flip_results = flip_coin()
    print(coin_flip_results)

    draw_gaussian_distribution_graph(coin_flip_results)
