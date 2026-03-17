import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin(number_of_experiments: int = 10000) -> dict:
    result = {key: 0.0 for key in range(11)}
    for _ in range(number_of_experiments):
        heads = 0
        for _ in range(10):
            heads += random.randint(0, 1)
        result[heads] += 1

    for key in result:
        result[key] = round(result[key] / number_of_experiments * 100, 2)

    return result


def draw_gaussian_destribution_graph() -> None:
    result = flip_coin()
    xpoints = np.array([i for i in range(11)])
    ypoints = np.array([value for key, value in result.items()])

    plt.plot(xpoints, ypoints)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.grid(True)
    plt.show()
