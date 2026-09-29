import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> None:
    result = {i: 0 for i in range(11)}

    for _ in range(10000):
        pick = sum(random.choice([0, 1]) for _ in range(10))
        result[pick] += 1

    for key in result:
        result[key] = (result[key] / 10000) * 100
    return result


print(flip_coin())


def draw_gaussian_distribution_graph() -> None:
    data_result = flip_coin()
    right = np.array(list(data_result.keys()))
    up = np.array(list(data_result.values()))
    plt.plot(right, up)

    plt.xlabel("Скільки разів з 10 кидків випав орел")
    plt.ylabel("Частота разів випадання орла (%)")
    plt.title("Нормальний розподіл (Гаусса)")

    plt.show()


draw_gaussian_distribution_graph()
