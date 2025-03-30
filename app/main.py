import random
# import numpy as np
# from matplotlib import pyplot


def flip_coin(iterations: int = 10000, flips: int = 10) -> dict:
    statistics = {i: 0 for i in range(flips + 1)}

    for _ in range(iterations):
        counter = 0
        for flip in range(0, 10):
            if random.choice(["Heads", "Tails"]) == "Heads":
                counter += 1
        statistics[counter] += 1

    for key, value in statistics.items():
        statistics[key] = round(value / iterations * 100, 2)

    return statistics


# def draw_gaussian_distribution_graph(statistics: dict) -> None:
#     x_list = []
#     y_list = []
#     for i in range(len(statistics)):
#         x_list.append(i)
#         y_list.append(statistics[i])
#
#     x_axis = np.array(x_list)
#     y_axis = np.array(y_list)
#
#     pyplot.plot(x_axis, y_axis)
#     pyplot.ylim(0, 100)
#     pyplot.xlim(0, 10)
#
#     pyplot.title("Gaussian distribution")
#     pyplot.xlabel("Heads count")
#     pyplot.ylabel("Drop Percentage %")
#
#     pyplot.show()
