import random
from typing import Dict
# import matplotlib.pyplot as plt


def flip_coin(num_trials: int = 10000) -> Dict[int, float]:
    results = {i: 0 for i in range(11)}
    for _ in range(num_trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    percentages = {k: round((v / num_trials) * 100, 2)
                   for k, v in results.items()}
    return percentages


# def draw_gaussian_distribution_graph(percentages: Dict[int, float]) -> None:
#     num_heads = list(percentages.keys())
#     percentage = list(percentages.values())
#
#     plt.bar(num_heads, percentage, color="skyblue", edgecolor="black")
#     plt.xlabel("Number of Heads")
#     plt.ylabel("Percentage (%)")
#     plt.title("Distribution of Number of Heads in 10 Coin Flips")
#     plt.show()
