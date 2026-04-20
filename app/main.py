import random
from typing import Callable
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result_dict = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            heads += random.randint(0, 1)
        result_dict[heads] += 1

    for key in result_dict:
        result_dict[key] = round(result_dict[key] / 10000 * 100, 2)
    return result_dict


def draw_gaussian_distribution_graph(func: Callable) -> None:
    initial_dict = func()
    list_to_graph = []
    for value in initial_dict.values():
        list_to_graph.append(value)

    plt.plot(list_to_graph)
    plt.show()
