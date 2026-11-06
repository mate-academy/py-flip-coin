import random
import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    cases: int = 10000
    flips: int = 10

    results: dict[int, int] = {i: 0 for i in range(flips + 1)}

    for _ in range(cases):
        heads: int = 0

        for _ in range(flips):
            if random.choice(["heads", "tails"]) == "heads":
                heads += 1

        results[heads] += 1

    percentages: dict[int, float] = {}

    for heads, count in results.items():
        percentages[heads] = round(count / cases * 100, 2)

    return percentages


def draw_gaussian_distribution_graph() -> None:
    results: dict[int, float] = flip_coin()

    number_of_heads: list[int] = list(results.keys())
    percentages: list[float] = list(results.values())

    plt.bar(number_of_heads, percentages, color="skyblue", edgecolor="black")

    plt.title("Coin Flip Distribution")
    plt.xlabel("Number of Heads")
    plt.ylabel("Probability (%)")

    plt.xticks(range(11))
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.show()


print(flip_coin())
draw_gaussian_distribution_graph()
