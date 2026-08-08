import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    for i in range(10000):
        current_case = [random.choice((1, 0)) for _ in range(10)]
        result[current_case.count(1)] += 1
    return {key: value / 10000 * 100 for key, value in result.items()}


def draw_gaussian_distribution_graph(result: dict) -> None:
    xpoints = np.array(list(result.keys()))
    ypoints = np.array(list(result.values()))
    print(list(result.keys()))
    print(list(map(str, result.values())))
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.ylim(0, 100)
    plt.xlim(0, 10)
    plt.plot(xpoints, ypoints)
    plt.show()
