import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result_dict = {
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
    choices = ("heads", "tails")

    for _ in range(10000):
        heads_count = 0
        for _ in range(10):
            choice = random.choice(choices)
            if choice == "heads":
                heads_count += 1
        result_dict[heads_count] += 0.01
        result_dict[heads_count] = round(result_dict[heads_count], 2)

    return result_dict


def draw_gaussian_distribution_graph() -> None:
    flips_dict = flip_coin()

    x_points = np.array(list(flips_dict.keys()))
    y_points = np.array(list(flips_dict.values()))

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.plot(x_points, y_points)
    plt.show()


draw_gaussian_distribution_graph()
