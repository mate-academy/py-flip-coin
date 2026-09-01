import random


import matplotlib.pyplot as plt
import numpy as np

result_dict = {
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


def flip_coin() -> dict:
    for i in range(10_000):
        count = 0
        for _ in range(10):
            current = random.choice(["head", "tail"])
            if current == "head":
                count += 1
        result_dict[count] += 1

    for key in result_dict:
        result_dict[key] = round(((result_dict[key] / 10_000) * 100), 2)
    return result_dict


def draw_gaussian_distribution_graph() -> None:
    flip_coin()

    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.title("Gaussian distribution")
    plt.xlabel("Drop percentage %")
    plt.ylabel("Heads count")

    x_points = np.array(list(result_dict.keys()))
    y_points = np.array(list(result_dict.values()))

    plt.plot(x_points, y_points)
    plt.show()
