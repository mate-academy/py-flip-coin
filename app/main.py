import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    dict_counter = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }
    for _ in range(10000):
        counter = 0
        for _ in range(10):
            if random.choice([0, 1]) == 1:
                counter += 1
        dict_counter[counter] += 1
    for key, value in dict_counter.items():
        dict_counter[key] = round(value / 100, 2)
    return dict_counter


def draw_gaussian_distribution_graph() -> None:
    dict_points = flip_coin()

    x_list = []
    y_list = []

    for key, value in dict_points.items():
        x_list.append(key)
        y_list.append(value)

    x_point = np.array(x_list)
    y_point = np.array(y_list)

    plt.plot(x_point, y_point)

    plt.title("Gaussian Distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
