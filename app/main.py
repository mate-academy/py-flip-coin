import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result = {}
    for i in range(10000):
        ten_flips = 0
        for _ in range(10):
            coin_flip = random.randint(0, 1)
            if coin_flip == 1:
                ten_flips += 1
        result[i] = ten_flips / 10
    print(result)
    return result

def draw_gaussian_distribution_graph() -> None:
    y_points = np.array(list(flip_coin().values()))
    x_points = np.array(list(flip_coin().keys()))

    plt.plot(x_points, y_points)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
