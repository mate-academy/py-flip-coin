import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {i: 0 for i in range(11)}
    for _ in range(10000):
        heads = 0
        for _ in range(10):
            side_of_coin = random.randint(0, 1)
            if side_of_coin == 1:
                heads += 1
        result[heads] += 1

    for heads in result:
        result[heads] = (result[heads] / 10000) * 100

    return result


def draw_gaussian_distribution_graph() -> dict:
    variable_x = np.arange(0, 11)
    mu = 5
    sigma = 2
    variable_y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(
        -(variable_x - mu) ** 2 / (2 * sigma ** 2)
    )

    plt.figure(figsize=(10, 6))
    plt.plot(variable_x, variable_y * 100)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.grid()
    plt.show()


print(flip_coin())
draw_gaussian_distribution_graph()
