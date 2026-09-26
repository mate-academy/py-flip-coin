import random

from matplotlib import pyplot as plt


def flip_coin() -> dict[int, float]:
    result = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            flip = random.randint(0, 1)
            if flip:
                heads += 1
        result[heads] += 1
    for i in range(11):
        result[i] = result[i] / 100
    return result


def draw_gaussian_distribution_graph() -> None:
    flips = flip_coin()
    heads = list(flips.keys())
    percentages = list(flips.values())
    plt.bar(heads, percentages)

    plt.xlabel("Number of heads")
    plt.ylabel("Percentage")
    plt.title("Coin toss distribution")
    plt.xticks(range(11))

    plt.show()
