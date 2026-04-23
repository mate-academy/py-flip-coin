import random
from collections import defaultdict


def flip_coin() -> dict:
    results = defaultdict(int)
    for _ in range(10000):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    for heads_count in results:
        results[heads_count] = round((results[heads_count] / 10000) * 100, 2)

    return dict(results)


# def draw_gaussian_distribution_graph(flip_results: dict) -> None:
#     heads, percentages = zip(*sorted(flip_results.items()))
#     plt.bar(heads, percentages)
#     plt.xlabel("Number of Heads")
#     plt.ylabel("Percentage (%)")
#     plt.title("Gaussian Distribution of Coin Flips")
#     plt.show()
