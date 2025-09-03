import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    dict_results = {}
    list1 = ["heads", "tail"]
    for _ in range(10000):
        list_results = []
        for member in range(10):
            list_results.append(random.choice(list1))
        result_count = list_results.count("heads")
        if result_count not in dict_results:
            dict_results[result_count] = 1
        else:
            dict_results[result_count] += 1
    for key, value in dict_results.items():
        dict_results[key] = round(value / 10000 * 100, 2)
    dict_results = dict(sorted(dict_results.items()))
    return dict_results


def draw_gaussian_distribution_graph() -> None:
    list_x = []
    list_y = []
    dict_point = flip_coin()
    for key, value in dict_point.items():
        list_x.append(key)
        list_y.append(value)
    x_points = np.array(list_x)
    y_points = np.array(list_y)

    plt.plot(x_points, y_points)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
