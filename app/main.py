import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    heads_count = {i: 0 for i in range(11)}
    number = 0
    while True:
        throws = [random.randint(0, 1) for _ in range(10)]
        heads = sum(throws)
        heads_count[heads] += 1
        number += 1
        if number == 10000:
            break

    for key in heads_count:
        heads_count[key] = round(heads_count[key] / 10000 * 100, 2)

    return heads_count


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    x_array = []
    y_array = []
    for key, value in data.items():
        x_array.append(key)
        y_array.append(value)
    coordinate_x = np.array(x_array)
    coordinate_y = np.array(y_array)
    plt.plot(coordinate_x, coordinate_y)
    plt.ylim(0, 100)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads Count")
    plt.ylabel("Drop percentage %")
    plt.show()


draw_gaussian_distribution_graph()
