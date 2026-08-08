import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    coin = ["H", "T"]
    results = {i: 0 for i in range(11)}
    for _ in range(10000):
        head_count = 0
        for _ in range(10):
            if random.choice(coin) == "H":
                head_count += 1
        results[head_count] += 1
    sort_dict = dict()
    for count, total in sorted(results.items(), key=lambda item: item[0]):
        sort_dict[count] = round(total / 100, 2)
    return sort_dict


def draw_gaussian_distribution_graph(heads: dict) -> None:
    x_axis = np.array([head for head in heads])
    y_axis = np.array([percentage for head, percentage in heads.items()])
    plt.plot(x_axis, y_axis)
    plt.xlabel("Heads Count")
    plt.ylabel("Drop Percentage")
    plt.show()
