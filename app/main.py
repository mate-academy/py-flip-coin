import random

import matplotlib

import matplotlib.pyplot as plt

import numpy as np


def flip_coin() -> dict:
    result_dict = {i: 0 for i in range(11)}
    for _ in range(10000):
        head_case = 0
        for _ in range(10):
            if random.choice([0, 1]) == 1:
                head_case += 1
        result_dict[head_case] += 0.01
    return result_dict


def draw_gaussian_distribution_graph() -> None:
    result_dict = flip_coin()
    x = list(result_dict.keys())
    y = list(result_dict.values())
    plt.xlim(0, 10)
    plt.xticks([i for i in range(0, 10 + 1)])
    plt.yticks([i for i in range(8, 108 + 18, 10)])
    plt.ylim(0, 100)
    plt.plot(x, y)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
