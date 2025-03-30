import random
# import numpy as np
# import matplotlib.pyplot as plt


def flip_coin() -> dict:
    coin_side = ["heads", "tails"]
    result_dict = {}
    for i in range(10000):
        list_of_flips = []
        for _ in range(10):
            list_of_flips.append(random.choice(coin_side))
        for key in range(11):
            if list_of_flips.count("heads") == key:
                if key in result_dict.keys():
                    result_dict[key] += 0.01
                    result_dict[key] = round(result_dict[key], 2)
                else:
                    result_dict[key] = 0.01
    result_dict_sorted = dict(sorted(result_dict.items()))
    return result_dict_sorted


# def draw_gaussian_distribution_graph() -> None:
#     x_points = np.array(list(flip_coin().keys()))
#     y_points = np.array(list(flip_coin().values()))
#
#     plt.plot(x_points, y_points)
#
#     plt.title("Gaussian distribution")
#     plt.xlabel("Heads count")
#     plt.ylabel("Drop percentage %")
#
#     plt.ylim(0, 100)
#
#     plt.show()
