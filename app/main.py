import random

import matplotlib.pyplot as plt


def flip_coin():
    coin = ["heads", "tails"]
    heads_dropped = {i: 0 for i in range(11)}
    for _ in range(10000):
        count_heads = 0
        for _ in range(10):
            if random.choice(coin) == "heads":
                count_heads += 1
        heads_dropped[count_heads] += 1
    heads_dropped = {key: value / 100 for key, value in heads_dropped.items()}
    return heads_dropped


def draw_gaussian_distribution_graph():
    coordinates = flip_coin()

    x = [key for key in coordinates]
    y = [value for value in coordinates.values()]
    plt.plot(x, y)

    plt.axis([0, 10, 0, 100])
    plt.xlim([0, 10])
    plt.ylim([0, 100])
    plt.xticks(range(0, 11, 1))
    plt.yticks(range(0, 110, 10))

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
