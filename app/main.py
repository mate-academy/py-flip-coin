import random
from matplotlib import pyplot as plt


def flip_coin() -> dict:
    results = {amount: 0 for amount in range(11)}
    for _ in range(10000):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        results[heads] += 1
    total = sum(results.values())
    return {k: (v / total) * 100 for k, v in results.items()}


def draw_gaussian_distribution_graph(data: dict) -> None:
    heads_counts = list(data.keys())
    percentages = list(data.values())
    plt.figure()
    plt.bar(heads_counts, percentages)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage%")
    plt.title("Gaussian distribution")
    plt.xticks(heads_counts)
    plt.grid(True)
    plt.show()
