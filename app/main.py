import matplotlib.pyplot as plt
import numpy as np
import random


def flip_coin() -> dict:
    results = {}
    number_of_attempts = 10000

    for _ in range(number_of_attempts):
        number_of_heads = 0
        for _ in range(10):
            if random.randint(1, 2) == 2:
                number_of_heads += 1
        results[number_of_heads] = results.get(number_of_heads, 0) + 1

    return {key: value / number_of_attempts * 100
            for key, value in sorted(results.items())}


def draw_gaussian_distribution_graph() -> None:
    flip_map = flip_coin()
    x_points = np.array(list(flip_map.keys()))
    y_points = np.array(list(flip_map.values()))

    plt.plot(x_points, y_points, marker="o", color="black")
    plt.ylim(0, 100)
    plt.xlabel("Количество орлов")
    plt.ylabel("Вероятность")
    plt.title("Gaussian distribution")
    plt.show()
