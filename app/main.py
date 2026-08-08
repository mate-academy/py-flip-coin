import matplotlib.pyplot as plt
import numpy as np
import random


def flip_coin() -> dict:
    result = {key: 0 for key in range(11)}
    count_of_fliping = 10_000
    for _ in range(count_of_fliping):
        list_flip = [random.randint(0, 1) for _ in range(10)]
        result[sum(list_flip)] += 1
    result = {key: 100 * result[key] / count_of_fliping for key in range(11)}
    return result


def draw_gaussian_distribution_graph(flip_coin_result: dict) -> None:
    x_points = np.array([index for index in range(11)])
    y_points = np.array([value for value in flip_coin_result.values()])

    plt.plot(x_points, y_points)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.ylim(top=100)

    plt.show()


draw_gaussian_distribution_graph(flip_coin())
