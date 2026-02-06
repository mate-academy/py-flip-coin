import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:

    flip_results = {}

    for iteration in range(10001):

        heads = 0
        for flip in range(10):
            if random.randint(0, 1) == 1:
                heads += 1
        flip_results[heads] = flip_results.get(heads, 0) + 1e-02

    return flip_results


def draw_gaussian_distribution_graph() -> None:

    y_values = []
    distribution = flip_coin()

    for i in range(11):
        y_values.append(distribution.get(i, 0))

    plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], y_values)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.ylim(0, 100)
    plt.title("Gaussian distribution")
    plt.show()
