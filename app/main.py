import matplotlib.pyplot as plt
import numpy as np
import random


def flip_coin() -> dict:
    return_dict = {
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
        heads_count = 0

        for _ in range(10):
            if random.choice(["head", "tail"]) == "head":
                heads_count += 1

        return_dict[heads_count] += 0.01
        return_dict[heads_count] = round(return_dict[heads_count], 2)

    return return_dict


def draw_gaussian_distribution_graph() -> None:
    x_points = np.array(list(flip_coin().keys()))
    y_points = np.array(list(flip_coin().values()))

    plt.plot(x_points, y_points)
    plt.show()


if __name__ == "__main__":
    draw_gaussian_distribution_graph()
