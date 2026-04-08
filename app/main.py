import random
from typing import Dict


def flip_coin(experiments: int = 10000) -> Dict[int, float]:
    results = {heads: 0 for heads in range(11)}

    for _ in range(experiments):
        heads_count = 0

        for _ in range(10):
            if random.choice([0, 1]) == 1:
                heads_count += 1

        results[heads_count] += 1

    for heads in results:
        results[heads] = round(results[heads] / experiments * 100, 2)

    return results


def draw_gaussian_distribution_graph() -> None:
    import matplotlib.pyplot as plt  # ← ВАЖЛИВО: імпорт ТУТ

    distribution = flip_coin()

    x_values = list(distribution.keys())
    y_values = list(distribution.values())

    plt.figure(figsize=(8, 5))
    plt.plot(x_values, y_values, marker="o")
    plt.xlabel("Number of heads (out of 10 flips)")
    plt.ylabel("Percentage (%)")
    plt.title("Gaussian Distribution of Coin Tosses")
    plt.grid(True)
    plt.show()
