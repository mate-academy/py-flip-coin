from collections import Counter
import random


def flip_coin() -> dict:
    total_trials = 10000
    heads_counts = Counter()

    for _ in range(total_trials):
        heads = sum(random.randint(0, 1) for _ in range(10))
        heads_counts[heads] += 1

    result = {}
    for i in range(11):
        percentage = (heads_counts[i] / total_trials) * 100
        result[i] = round(percentage, 2)

    return result


def draw_gaussian_distribution_graph() -> None:
    import matplotlib.pyplot as plt

    data = flip_coin()
    horizontal_axis = list(data.keys())
    vertical_axis = list(data.values())

    plt.bar(
        horizontal_axis,
        vertical_axis,
        color="skyblue",
        edgecolor="black"
    )
    plt.xlabel("Number of Heads")
    plt.ylabel("Percentage (%)")
    plt.title("Coin Tossing Gaussian Distribution")
    plt.xticks(horizontal_axis)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


if __name__ == "__main__":
    print(flip_coin())
