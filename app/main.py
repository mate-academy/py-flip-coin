import random

# import matplotlib.pyplot as plt
# import numpy as np


def flip_coin() -> dict:
    result = {x: 0 for x in range(11)}
    sum_values = 0

    for _ in range(10000):
        while True:
            count_flip = random.gauss(5, 5 / 3)
            if 0 <= count_flip <= 11:
                break
        result[int(count_flip)] += count_flip
        sum_values += count_flip

    return {i: round((result[i] / sum_values) * 100, 2) for i in range(11)}


# def draw_gaussian_distribution_graph() -> None:
#     list_x = []
#     list_y = []
#     for key, value in flip_coin().items():
#         list_x.append(key)
#         list_y.append(round(value))
#
#     xpoints = np.array(list_x)
#     ypoints = np.array(list_y)
#
#     plt.plot(xpoints, ypoints)
#
#     plt.title("Gaussian distribution")
#     plt.xlabel("Number of flip in 0 to 10")
#     plt.ylabel("Drop percentage %")
#     plt.show()
