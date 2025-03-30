from random import choice
# import matplotlib.pyplot as plt
# import numpy as np


def flip_coin() -> dict:
    coin_sides = ["head", "tail"]
    result_distribution = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
    }

    for i in range(10000):
        count = 0
        for _ in range(10):
            result = choice(coin_sides)
            if result == "head":
                count += 1
        result_distribution[count] += 1
    return {
        k: round(v / (sum(result_distribution.values())) * 100, 2)
        for k, v in result_distribution.items()
    }


# def draw_gaussian_distribution_graph() -> None:
#     data = flip_coin()
#     plt.xticks([i for i in range(11)])
#     plt.ylim(0, 100)
#     plt.yticks(range(0, 101, 10))
#     x_points, y_points = (
#         np.asarray([num for num in data.keys()]),
#         np.asarray([num for num in data.values()]),
#     )
#
#     plt.plot(x_points, y_points)
#     plt.xlabel("Heads count")
#     plt.ylabel("Drop percentage %")
#     plt.title("Gaussian distribution")
#     plt.show()
