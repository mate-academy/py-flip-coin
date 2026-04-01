# from matplotlib import pyplot
# import numpy as np
from random import random


# def draw_gaussian_distribution_graph(arr: dict) -> None:
#     xpoints = np.array(range(11))
#     ypoints = np.array([num for num in arr.values()])
#     pyplot.plot(xpoints, ypoints)
#     pyplot.xlabel("Heads count")
#     pyplot.ylabel("Drop percantage %")
#     ax = pyplot.gca()
#     ax.set_ylim([0, 100])
#     pyplot.show()


def flip_coin() -> dict:
    flips = [[1 if random() < 0.5 else 0 for num in range(10)]
             for i in range(10000)]
    results = {
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
        10: 0
    }
    for result in flips:
        results[result.count(1)] += 1
    for key, value in results.items():
        results[key] = round((value / 10000) * 100, 2)
    return results
