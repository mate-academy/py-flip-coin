import random
import matplotlib.pyplot as plt


def flip_coin(cases: int = 10000, flips: int = 10) -> dict:
    counts = {i: 0 for i in range(flips + 1)}

    for _ in range(cases):
        heads = sum(random.randint(0, 1) for _ in range(flips))
        counts[heads] += 1

    return {k: round(v / cases * 100, 2) for k, v in counts.items()}


print(flip_coin())


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    heads_counts = list(data.keys())
    percentages = list(data.values())

    plt.figure(figsize=(10, 6))
    plt.plot(
        heads_counts,
        percentages,
        marker="o",
        color="blue",
        linewidth=2,
        markersize=6)
    plt.fill_between(
        heads_counts,
        percentages,
        alpha=0.2,
        color="blue")

    plt.title("Draw gaussian distribution graph(flip coin)")
    plt.xlabel("Number of Heads:", fontsize=12)
    plt.ylabel("Percentage (%)", fontsize=12)
    plt.xticks(heads_counts)
    plt.grid(True, linestyle="--", alpha=0.6)

    plt.tight_layout()
    plt.savefig("gaussian_distribution.png", dpi=150)
    plt.show()


draw_gaussian_distribution_graph()
