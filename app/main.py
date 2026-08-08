import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    count_test = 10000
    result = {i: 0 for i in range(11)}

    for part in range(count_test):
        flip = [random.randint(0, 1) for i in range(10)]
        count = sum(flip)
        result[count] += 1

    for key, value in result.items():
        percent = round((value / count_test) * 100, 2)
        result[key] = percent

    return result


def draw_gaussian_distribution_graph() -> None:
    numbers = flip_coin()
    list_numbers = list(numbers.values())

    ypoints = np.array(list_numbers)
    plt.plot(ypoints)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
    return
