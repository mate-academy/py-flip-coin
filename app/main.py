import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator


def flip_coin() -> dict:
    num_experimets = 10000
    result_dict = {i: 0 for i in range(11)}
    for _ in range(num_experimets):
        counter = sum(random.choice([0, 1]) for _ in range(10))
        result_dict[counter] += 1
    for key, value in result_dict.items():
        result_dict[key] = round(value / num_experimets * 100, 2)
    return result_dict


def draw_gaussian_distribution_graph(dict_to_draw: dict) -> None:
    x_ax = np.array(list(dict_to_draw.keys()))
    x_ay = np.array(list(dict_to_draw.values()))
    plt.plot(x_ax, x_ay)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xticks(x_ax)
    plt.yticks(np.arange(0, 110, 10))
    ay = plt.gca()
    ay.yaxis.set_minor_locator(AutoMinorLocator(2))
    plt.show()
