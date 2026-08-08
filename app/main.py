import random
# import matplotlib.pyplot as plt
# import numpy as np


def flip_coin() -> dict:
    flips = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for _ in range(10000):
        count = 0
        for i in range(10):
            count += random.choice([0, 1])
        flips[count] += 1
    flips_dict = {index: num / 100 for index, num in enumerate(flips)}
    return flips_dict

# def draw_gaussian_distribution_graph(flips: dict) -> None:
#     x_points = np.array(list(flips.keys()))
#     y_points = np.array(list(flips.values()))
#     plt.plot(x_points, y_points)
#     plt.show()
