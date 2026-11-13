import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    count = {i: 0 for i in range(11)}

    for i in range(10000):
        coin = random.choices(["Орел", "Решка"], k=10)
        heads_count = coin.count("Орел")
        count[heads_count] += 1

    result = {}
    for key, value in count.items():
        percent = (value / 10000) * 100
        result[key] = round(percent, 2)

    return result


def draw_gaussian_distribution_graph() -> None:
    result_dict = flip_coin()
    x_values = np.array(list(result_dict.keys()))
    y_values = np.array(list(result_dict.values()))

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.plot(x_values, y_values)
    plt.xticks(range(0, 11))
    plt.yticks(range(0, 110, 10))
    plt.show()
