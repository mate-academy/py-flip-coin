import random
from matplotlib import pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result_exps = {}
    for _ in range(10000):
        result_of_one_exp = 0
        for _ in range(10):
            coin = random.randint(0, 1)
            if coin == 1:
                result_of_one_exp += 1
        result_exps[result_of_one_exp] = result_exps.get(
            result_of_one_exp, 0) + 1
    for key, value in result_exps.items():
        result_exps[key] = round((value / 100), 2)
    return dict(sorted(result_exps.items()))


def draw_gaussian_distribution_graph() -> None:
    result = flip_coin()
    xpoints = np.array(list(result.keys()))
    ypoints = np.array(list(result.values()))
    plt.title("Gaussian Distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.plot(xpoints, ypoints)
    plt.xticks(range(11))
    plt.yticks(range(0, 101, 10))
    plt.show()
