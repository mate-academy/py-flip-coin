import random
from typing import Any

import matplotlib.pyplot as plt


def draw_gaussian_distribution_graph(
        xpoints: Any,
        ypoints: Any) -> None:
    plt.plot(xpoints, ypoints)
    plt.ylim(0, 100)
    plt.show()


def flip_coin() -> dict:
    coin = ["head", "number"]
    results = []
    result_dict = {}
    for _ in range(10000):
        count = 0
        for i in range(10):
            if random.choice(coin) == "head":
                count += 1
        results.append(count)
    for count in range(11):
        result_dict[count] = round((results.count(count) / 10000) * 100, 3)

    return result_dict
