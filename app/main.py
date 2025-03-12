import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    coin_sides = ("head", "tail")
    count_head_list = []
    for _ in range(10000):
        head_count = 0
        for _ in range(10):

            case = random.choice(coin_sides)
            if case == "head":
                head_count += 1
        count_head_list.append(head_count)
    return {
        0: count_head_list.count(0) / 10000 * 100,
        1: count_head_list.count(1) / 10000 * 100,
        2: count_head_list.count(2) / 10000 * 100,
        3: count_head_list.count(3) / 10000 * 100,
        4: count_head_list.count(4) / 10000 * 100,
        5: count_head_list.count(5) / 10000 * 100,
        6: count_head_list.count(6) / 10000 * 100,
        7: count_head_list.count(7) / 10000 * 100,
        8: count_head_list.count(8) / 10000 * 100,
        9: count_head_list.count(9) / 10000 * 100,
        10: count_head_list.count(10) / 10000 * 100
    }


def draw_gaussian_distribution_graph() -> None:
    data_input = flip_coin()
    x_values = []
    y_values = []
    for key, value in data_input.items():
        x_values.append(key)
        y_values.append(value)
    x_points = np.array([x_values])
    y_points = np.array([y_values])
    plt.plot(x_points, y_points)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
