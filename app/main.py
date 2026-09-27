import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    num_repeat = 10000
    result = {0: 0,
              1: 0,
              2: 0,
              3: 0,
              4: 0,
              5: 0,
              6: 0,
              7: 0,
              8: 0,
              9: 0,
              10: 0}

    for _ in range(num_repeat):
        count = 0
        for _ in range(10):
            if random.randint(0, 1) == 1:
                count += 1
        result[count] += 1

    for key, value in result.items():
        result[key] = round((value / num_repeat) * 100, 2)

    return result


def draw_gaussian_distribution_graph(results: dict) -> None:

    x_values = []
    y_values = []
    for key, value in results.items():
        x_values.append(key)
        y_values.append(value)

    x_points = np.array(x_values)
    y_points = np.array(y_values)

    plt.plot(x_points, y_points)

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.ylim(0, 100)

    plt.show()
