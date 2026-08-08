from random import choice
import matplotlib.pyplot as plt


def flip_coin():
    head_percentage = dict()
    heads = 0
    for time in range(10000):
        heads = len([heads for _ in range(10) if choice((0, 1)) == 0])
        head_percentage[heads] = head_percentage.get(heads, 0) + 1
    distribution = {key: (value / 10000) * 100
                    for key, value in head_percentage.items()}
    distribution_keys = list(distribution.keys())
    distribution_keys.sort()
    return {key: distribution[key] for key in distribution_keys}


def draw_gaussian_distribution_graph():
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(*zip(*flip_coin().items()))
    plt.ylim([0, 100])
    plt.ylabel("Drop percentage %", fontsize=14)
    plt.xlabel("Heads count", fontsize=14)
    plt.show()
