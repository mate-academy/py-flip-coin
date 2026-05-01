import random
import matplotlib.pyplot as plt
from collections import Counter


def flip_coin(cases: int = 10000) -> None:
    counts = Counter(
        sum(random.randint(0, 1) for _ in range(10))
        for _ in range(cases)
    )

    return {k: round(counts.get(k, 0) / cases * 100, 2) for k in range(11)}


def draw_gaussian_distribution_graph() -> None:
    results = flip_coin()

    xi = list(results.keys())
    yi = list(results.values())

    plt.figure(figsize=(10, 6))
    plt.bar(xi, yi, color="steelblue",
            edgecolor="white",
            width=0.6,
            label="Simulated")
    plt.plot(xi, yi, color="tomato", marker="o", linewidth=2, label="Trend")

    plt.title("Coin Flip: Gaussian Distribution "
              "(10 flips × 10,000 trials)", fontsize=14)
    plt.xlabel("Number of Heads", fontsize=12)
    plt.ylabel("Percentage (%)", fontsize=12)
    plt.xticks(xi)
    plt.legend()
    plt.tight_layout()
    plt.savefig("/mnt/user-data/outputs/gaussian_distribution.png", dpi=150)
    plt.show()
    print("Graph saved.")


if __name__ == "__main__":
    print(flip_coin())
    draw_gaussian_distribution_graph()
