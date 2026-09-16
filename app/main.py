from random import randint

import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    coin_head_quantity = {}
    number_of_drops = 10_000

    for number in range(number_of_drops):
        count_success = 0
        for drop_coin in range(10):
            if randint(1, 2) == 1:
                count_success += 1

        coin_head_quantity[count_success] = (
            coin_head_quantity.get(count_success, 0) + 1)

    coin_head_probability = {key: value / number_of_drops * 100
                             for key, value in coin_head_quantity.items()}

    return dict(sorted(coin_head_probability.items()))


def draw_gaussian_distribution_graph() -> None:
    gaussian_distribution = flip_coin()

    x_points = np.array([key for key in gaussian_distribution])
    y_points = np.array([value for value in gaussian_distribution.values()])

    plt.plot(x_points, y_points)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
