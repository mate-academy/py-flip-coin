import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads = 0
        for _ in range(10):
            if random.choice(["h", "t"]) == "h":
                heads += 1
        results[heads] += 1

    for k in results:
        results[k] = round(results[k] / 10000 * 100, 2)
    return results


def draw_gaussian_distribution_graph() -> None:
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y = np.array(
        [0, 1, 2.5, 5, 20, 25, 20, 5, 2.5, 1, 0])
    plt.plot(x, y)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.show()
