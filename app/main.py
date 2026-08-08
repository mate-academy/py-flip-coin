import random
import matplotlib.pyplot as plt


def flip_coin(trails: int = 10000) -> dict[int, float]:
    counts = {i: 0 for i in range(11)}
    for _ in range(trails):
        heads = sum(random.randint(0, 1) for _ in range(10))
        counts[heads] += 1
    return {k: round(v * 100 / trails, 2) for k, v in counts.items()}


def draw_gaussian_distribution_graph(trails: int = 10000) -> None:
    distributions = flip_coin(trails)

    heads_counts = list(distributions.keys())
    percentages = list(distributions.values())

    plt.plot(
        heads_counts,
        percentages,
        marker="o",
        linestyle="-",
        color="blue"
    )
    plt.title("Coin Flip Distribution (10 tosses)")
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage of cases")
    plt.xticks(range(0, 11))
    plt.grid(True)
    plt.show()


print(flip_coin())
draw_gaussian_distribution_graph()
