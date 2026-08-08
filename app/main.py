import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {num: 0.0 for num in range(11)}
    for _ in range(10_000):
        counter = 0
        for _ in range(10):
            coin = random.choice(["heads", "tails"])
            if coin == "heads":
                counter += 1
        result[counter] += 1

    for key in result:
        result[key] = (result[key] / 10_000) * 100

    return result


def draw_gaussian_distribution_graph() -> None:
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.plot(flip_coin().values())
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage (%)")
    plt.show()
