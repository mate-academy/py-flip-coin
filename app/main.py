import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for _ in range(10000):
        ten_flips = 0
        for _ in range(10):
            coin_flip = random.randint(0, 1)
            if coin_flip == 1:
                ten_flips += 1
        result[ten_flips] += 1

    for key, value in result.items():
        result[key] = round(value / 100, 2)
    return result

def draw_gaussian_distribution_graph() -> None:
    y_points = np.array(list(flip_coin().values()))
    x_points = np.array(list(flip_coin().keys()))
    plt.ylim([0, 100])
    plt.xlim([0, 10])
    plt.yticks(np.arange(0, 101, step=10))
    plt.xticks(np.arange(0, 11, step=1))

    plt.plot(x_points, y_points)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
