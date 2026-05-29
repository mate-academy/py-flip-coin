import random

import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    heads_dict = {}
    for _ in range(0, 10000):
        count_heads = sum(random.choices([0, 1], k=10))
        heads_dict[count_heads] = heads_dict.get(count_heads, 0) + 1

    for heads_count in heads_dict:
        heads_dict[heads_count] = round(
            (heads_dict[heads_count] / 10000) * 100, 2
        )

    return heads_dict


def draw_gaussian_distribution_graph(heads_dict: dict) -> None:
    x_points = np.array(list(heads_dict.keys()))
    y_points = np.array(list(heads_dict.values()))

    plt.plot(x_points, y_points)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
