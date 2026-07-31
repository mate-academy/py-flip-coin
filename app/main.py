import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    number_of_flipping_coin = 10
    cases = 100000
    heads_count = {}
    for key in range(number_of_flipping_coin + 1):
        heads_count[key] = 0

    for _ in range(cases):
        counter = 0
        for flip in range(number_of_flipping_coin):
            counter += random.randint(0, 1)
        heads_count[counter] += 1

    for key in range(number_of_flipping_coin + 1):
        heads_count[key] /= cases / 100

    return heads_count


def draw_gaussian_distribution_graph(draw: dict) -> None:
    x_array = []
    y_array = []
    for key, value in draw.items():
        x_array.append(key)
        y_array.append(value)

    x_np = np.array(x_array)
    y_np = np.array(y_array)

    plt.plot(x_np, y_np)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
