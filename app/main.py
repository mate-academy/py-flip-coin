import random
import matplotlib.pyplot as plt
from typing import Any


def flip_coin(trials: int = 10000) -> dict:
    counts = [0] * 11
    for _ in range(trials):
        sum_of_heads = (sum([random.randint(0, 1) for _ in range(10)]))
        counts[sum_of_heads] += 1

    heads_dict = {}
    for index, value in enumerate(counts):
        heads_dict[index] = (value / trials) * 100
    return heads_dict


def draw_gaussian_distribution_graph(heads_dict: dict) -> Any:

    x_coord = list(heads_dict.keys())
    y_coord = list(heads_dict.values())

    plt.bar(x_coord, y_coord)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()

# result_data = flip_coin(10000)
# draw_gaussian_distribution_graph(result_data)
