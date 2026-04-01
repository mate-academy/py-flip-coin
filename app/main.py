from random import choice
# import matplotlib.pyplot as plt
# import numpy as np


def flip_coin() -> dict:
    flips_number = 10
    iteration_number = 10000
    flips_dict = dict((i, 0) for i in range(flips_number + 1))
    for i in range(iteration_number):
        flips_dict[sum([choice([1, 0]) for i in range(10)])] += 1
    for key in flips_dict.keys():
        flips_dict[key] = round(flips_dict[key] * 100 / iteration_number, 2)
    return flips_dict


# def draw_gaussian_distribution_graph() -> None:
#
#     data = flip_coin()
#     x_np = np.array([x_ for x_ in data.keys()])
#     y_np = np.array([y_ for y_ in data.values()])
#     plt.plot(x_np, y_np)
#     plt.title("Gaussian distribution curve")
#     plt.xlabel("Heads Count")
#     plt.ylabel("Drop percentage, %")
#     plt.show()
