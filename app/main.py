import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin(cases: int = 10000, flips: int = 10) -> dict:
    temp_dict = {i: 0 for i in range(flips + 1)}
    for _ in range(cases):
        temp_dict[sum(random.choice([0, 1]) for _ in range(flips))] += 1
    results_dict = {}
    for key in temp_dict:
        results_dict[key] = (temp_dict[key] / cases) * 100
    return results_dict


def draw_gaussian_distribution_graph(result_dict: dict) -> None:
    x_value = np.array(list(flip_coin().keys()))
    y_value = np.array(list(flip_coin().values()))
    plt.plot(x_value, y_value)
    plt.xlabel("Head count")
    plt.ylabel("Drop percentage %")
    plt.title = "Gaussian distribution"
    plt.show()
