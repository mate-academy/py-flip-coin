import random
# import matplotlib.pyplot as plt
# import numpy as np


def flip_coin() -> dict:
    result = {number: 0 for number in range(0, 11)}
    coin_sides = ["Heads", "Tails"]

    for case in range(10000):
        flip_result = 0

        for flip in range(10):
            if random.choice(coin_sides) == "Heads":
                flip_result += 1

        result[flip_result] = round(result[flip_result] + 0.01, 2)

    return result


# def draw_gaussian_distribution_graph(result: dict) -> None:
#     heads_count = list(result.keys())
#     percentage = list(result.values())
#
#     x_point = np.array(heads_count)
#     y_point = np.array(percentage)
#
#     plt.plot(x_point, y_point)
#
#     plt.xlabel("Heads count")
#     plt.ylabel("Drop percentage, %")
#
#     plt.show()
