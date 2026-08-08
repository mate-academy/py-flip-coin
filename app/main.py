import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {i: 0 for i in range(0, 11)}

    for _ in range(10000):
        head = 0
        for __ in range(10):
            if random.randint(0, 1) == 1:
                head += 1
        result[head] += 0.01

    return result


def draw_gaussian_distribution_graph() -> None:
    fliped = flip_coin()
    plt.plot(fliped.keys(), fliped.values())
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.show()
