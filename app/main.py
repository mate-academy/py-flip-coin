import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:

    result = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }
    for _ in range(10000):
        counter = 0
        for _ in range(10):
            if random.randint(0, 1):
                counter += 1
        result[counter] += 1
    return {key: round((value / 10000 * 100), 2)
            for key, value in result.items()}


coin_flips_res = flip_coin()


def draw_gaussian_distribution_graph(coin_flips: dict) -> None:

    x_coords = np.array(list(coin_flips.keys()))
    y_coords = np.array(list(coin_flips.values()))

    plt.plot(x_coords, y_coords)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
