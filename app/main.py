import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    result = {i: 0.0 for i in range(11)}
    for _ in range(10000):
        count = 0
        for _ in range(10):
            if random.choice([True, False]):
                count += 1
        result[count] += 1
    for key in result.keys():
        result[key] = round(result[key] / 10000 * 100, 2)
    return result


def draw_gaussian_distribution_graph() -> None:
    result = flip_coin()
    x_axis = np.array(list(result.keys()))
    y_axis = np.array(list(result.values()))
    plt.plot(x_axis, y_axis)
    plt.xlabel("Average Pulse")
    plt.ylabel("Calorie Burnage")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage, %")
    plt.title("Gaussian Distribution")
    plt.show()


if __name__ == "__main__":
    draw_gaussian_distribution_graph()
