import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    flip_dict = {
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
        10: 0,
    }
    for _ in range(10000):
        eagle_count = 0
        for one in range(10):
            if random.randint(0, 1) == 1:
                eagle_count += 1
        flip_dict[eagle_count] += 1
    for key, value in flip_dict.items():
        updated_value = value / 100
        flip_dict[key] = updated_value
    return flip_dict


def draw_gaussian_distribution_graph() -> None:
    dict_for_graph = flip_coin()
    list_for_x = dict_for_graph.keys()
    list_for_y = dict_for_graph.values()
    xpoints = np.array(list_for_x)
    ypoints = np.array(list_for_y)
    plt.plot(xpoints, ypoints)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.show()
