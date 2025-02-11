import random
import matplotlib.pyplot as plt
from typing import Dict


def flip_coin(trials: int = 10000,
              flips_per_trial: int = 10) -> Dict[int, float]:
    results: Dict[int, int] = {i: 0
                               for i in range(flips_per_trial + 1)}

    for _ in range(trials):
        heads_count = sum(random.choice([0, 1])
                          for _ in range(flips_per_trial))
        results[heads_count] += 1

    return {key: round((value / trials) * 100, 2)
            for key, value in results.items()}


def draw_gaussian_distribution_graph(data: Dict[int, float]) -> None:
    plt.bar(list(data.keys()), list(data.values()), color="blue", alpha=0.7)
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.title("Gaussian Distribution of Coin Flips")
    plt.xticks(range(11))
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


coin_flip_results = flip_coin()
print(coin_flip_results)

draw_gaussian_distribution_graph(coin_flip_results)
