import random

import matplotlib.pyplot as plt
import numpy as np


def flip_coin(cases):
    dictionary = {i: 0 for i in range(11)}

    for _ in range(cases):
        heads = 0
        for _ in range(10):
            if random.randint(1, 2) == 1:
                heads += 1
        dictionary[heads] = dictionary.get(heads, 0) + 1

    for key, value in dictionary.items():
        dictionary[key] = int(value / cases * 100)

    return dict(dictionary.items())


def draw_gaussian_distribution_graph():

    data = flip_coin(1000)

    heads_count = [*data.keys()]
    percentage = [*data.values()]

    x_points = np.array(heads_count)
    y_points = np.array(percentage)

    plt.plot(x_points, y_points)

    plt.xticks(np.arange(0, 11, 1))
    plt.yticks(np.arange(0, 101, 10))

    plt.ylabel("Drop percentage %")
    plt.xlabel("Heads count")
    plt.title("Gaussian distribution")

    plt.show()
