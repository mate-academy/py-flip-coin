import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result_dict = {}
    count = 0
    while count < 10001:
        heads_count = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                heads_count += 1
        result_dict[heads_count] = result_dict.get(heads_count, 0) + 1
        count += 1

    for key in result_dict:
        result_dict[key] = round(result_dict[key] / 10001 * 100, 2)
    return result_dict


def draw_gaussian_distribution_graph() -> None:
    data_func = flip_coin()
    x_coordinate = np.array(list(data_func.keys()))
    y_coordinate = np.array(list(data_func.values()))
    plt.plot(x_coordinate, y_coordinate)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Percentage of cases (%)")

    plt.show()
