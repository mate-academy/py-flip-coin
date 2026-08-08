import random
import numpy as np
import matplotlib.pyplot as plt
from typing import Callable


def flip_coin(attempts: int = 10000, flip: int = 10) -> dict:
    amount = []
    attempt = []
    for _ in range(attempts):
        for _ in range(flip):
            attempt.append(random.choice(["heads", "tails"]))
        amount.append(attempt.count("heads"))
        attempt = []
    percentage = {i: round((amount.count(i) / attempts) * 100, 2)
                  for i in range(flip + 1)}
    return percentage


def draw_gaussian_distribution_graph(func: Callable[[int, int], dict]) -> None:
    x_point = np.array(list(func.keys()))
    y_point = np.array(list(func.values()))

    plt.ylim(0, 100)
    plt.xlim(0, 10)

    plt.yticks(np.arange(0, 100, 5), minor=True)
    plt.yticks(np.arange(0, 110, 10))
    plt.xticks(np.arange(0, 11, 1))

    plt.plot(x_point, y_point)

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
