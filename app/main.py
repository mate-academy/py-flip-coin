import random
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}

    for _ in range(10000):
        current_result = int(sum(random.randint(0, 1) for _ in range(10)))
        result[current_result] += 1

    finish_result = {i: round(percent / 10000 * 100, 2) for i, percent in result.items()}
    return finish_result


def draw_gaussian_distribution_graph():
    x = np.array([flip_coin().keys()])
    y = np.array(flip_coin().values())
    plt.plot(x, y)
    plt.show()
