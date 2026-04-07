# write your code here
import random
import matplotlib.pyplot as plt
from typing import Dict


def flip_coin(num_trials: int = 10000) -> Dict[int, float]:
    results: Dict[int, int] = {num_heads: 0 for num_heads in range(11)}

    for _ in range(num_trials):
        heads_count: int = 0

        for _ in range(10):
            if random.random() < 0.5:
                heads_count += 1

        results[heads_count] += 1

    percentages: Dict[int, float] = {}

    for num_heads, count in results.items():
        percentages[num_heads] = round(count / num_trials * 100, 2)

    return percentages


def draw_gaussian_distribution_graph() -> None:
    distribution_data: Dict[int, float] = flip_coin(20000)

    heads_counts: list[int] = list(distribution_data.keys())
    percentages: list[float] = list(distribution_data.values())

    plt.bar(heads_counts, percentages)
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage (%)")
    plt.title("Distribution of Heads in 10 Coin Tosses")
    plt.show()


if __name__ == "__main__":
    print(flip_coin())
    draw_gaussian_distribution_graph()
