import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    probability_dict = {key: 0 for key in range(11)}
    for _ in range(10000):
        amount = 0
        for __ in range(10):
            amount += random.randint(0, 1)
        probability_dict[amount] += 0.01
    return probability_dict


def draw_gaussian_distribution_graph() -> None:
    probability_dict = flip_coin()
    xpoints = np.array(list(probability_dict.keys()))
    ypoints = np.array(list(probability_dict.values()))
    plt.plot(xpoints, ypoints)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
