import random
from collections import defaultdict
import matplotlib.pyplot as plt


def flip_coin(num_flips: int = 10,
              num_trials: int = 10000) -> dict[int, float]:
    results = defaultdict(int)

    for _ in range(num_trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(num_flips))
        results[heads_count] += 1

    percentages = {num: round(v / num_trials * 100, 2)
                   for num, vit in results.items()}

    for num in range(num_flips + 1):
        if num not in percentages:
            percentages[k] = 0.0

    return dict(sorted(percentages.items()))


def draw_gaussian_distribution_graph(distribution: dict[int, float]) -> None:
    list_1 = list(distribution.keys())
    list2 = list(distribution.values())

    plt.bar(list_1, list2, color='skyblue')
    plt.xlabel("Number of heads in 10 flips")
    plt.ylabel("Percentage of trials (%)")
    plt.title("Distribution of Heads in 10 Coin Flips")
    plt.xticks(list_1)
    plt.show()


# Example usage
distribution = flip_coin()
print(distribution)
draw_gaussian_distribution_graph(distribution)
