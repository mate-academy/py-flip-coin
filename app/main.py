import matplotlib.pyplot as plt
import numpy as np
import random


def flip_coin() -> dict:
    side = ["heads", "tails"]
    dict_heads = {}

    for _ in range(10000):
        heads_count = 0
        for flip in range(10):
            if random.choice(side) == "heads":
                heads_count += 1
        if heads_count not in dict_heads:
            dict_heads[heads_count] = 1
        else:
            dict_heads[heads_count] += 1

    return {
        key: round(dict_heads[key] / 10000 * 100, 2)
        for key in sorted(dict_heads)}


def draw_gaussian_distribution_graph(result: dict) -> None:
    x_points = np.array(list(result.keys()))
    y_points = np.array(list(result.values()))

    plt.plot(x_points, y_points)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
