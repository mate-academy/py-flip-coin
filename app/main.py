import random

import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:

    res = {i: 0 for i in range(11)}

    for _ in range(10000):
        count_of_heads = 0

        for flip in range(10):
            result = random.randint(0, 1)
            if result == 1:
                count_of_heads += 1

        res[count_of_heads] += 1

    for key in res:
        res[key] = round(res[key] / 10000 * 100, 2)

    return res


def draw_gaussian_distribution_graph() -> None:
    flip = flip_coin()
    x_list = []
    y_list = []
    for key, values in flip.items():
        x_list.append(key)
        y_list.append(values)
    xp = np.array(x_list)
    yp = np.array(y_list)
    plt.plot(xp, yp)

    plt.xlabel("Number of Heads")
    plt.ylabel("Drop percentage %")

    plt.show()
