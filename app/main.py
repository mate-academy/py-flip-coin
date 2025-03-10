import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict[int, float]:
    coin_outcomes = [0, 1]
    heads_count: dict[int, int] = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
                                   6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for experiment_index in range(10000):
        num_heads: int = 0
        for flip_index in range(10):
            flip_result = random.choice(coin_outcomes)
            if flip_result == 1:
                num_heads += 1
        heads_count[num_heads] += 1
    for i in range(11):
        heads_count[i] = round((heads_count[i] / 10000) * 100, 2)
    return heads_count


# def draw_gaussian_distribution_graph(distribution: dict[int, float]) -> None:
#     heads_values = []
#     percentages = []
#     for key, value in distribution.items():
#         heads_values.append(key)
#         percentages.append(value)
#     x_coordinates = np.array(heads_values)
#     y_coordinates = np.array(percentages)
#
#     plt.plot(x_coordinates, y_coordinates)
#     plt.show()
