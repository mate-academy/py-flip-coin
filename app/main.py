import random

# import matplotlib.pyplot as plt
# import matplotlib.ticker as ticker
# import numpy as np


def flip_coin() -> dict:
    results = {
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

    total_trials = 10000
    for _ in range(total_trials):
        heads_times = 0  # 0
        for _ in range(10):
            flip_value = random.randint(0, 1)
            if flip_value == 0:
                heads_times += 1
        results[heads_times] += 1

    for key in results:
        results[key] = round((results[key] / total_trials) * 100, 2)

    return results
#
#
# def draw_gaussian_distribution_graph(points: dict) -> None:
#     x_points = np.array(list(points.keys()))
#     y_points = np.array(list(points.values()))
#
#     plt.plot(x_points, y_points)
#
#     plt.ylim(0, 100)
#     plt.xlim(0, 10)
#
#     plt.title("Gaussian distribution")
#     plt.xlabel("Heads count")
#     plt.ylabel("Drop percentage %")
#
#     plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(10))
#     plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(1))
#
#     plt.show()
