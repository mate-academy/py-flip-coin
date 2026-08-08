import random
# import matplotlib.pyplot as plt
# import numpy as np


def flip_coin() -> dict:
    coin = ["heads", "tails"]

    heads_counter = [
        sum(random.choice(coin) == "heads" for _ in range(10))
        for _ in range(10_000)
    ]

    result = {
        number: heads_counter.count(number) / 10_000 * 100
        for number in range(0, 11)
    }

    return result


"""
def draw_gaussian_distribution_graph(dist: dict) -> None:
    xpoints = np.array([x for x in range(0, 11)])
    ypoints = np.array([y for y in list(dist.values())])

    plt.plot(xpoints, ypoints)
    plt.xlim(0, max(xpoints))
    plt.ylim(0, 100)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
"""
