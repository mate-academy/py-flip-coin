from random import choice
# import matplotlib.pyplot as plt
# import numpy as np


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}

    for _ in range(10000):
        heads = sum(choice([0, 1]) for _ in range(10))
        results[heads] += 1

    for key in results:
        results[key] = round((results[key] / 10000) * 100, 2)

    return results


# def draw_gaussian_distribution_graph() -> None:
#     xpoints = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#     ypoints = np.array([
#         0.13, 0.97, 4.22, 12.04, 20.51, 24.61,
#         20.51, 12.04, 4.22, 0.97, 0.13
#     ])
#     plt.plot(xpoints, ypoints)
#     plt.show()
