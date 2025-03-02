import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result_flip_heads = []
    for _ in range(1, 10001):
        flips = [random.choice(["tails", "heads"]) for _ in range(1, 11)]
        flips_heads_count = flips.count("heads")
        result_flip_heads.append(flips_heads_count)
    return {
        i: result_flip_heads.count(i)
        / len(result_flip_heads)
        * 100 for i in range(11)
    }


def draw_gaussian_distribution_graph() -> None:
    flip_coin_heads = flip_coin()
    x_points = np.array([x for x in flip_coin_heads.keys()])
    y_points = np.array([y for y in flip_coin_heads.values()])
    plt.plot(x_points, y_points)

    font = {"family": "serif", "color": "red", "size": 10}
    plt.title("Gaussian distribution", fontdict=font)
    plt.xlabel("Heads count", fontdict=font)
    plt.ylabel("Percent", fontdict=font)

    plt.show()
