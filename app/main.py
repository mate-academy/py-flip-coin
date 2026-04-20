import random
import numpy as np
from matplotlib import pyplot as plt


def flip_coin(quantities: int = 10000) -> dict:
    result = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }
    coin = ["heads", "tails"]
    for _ in range(quantities):
        list_result = []
        for num in range(10):
            list_result.append(random.choice(coin))
        result[list_result.count("heads")] += 1 / quantities * 100
    return result


def draw_gaussian_distribution_graph(results: dict) -> None:
    its_x = np.array([key for key in results])
    its_y = np.array([values for values in results.values()])
    plt.plot(its_x, its_y)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
