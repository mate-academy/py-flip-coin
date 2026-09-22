import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result = {num: 0 for num in range(11)}

    for _ in range(10000):
        heads_count_orl = 0
        for _ in range(10):
            heads_count_orl += random.randint(0, 1)
        result[heads_count_orl] += 1
    return {
        chance: round(rest / 10000 * 100, 2)
        for chance, rest in result.items()
    }


def draw_gaussian_distribution_graph() -> any:
    okay = flip_coin()
    new_list = []
    length_list = []
    for num, element in okay.items():
        new_list.append(element)
        length_list.append(num)
    xpoints = np.array(length_list)
    ypoints = np.array(new_list)
    plt.title("Gaussian distribution", loc="center")
    plt.xlabel("Drop percentage %")
    plt.ylabel("Heads count")
    plt.ylim(bottom=None, top=100)
    plt.plot(xpoints, ypoints)
    plt.show()
