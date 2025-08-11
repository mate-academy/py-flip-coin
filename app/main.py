import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    coin = ["heads", "tails"]
    chances = {
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
        10: 0,
    }

    for _ in range(10000):
        list_of_sides = []
        for _ in range(10):
            list_of_sides.append(random.choice(coin))
        counter = list_of_sides.count("heads")
        chances[counter] += 1

    for i in range(11):
        chances[i] = chances[i] / 100

    return chances


def draw_gaussian_distribution_graph() -> None:
    result_of_flips = flip_coin()
    heads_count = [key for key in result_of_flips.keys()]
    percents = [value for value in result_of_flips.values()]
    xpoints = np.array(heads_count)
    ypoints = np.array(percents)

    plt.plot(xpoints, ypoints)

    plt.title("Gaussian Distribution")
    plt.xlabel("Heads Count")
    plt.ylabel("Drop Percentage %")

    plt.xticks(range(0, 11, 1))
    plt.yticks(range(0, 101, 10))

    plt.show()
