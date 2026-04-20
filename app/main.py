import random
import matplotlib.pyplot as plt
from collections import Counter


def flip_coin(num_experiments: int = 10000) -> dict[int, float]:
    """
    Simulate flipping a coin 10 times for many experiments.
    Return a dictionary of head counts (0–10) and their percentages.
    """
    results = []

    for _ in range(num_experiments):
        heads = sum(
            random.choice(["H", "T"]) == "H"
            for _ in range(10)
        )
        results.append(heads)

    counts = Counter(results)

    percentages = {
        i: round((counts[i] / num_experiments) * 100, 2)
        for i in range(11)
    }

    return percentages


def draw_gaussian_distribution_graph(data: dict[int, float]) -> None:
    """
    Draw a Gaussian-like distribution graph based on simulated data.
    """
    plt.bar(
        data.keys(),
        data.values(),
        color="skyblue",
        edgecolor="black"
    )
    plt.title("Distribution of Heads in 10 Coin Flips")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


if __name__ == "__main__":
    distribution = flip_coin()
    print(distribution)
    draw_gaussian_distribution_graph(distribution)
