from random import randint
# import matplotlib.pyplot as plt
# import numpy as np


def flip_coin() -> dict:
    conducts_10000_flipping_a_coin = []
    for number in range(10000):
        coin_flip_10 = []
        for _ in range(10):
            coin_flip_10.append(randint(0, 1))
        conducts_10000_flipping_a_coin.append(sum(coin_flip_10))

    return {
        key : (
            conducts_10000_flipping_a_coin.count(key) * 100
        ) / len(conducts_10000_flipping_a_coin)
        for key in range(11)
    }


# def draw_gaussian_distribution_graph() -> None:
#     y_points = np.array([int(number) for number in flip_coin().values()])
#
#     plt.plot(y_points)
#     plt.show()
