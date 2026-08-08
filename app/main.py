import random
from collections import defaultdict
from typing import Dict
import matplotlib.pyplot as plt


def flip_coin(trials: int = 10000,
              flips_per_trial: int = 10) -> Dict[int, float]:
    results = defaultdict(int)

    for _ in range(trials):
        heads_count = sum(random.choice([0, 1])
                          for _ in range(flips_per_trial))
        results[heads_count] += 1

    for heads_total in results:
        results[heads_total] = round((results[heads_total] / trials) * 100, 2)

    return dict(sorted(results.items()))


def draw_gaussian_distribution_graph(data: Dict[int, float]) -> None:
    keys = list(data.keys())
    values = list(data.values())

    plt.figure(figsize=(10, 6))
    plt.bar(keys, values, color="skyblue", edgecolor="black")
    plt.title("Распределение выпадений орла при 10 подбрасываниях монеты")
    plt.xlabel("Количество выпадений орла")
    plt.ylabel("Процент случаев (%)")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.xticks(range(11))
    plt.show()


if __name__ == "__main__":
    coin_flip_result = flip_coin()
    print(coin_flip_result)
    draw_gaussian_distribution_graph(coin_flip_result)
