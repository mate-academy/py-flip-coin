import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    counts = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads = 0
        for _ in range(10):
            result = random.choice(["Heads", "Tails"])
            if result == "Heads":
                heads += 1
        counts[heads] += 1

    results = {k: round((v / 10000) * 100, 2) for k, v in counts.items()}
    return results


def draw_gaussian_distribution_graph(data: dict = None) -> None:
    if data is None:
        data = flip_coin()

    num_heads = list(data.keys())
    percentages = list(data.values())

    plt.figure(figsize=(10, 6))
    plt.bar(
        num_heads, percentages, color="steelblue",
        edgecolor="black", alpha=0.7
    )

    plt.xlabel("Number of Heads", fontsize=12)
    plt.ylabel("Percentage (%)", fontsize=12)
    plt.title(
        "Distribution of Heads in 10 Coin Flips (10,000 trials)",
        fontsize=14,
        fontweight="bold"
    )

    plt.grid(axis="y", alpha=0.3, linestyle="--")

    plt.xticks(num_heads)

    for i, value in enumerate(percentages):
        plt.text(
            i,
            value + 0.3,
            f"{value}%",
            ha="center",
            va="bottom",
            fontsize=9
        )

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    results = flip_coin()
    print(results)

    draw_gaussian_distribution_graph(results)
