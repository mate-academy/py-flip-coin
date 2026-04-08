import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    coin_sides = ["front", "heads"]
    for _ in range(10000):
        heads_count = 0
        for _ in range(10):
            side = random.choice(coin_sides)
            if side == "heads":
                heads_count += 1
        result[heads_count] += 1

    return {
        key: round((value / 10000) * 100, 2)
        for key, value in result.items()
    }


def draw_gaussian_distribution_graph() -> None:
    coords = flip_coin()
    xypoints = np.array(list(coords.keys()))
    ypoints = np.array(list(coords.values()))

    plt.plot(xypoints, ypoints)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.ylim(0, 100)

    plt.show()
