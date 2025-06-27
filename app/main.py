import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    num_experiments = 10000
    num_flips = 10
    results = {k: 0 for k in range(num_flips + 1)}

    for _ in range(num_experiments):
        heads_count = 0
        for _ in range(num_flips):
            if random.choice(["H", "T"]) == "H":
                heads_count += 1
        results[heads_count] += 1

    # convert to percentages
    for k in results:
        results[k] = (results[k] / num_experiments) * 100

    return results


def draw_gaussian_distribution_graph(distribution: dict) -> None:
    """
    Plots the distribution of number of heads in 10 coin flips
    as a bar graph with labels and a grid.
    """
    # x-axis: number of heads (0 to 10)
    x = list(distribution.keys())
    # y-axis: percentages
    y = list(distribution.values())

    plt.bar(x, y, color="skyblue", edgecolor="black")

    plt.title("Distribution of Heads in 10 Coin Flips (approx Gaussian)")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage of Occurrences (%)")
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    plt.xticks(range(0, 11))  # 0 to 10 heads
    plt.show()
