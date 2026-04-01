from random import randint
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    for _ in range(10000):
        count_coins = sum(randint(0, 1) for _ in range(10))
        result[count_coins] += 1
    return {key: value / 100 for key, value in result.items()}


def draw_gaussian_distribution_graph(drop: dict) -> None:
    xpoints = np.array(list(drop.keys()))
    ypoints = np.array(list(drop.values()))

    plt.plot(xpoints, ypoints)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.xticks(range(0, 11))
    plt.yticks(range(0, 101, 10))

    plt.show()
