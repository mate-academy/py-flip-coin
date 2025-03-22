import random
from matplotlib import pyplot as plt


def flip_coin() -> dict:
    results = {}

    for _ in range(10000):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] = results.get(heads_count, 0) + 1

    results_percentage = {k: round(v / 10000 * 100, 2)
                          for k, v in results.items()}
    return results_percentage


def draw_gaussian_distribution_graph() -> None:
    results = flip_coin()
    x_values = list(map(int, results.keys()))
    y_values = list(results.values())
    plt.bar(x_values, y_values, color="blue", alpha=0.7)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.xticks(range(11))
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()
