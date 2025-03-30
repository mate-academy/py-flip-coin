from random import randint
# import matplotlib.pyplot as plt
# import numpy as np


def flip_coin() -> dict:
    flip_results = []
    results_of_flipping_heads = {}
    for _ in range(10000):
        flip_coin_10_times = [randint(0, 1) for _ in range(10)]
        flip_results.append(flip_coin_10_times.count(1))
    for i in range(11):
        results_of_flipping_heads[i] = round(flip_results.count(i) / 100, 2)
    return results_of_flipping_heads


# def draw_gaussian_distribution_graph() -> None:
#     result_of_flipping = flip_coin()
#     x_point = np.array([key for key in result_of_flipping.keys()])
#     y_point = np.array([value for value in result_of_flipping.values()])
#
#     plt.plot(x_point, y_point)
#     plt.title("Gaussian distribution")
#     plt.xlabel("Heads count")
#     plt.ylabel("Drop percentage %")
#     plt.show()
