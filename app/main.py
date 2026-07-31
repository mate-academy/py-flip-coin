import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    res = {i: 0 for i in range(0, 11)}
    for num in range(0, 10000):
        count = 0
        for number in range(0, 10):
            if random.randint(0, 1):
                count += 1
        res[count] += 1
    res = {key: value / 10000 for key, value in res.items()}
    return res


def draw_gaussian_distribution_graph() -> None:
    flipped_points = flip_coin()

    xpoints = np.array(list(flipped_points.keys()))

    ypoints = np.array([100 * prc for prc in flipped_points.values()])

    plt.plot(xpoints, ypoints)

    plt.ylim([0, 100])

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")

    plt.show()


draw_gaussian_distribution_graph()
