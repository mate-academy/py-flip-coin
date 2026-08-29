import random
from typing import Callable

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def flip_coin() -> dict:
    iterations = 10000
    head_percentage = {i: 0.0 for i in range(11)}

    for _ in range(iterations):
        head_count = 0

        for _ in range(10):
            coin = random.randint(0, 1)
            if coin == 0:
                head_count += 1

        head_percentage[head_count] += 1

    total = sum(head_percentage.values())
    for head in head_percentage:
        head_percentage[head] = round(head_percentage[head] / total * 100, 2)

    return head_percentage


def draw_gaussian_distribution_graph(func: Callable) -> None:
    coords = func()

    plt.plot(coords.keys(), coords.values())

    plt.xlim(0, 10)
    plt.ylim(0, 100)

    plt.gca().xaxis.set_major_locator(MultipleLocator(1))
    plt.gca().yaxis.set_major_locator(MultipleLocator(10))

    plt.title("Gaussian Distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
