import random
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    counts = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }
    for iteration in range(10000):
        heads_count = 0
        for flip in range(10):
            heads_count += random.randint(0, 1)
        counts[heads_count] += 1
    for key in counts:
        counts[key] = counts[key] / 100
    return counts


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()

    x_points = list(data.keys())
    y_points = list(data.values())

    plt.plot(x_points, y_points)
    plt.show()
