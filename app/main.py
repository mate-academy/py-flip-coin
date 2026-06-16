import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    heads_dict = {key: 0 for key in range(11)}
    for _ in range(10000):
        heads_count = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                heads_count += 1
        heads_dict[heads_count] += 1
    for key in heads_dict:
        heads_dict[key] = round((heads_dict[key] / 10000) * 100, 2)
    return heads_dict


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()
    x_coordinates = np.array(list(distribution.keys()))
    y_coordinates = np.array(list(distribution.values()))
    plt.plot(x_coordinates, y_coordinates, color="blue")
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
