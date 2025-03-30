import random
# import matplotlib.pyplot as plt
# import numpy as np


def flip_coin() -> dict:
    results = {}

    for _ in range(10000):
        heads_count = 0

        for _ in range(10):
            if random.random() < 0.5:
                heads_count += 1

        if heads_count in results:
            results[heads_count] += 1
        else:
            results[heads_count] = 1

    results = dict(sorted(results.items()))
    for key in results:
        results[key] = round((results[key] / 10000) * 100, 2)

    return results


# def draw_gaussian_distribution_graph(results: dict) -> None:
#     list_of_keys = [key for key in results]
#     list_of_values = [value for value in results.values()]
#
#     x_coordinates = np.array(list_of_keys)
#     y_coordinates = np.array(list_of_values)
#
#     plt.plot(x_coordinates, y_coordinates)
#
#     plt.xlabel("Frequency")
#     plt.ylabel("Percents")
#
#     plt.show()
