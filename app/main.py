import random
# import numpy as np
# import matplotlib.pyplot as plt


def flip_coin() -> dict:
    cases_of_flipping = 10000
    result = {0: 0}
    head_amount = 0

    while cases_of_flipping > 0:
        for i in range(1, 11):
            if i not in result:
                result[i] = 0
            if random.randint(0, 1) == 1:
                head_amount += 1

        result[head_amount] += 1
        head_amount = 0
        cases_of_flipping -= 1

    for key in result.keys():
        result[key] = result[key] / 100

    return result


# data_1 = flip_coin()
#
#
# def draw_gaussian_distribution_graph(data: dict) -> None:
#
#     xpoints = np.array([key for key in data.keys()])
#     ypoints = np.array([value for value in data.values()])
#
#     font1 = {"family": "serif", "color": "blue", "size": 20}
#     font2 = {"family": "serif", "color": "darkred", "size": 15}
#
#     plt.title("Gaussian distribution", fontdict=font1)
#     plt.xlabel("Heads count", fontdict=font2)
#     plt.ylabel("Drop percentage %", fontdict=font2)
#
#     plt.plot(xpoints, ypoints)
#     plt.show()
#
#
# draw_gaussian_distribution_graph(data_1)
