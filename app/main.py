import random
from unittest import result

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {}

    def flip_10_times() -> int:
        return sum(random.choices([0, 1], k=10))

    arr_results = []
    for _ in range(10000):
        arr_results.append(flip_10_times())

    for num in range(0, 11):
        result[num] = arr_results.count(num) / 100

    return result


def draw_gaussian_distribution_graph(data_dict: dict) -> None:
    res_keys = list(data_dict.keys())
    res_values = list(data_dict.values())

    plt.plot(res_keys, res_values)
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.yticks(range(0, 101, 10))
    plt.xticks(range(0, 11))
    plt.title("Gaussian Distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
