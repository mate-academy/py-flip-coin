import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    trials = 10000
    counts = {i: 0 for i in range(11)}

    for _ in range(trials):
        heads = sum(random.randint(0, 1) for _ in range(10))
        counts[heads] += 1

    percentages = {
        k: round((v / trials) * 100, 2) for k, v in counts.items()
    }
    return percentages


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    heads_count = list(data.keys())
    percentages = list(data.values())

    plt.figure(figsize=(8, 5))
    plt.bar(heads_count, percentages, color="skyblue", edgecolor="black")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.title("Coin Flip Distribution (Binomial / Gaussian)")
    plt.xticks(heads_count)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()
