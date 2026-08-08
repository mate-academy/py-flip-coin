import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:

    result = {key: 0 for key in range(11)}

    for _ in range(1, 10001):
        count = 0

        for _ in range(1, 11):
            flip = random.randint(0, 1)
            if flip == 1:
                count += 1
        result[count] += 1

    for percent in result:
        result[percent] = round(result[percent] / 10000 * 100, 2)

    return result


def draw_gaussian_distribution_graph(result: dict) -> None:
    x_dot = list(result.keys())
    y_dot = list(result.values())

    xpoints = np.array(x_dot)
    ypoints = np.array(y_dot)

    plt.plot(xpoints, ypoints, color="blue", linewidth=1)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.show()


data = flip_coin()
print(data)
draw_gaussian_distribution_graph(data)
