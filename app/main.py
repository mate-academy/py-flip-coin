import random

import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict[int, float]:
    result_dict: dict[int, float] = {i: 0 for i in range(11)}

    flipping_cases = 10000

    for i in range(flipping_cases):
        result_dict[random.choices(["Avers", "Revers"]
                                   , k=10).count("Avers")] += 1

    for key, value in result_dict.items():
        result_dict[key] = round((value / flipping_cases) * 100, 2)

    return result_dict


def draw_gaussian_distribution_graph(res_dict: dict[int, float]) -> None:
    xpoint = np.array(list(res_dict.keys()))
    ypoint = np.array(list(res_dict.values()))

    plt.plot(xpoint, ypoint)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
