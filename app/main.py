from random import randint

import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    data = {i: 0 for i in range(11)}
    for _ in range(10000):
        data[sum(randint(0, 1) for _ in range(10))] += 1
    return {key: value / 100 for key, value in data.items()}


def draw_gaussian_distribution_graph() -> None:
    result = flip_coin()
    x_points = list(result.keys())
    y_points = list(result.values())

    plt.plot(x_points, y_points)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
