from random import randint
from collections import Counter

import matplotlib.pyplot as plt


def flip_coin() -> dict[int, int]:
    tries = 10000
    heads = list(range(tries))

    for i in range(tries):
        heads[i] = 0
        for _ in range(10):
            heads[i] += randint(0, 1)

    results = Counter(heads)
    results = {
        key: round(value / tries * 100, 2) for key, value in results.items()
    }
    results = dict(sorted(results.items()))
    return results


def draw_gaussian_distribution_graph() -> None:
    flips = flip_coin()

    x_axis = flips.keys()
    y_axis = [flips[k] for k in x_axis]

    plt.plot(x_axis, y_axis)
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.yticks(range(0, 101, 10))
    plt.xticks(range(0, 11))
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.show()
