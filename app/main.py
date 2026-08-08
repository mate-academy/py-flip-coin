from random import choices
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    coin = ["heads", "tails"]
    flips_dict = {
        0: 0.0,
        1: 0.0,
        2: 0.0,
        3: 0.0,
        4: 0.0,
        5: 0.0,
        6: 0.0,
        7: 0.0,
        8: 0.0,
        9: 0.0,
        10: 0.0
    }
    for _ in range(10000):
        flips = choices(coin, k=10)
        heads = flips.count("heads")
        flips_dict[heads] += 1
    for i in range(11):
        flips_dict[i] /= 100

    return flips_dict


def draw_gaussian_distribution_graph(coords: dict) -> None:

    coord_x = np.array([x for x in coords.keys()])
    coord_y = np.array([y for y in coords.values()])

    plt.plot(coord_x, coord_y)

    plt.axis((0, 10, 0, 100))
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop precentage %")

    plt.show()
