import random
import matplotlib.pyplot as plt


def flip_coin(trials: int = 10000) -> dict:
    counts = {i: 0 for i in range(11)}
    for _ in range(trials):
        heads = sum(random.choice([0, 1]) for _ in range(10))
        counts[heads] += 1
    percentages = {k: round((v / trials) * 100, 2) for k, v in counts.items()}
    return percentages


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    heads_nums = list(data.keys())
    pct_vals = list(data.values())
    plt.figure(figsize=(9, 5))
    plt.bar(heads_nums, pct_vals, color="skyblue", edgecolor="black")
    plt.xlabel("Number of heads (0 to 10)", fontsize=12)
    plt.ylabel("Percentage (%)", fontsize=12)
    plt.title("Normal Distribution of 10 Coin Flips", fontsize=14)
    plt.xticks(heads_nums)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


draw_gaussian_distribution_graph()
