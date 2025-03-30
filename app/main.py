import random
# import matplotlib.pyplot as plt
# import numpy as np


def flip_coin() -> dict:
    try_num = 0
    count_dict = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0
    }

    for i in range(10000):

        count_rand = 0
        for try_num in range(10):
            random_number = random.randint(0, 1)
            count_rand += random_number
        count_dict[count_rand] += 1

    for key, value in count_dict.items():
        count_dict[key] = (value / 100)

    return count_dict

#
# def draw_gaussian_distribution_graph(count_dict: dict) -> None:
#     xpoints = np.array(list(count_dict.keys()))
#     ypoints = np.array(list(count_dict.values()))
#
#     plt.plot(xpoints, ypoints)
#     plt.show()
