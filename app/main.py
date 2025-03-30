# import matplotlib.pyplot as plt
# import numpy as np
import random


def flip_coin() -> dict:
    flip_dict = {0: 0,
                 1: 0,
                 2: 0,
                 3: 0,
                 4: 0,
                 5: 0,
                 6: 0,
                 7: 0,
                 8: 0,
                 9: 0,
                 10: 0}
    coin = ["head", "tail"]
    for time in range(10000):
        value = 0
        for flip in range(10):
            if random.choice(coin) == "head":
                value += 1
        if value in flip_dict:
            flip_dict[value] += 1

    return {key: value / 100 for key, value in flip_dict.items()}
#
#
# def draw_gaussian_distribution_graph():
#     values_dict = flip_coin()
#     values_list = list(values_dict.values())
#     ypoints = np.array(values_list)
#
#     plt.plot(ypoints)
#     plt.show()
