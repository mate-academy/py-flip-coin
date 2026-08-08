import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    experiments = 10000

    counts = {i: 0 for i in range(11)}

    for _ in range(experiments):
        heads = 0

        for _ in range(10):
            if random.choice(["heads", "tails"]) == "heads":
                heads += 1

        counts[heads] += 1

    percentages = {}

    for heads_count in counts:
        percent = (counts[heads_count] / experiments) * 100
        percentages[heads_count] = round(percent, 2)

    return percentages


def draw_gaussian_distribution_graph(data: dict) -> None:
    x_arg = list(data.keys())
    y_arg = list(data.values())

    plt.plot(x_arg, y_arg)
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage")
    plt.title("Gaussian Distribution of Coin Flips")

    plt.xticks(range(0, 11))
    plt.yticks(range(0, 110, 10))

    plt.show()
