import random


import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    number_of_drops = 10000
    random_number = 0
    result_dict = {}
    for i in range(11):
        result_dict[i] = 0

    # random_number += number_of_drops
    for i in range(number_of_drops):
        for drop in range(10):
            random_number += random.randint(0, 1)
        result_dict[random_number] += 1
        random_number = 0

    for argument in result_dict:
        result_dict[argument] = result_dict[argument] / number_of_drops * 100

    return result_dict


def draw_gaussian_distribution_graph() -> None:
    y_points_percentage = [value
                           for value in list(flip_coin().values())]

    x_points = np.array(list(flip_coin().keys()))
    y_points = np.array(y_points_percentage)

    # Fit a quadratic polynomial (degree=2)
    coeffs = np.polyfit(x_points, y_points, 3)
    poly = np.poly1d(coeffs)

    x_new = np.linspace(0, 9, 200)
    y_new = poly(x_new)

    plt.ylim(-2, 100)
    plt.scatter(x_points, y_points, label="Original Points")
    plt.plot(x_new, y_new, label="Quadratic Fit")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.legend()
    plt.grid(True)
    plt.show()


"""
    plt.hexbin(x_points, y_points, gridsize=30)
    plt.colorbar(label="Counts")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Hexagonal Binning")
    plt.show()


    x_new = np.linspace(1, 9, 200)
    y_new = np.interp(x_new, x_points, y_points)

    plt.scatter(x_points, y_points, label="Original Points")
    plt.plot(x_new, y_new, label="Linear Interpolation")
    plt.legend()
    plt.grid(True)
    plt.show()
"""
