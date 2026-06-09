import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    counts_of_heads = dict.fromkeys([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
    number_of_heads = 10000
    for _ in range(number_of_heads):
        ten_flips = [random.randint(0, 1) for _ in range(10)]
        counts_of_heads[ten_flips.count(0)] += 1
    return {
        key: value / number_of_heads * 100
        for key, value in counts_of_heads.items()
    }


def draw_gaussian_distribution_graph(data: dict) -> None:
    x_scale = np.array(list(data.keys()))
    y_scale = np.array(list(data.values()))

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.plot(x_scale, y_scale)
    plt.show()
