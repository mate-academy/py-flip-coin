import random

import matplotlib.ticker as ticker
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    flip_results = {
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
        heads_count = 0

        for _ in range(10):
            if random.choice(["heads", "tails"]) == "heads":
                heads_count += 1

        flip_results[heads_count] += 1

    return {
        key: value / 100 for key, value in flip_results.items()
    }


def draw_gaussian_distribution_graph() -> None:
    flip_percentage = flip_coin()
    x_points = []
    y_points = []

    for key, value in flip_percentage.items():
        x_points.append(key)
        y_points.append(value)

    plt.plot(x_points, y_points)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.ylim(0, 100)
    plt.yticks(range(0, 101, 10))
    plt.xlim(0, 10)
    plt.xticks(range(0, 11, 1))
    plt.gca().yaxis.set_minor_locator(ticker.MultipleLocator(5))
    plt.show()
