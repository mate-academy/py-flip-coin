import random

# import matplotlib.pyplot as plt
# import numpy as np


def sort_dict(my_dict: dict) -> dict:
    return {k: my_dict[k] for k in sorted(my_dict)}


def percentage(my_dict: dict) -> dict:
    return {k: my_dict[k] / 100 for k in my_dict}


def flip_coin() -> dict:
    result_dict = {}
    for _ in range(10000):
        counter = 0
        for _ in range(10):
            if random.choice(["H", "T"]) == "H":
                counter += 1
        if counter in result_dict:
            result_dict[counter] += 1
        else:
            result_dict[counter] = 1
    return percentage(sort_dict(result_dict))


# def draw_gaussian_distribution_graph() -> None:
#     flip_coin_result = flip_coin()
#     flip_coin_keys = list(flip_coin_result.keys())
#     flip_coin_values = list(flip_coin_result.values())
#
#     x_points = np.array(flip_coin_keys)
#     y_points = np.array(flip_coin_values)
#     plt.grid(True)
#     plt.plot(x_points, y_points)
#     plt.xlabel("Heads count")
#     plt.ylim(0, 100)
#     plt.xticks(range(0, 11))
#     plt.ylabel("Drop percentage %")
#     plt.title("Gaussian distribution")
#     plt.show()
