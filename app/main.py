import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result = dict.fromkeys(range(11), 0.0)
    for num_first in range(10000):
        head = 0
        for num_second in range(10):
            flip = random.randint(0, 1)
            if flip == 1:
                head += 1
        result[head] = round(result.get(head) + 0.01, 2)
    return result


def draw_gaussian_distribution_graph(result: dict) -> None:
    x_axis = np.array(list(result.keys()))
    y_axis = np.array(list(result.values()))
    plt.plot(x_axis, y_axis)
    plt.xlabel("Heads count")
    plt.ylabel("Drop Percentage %")
    plt.show()
