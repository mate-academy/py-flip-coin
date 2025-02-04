import random
import matplotlib.pyplot as plt


def flip_coin(trials: int = 10000,
              flips: int = 10) -> dict[int, float]:
    flip_result = {i: 0 for i in range(0, flips + 1)}

    for _ in range(trials):
        head = (sum(random.choice[0, 1]) for _ in range(flips))
        flip_result[head] += 1

    for key in flip_result:
        flip_result[key] = (flip_result[key] / trials) * 100

    return flip_result


def draw_gaussian_distribution_graph(data: dict[int, float]) -> None:
    plt.bar(data.keys(), data.values(), color="skyblue", edgecolor="black")
    plt.title("Gaussian Distribution of Coin Flips (10 flips, 10000 trials)")
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage")
    plt.xticks(range(11))  # From 0 to 10 heads
    plt.grid(axis="y", linestyle=""-"", alpha=0.7)
    plt.show()
