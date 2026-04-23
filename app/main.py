import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {
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
        10: 0
    }

    for _ in range(10000):
        counter = 0
        for _ in range(10):
            side = random.choice(["heads", "tails"])
            if side == "heads":
                counter += 1
        result[counter] += 1

    for key, value in result.items():
        result[key] = round(value / 10000 * 100, 2)

    return result


def draw_gaussian_distribution_graph() -> None:
    dict_precent = flip_coin()
    x, y = [], []

    for key, value in dict_precent.items():
        x.append(key)
        y.append(value)

    plt.plot(np.array(x), np.array(y))

    plt.ylim(0, 100)
    plt.xlim(0, 10)

    plt.title("Guassian distribution")
    plt.ylabel("Drop percentage %")
    plt.xlabel("Heads count")

    plt.show()
