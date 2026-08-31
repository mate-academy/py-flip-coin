import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    res = {}
    for _ in range(10000):
        count_heads = 0
        for i in range(10):
            if random.randint(1, 2) == 1:
                count_heads += 1
        res[count_heads] = res.get(count_heads, 0) + 1

    for key, value in res.items():
        res[key] = value / 100
    return dict(sorted(res.items()))


def draw_gaussian_distribution_graph() -> None:
    stats = flip_coin()
    x_points = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y_points = np.array(list(stats.values()))

    plt.plot(x_points, y_points)
    plt.ylim(0, 100)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
