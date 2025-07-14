import random
import matplotlib.pyplot as plt


def flip_coin(trials: int = 10000) -> dict:
    results = {i: 0 for i in range(11)}
    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        results[heads] += 1
    for k in results:
        results[k] = round((results[k] / trials) * 100, 2)
    return results


def draw_gaussian_distribution_graph(distribution: dict) -> None:
    head_counts = list(distribution.keys())
    percentages = list(distribution.values())

    plt.bar(head_counts, percentages, color="skyblue", edgecolor="black")
    plt.title("Distribution of Heads in 10 Coin Flips (10,000 Trials)")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.xticks(range(11))
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()
