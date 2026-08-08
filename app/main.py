import random

import numpy as np
import matplotlib.pyplot as plt


def flip_coin():
    heads_dict = {}

    for _ in range(10000):
        heads = 0
        for i in range(10):
            if random.randint(1, 2) == 1:
                heads += 1
        heads_dict[heads] = heads_dict.get(heads, 0) + 1

    percentage_dict = {
        key: round(value * 0.01, 2)
        for key, value in heads_dict.items()
    }
    result_dict = dict(sorted(percentage_dict.items()))
    return result_dict


def draw_gaussian_distribution_graph(result_dict: dict):
    x = [key for key in result_dict.keys()]
    y = [value for value in result_dict.values()]

    plt.plot(x, y)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xticks(np.arange(0, 11, 1))
    plt.yticks(np.arange(0, 110, 10))
    plt.show()
