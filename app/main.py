import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    result_dict = {i: 0 for i in range(11)}
    heads = 1
    count = 0

    for _ in range(10000):
        for _ in range(10):
            if random.randint(0, 1) == heads:
                count += 1
        result_dict[count] += 1
        count = 0

    total = sum(result_dict.values())
    percentages = {
        key: (value / total) * 100
        for key, value in result_dict.items()
    }
    return percentages


def draw_gaussian_distribution_graph() -> None:
    x_values = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y_values = np.array([value for key, value in flip_coin().items()])

    plt.title("Gaussian distribution", loc="center")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.plot(x_values, y_values)
    plt.ylim(0, 100)
    plt.show()


draw_gaussian_distribution_graph()
