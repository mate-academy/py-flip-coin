import random

from matplotlib import pyplot as plt


def flip_coin() -> dict:
    result = {}
    total_experiments = 10000

    for _ in range(total_experiments):
        heads_count = 0
        for _ in range(10):
            if random.choice(["heads", "tails"]) == "heads":
                heads_count += 1
        if heads_count in result:
            result[heads_count] += 1
        else:
            result[heads_count] = 1

    for key in result:
        result[key] = round(result[key] / total_experiments * 100, 2)

    return result


def draw_gaussian_distribution_graph(distribution: dict) -> None:
    x_keys = list(distribution.keys())
    y_keys = list(distribution.values())
    plt.bar(x_keys, y_keys)
    plt.xlabel("Count of Heads")
    plt.ylabel("percentage (%)")
    plt.title("Gaussian Distribution of Coin Flips")
    plt.show()
