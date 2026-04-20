import random
# from matplotlib import pyplot as plt
# import numpy as np


def flip_coin() -> dict:
    result: dict = {key: 0 for key in range(0, 11)}
    attempts = 10000
    while attempts != 0:
        true_counter = 0
        for flip in range(1, 11):
            if random.choice([True, False]) is True:
                true_counter += 1
        result[true_counter] += 1
        attempts -= 1
    return {key: result[key] / 100 for key in result.keys()}


# def draw_gaussian_distribution_graph(dat_dict: dict) -> None:
#     xpoints = np.array([k for k in dat_dict.keys()])
#     ypoints = np.array([v[1] for v in dat_dict.items()])
#     print([v[1] for v in dat_dict.items()])
#     plt.plot(xpoints, ypoints)
#     plt.show()
