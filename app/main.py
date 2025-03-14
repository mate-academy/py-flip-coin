import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result_dict = {num: 0.0 for num in range(0, 11)}
    for cycle in range(0, 10000):
        result_dict[sum(random.choices([1, 0], k=10))] += 1
    for key, value in result_dict.items():
        result_dict[key] = round((value / 10000) * 100, 2)
    return result_dict


def draw_gaussian_distribution_graph(dictionary: dict) -> None:
    plt.plot(
        dictionary.keys(),
        dictionary.values()
    )
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()


draw_gaussian_distribution_graph(flip_coin())
