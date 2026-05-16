import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = [0] * 11
    repeats = 10000

    for _ in range(repeats):
        heads = sum(random.randint(0, 1) for _ in range(10))
        result[heads] += 1

    return {i: cnt * 100 / repeats for i, cnt in enumerate(result)}


def draw_gaussian_distribution_graph(distribution: dict) -> None:
    plt.plot(distribution.keys(), distribution.values())

    plt.title("Gaussian distribution")

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.xlim(0, 10)
    plt.xticks(range(11))

    plt.ylim(0, 100)
    plt.yticks(range(0, 100, 10))

    plt.show()
