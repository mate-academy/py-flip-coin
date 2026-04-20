import random
from typing import Callable

import matplotlib.pyplot as plt


def flip_coin(flips: int = 10, attempts: int = 10_000) -> dict:
    result = dict.fromkeys(range(flips + 1), 0)

    for _ in range(attempts):
        heads_count = sum(random.choice([0, 1]) for _ in range(flips))
        result[heads_count] += 1
    return {
        key: round((value / attempts) * 100, 2)
        for key, value in result.items()
    }


def draw_gaussian_distribution_graph(func: Callable) -> None:
    result = func()
    xline = result.keys()
    yline = result.values()

    plt.plot(xline, yline)
    plt.show()
