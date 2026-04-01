import random
# import matplotlib.pyplot as plt
# import numpy as np


def flip_coin() -> dict:
    result = {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0
    }
    coin_sides = [0, 1]

    for _ in range(10000):
        count_1 = 0
        for _ in range(10):
            if random.choice(coin_sides) == 1:
                count_1 += 1
        result[count_1] = round(result[count_1] + 0.01, 2)

    return result

# def draw_gaussian_distribution_graph(date: dict) -> None:
#     x_points = np.array(list(date.keys()))
#     y_points = np.array(list(date.values()))
#
#     plt.plot(x_points, y_points)
#
#     plt.title("Head count")
#     plt.xlabel("Number of heads up")
#     plt.ylabel("Percentage of 10,000 attempts")
#     plt.show()
