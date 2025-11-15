import matplotlib.pyplot as plt
import numpy as np
import random


def flip_coin() -> dict:
    dictionary = {i: 0 for i in range(11)}
    for _ in range(10000):
        count = 0
        for _ in range(10):
            state = random.choice([True, False])
            if state:
                count += 1
        dictionary[count] += 1
    return {key: (value / 10000) * 100 for key, value in dictionary.items()}


def draw_gaussian_distribution_graph() -> None:
    x_points = np.array([value for value in flip_coin().values()])
    plt.ylim(0, 100)
    plt.plot(x_points)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
