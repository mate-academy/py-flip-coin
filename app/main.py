import random
# from matplotlib import pyplot as plt
# import numpy as np


def flip_coin(cases: int = 10000) -> dict:
    result = {num: 0 for num in range(0, 11)}

    for _ in range(cases):
        num = sum(random.randint(0, 1) for _ in range(10))
        result[num] += 1

    for key, value in result.items():
        result[key] = value / 100

    return result

# def draw_gaussian_distribution_graph(result: dict) -> object:
#     x_list = []
#     y_list = []

    # for key, value in result.items():
    #     x_list.append(key)
    #     y_list.append(value)
    # xpoints = np.array(x_list)
    # ypoints = np.array(y_list)
    #
    #
    # matplotlib.plot(xpoints, ypoints)
    # plt.title("Gaussian distribution")
    # plt.xlabel("Heads count")
    # plt.ylabel("Drop percentage %")
    # plt.show()
