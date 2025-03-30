# import sys
import random
# import matplotlib
# import matplotlib.pyplot as plt
# import numpy as np
#
#
# # matplotlib.use("Agg")


def flip_coin() -> dict:
    results = {i: 0 for i in range(10 + 1)}

    cases_count = 10000

    for _ in range(cases_count):
        heads_count = sum(random.choice([0, 1]) for _ in range(10))
        results[heads_count] += 1

    for key in results:
        results[key] = (results[key] / cases_count) * 100

    return results


# coin_dict = flip_coin()
#
#
# def draw_gaussian_distribution_graph() -> None:
    # xpoints = np.array([key for key in coin_dict.keys()])
    # ypoints = np.array([value for value in coin_dict.values()])
#
    # font1 = {"family": "serif", "color": "blue", "size": 20}
    # font2 = {"family": "serif", "color": "darkred", "size": 15}
#
    # plt.title("Gaussian distribution", fontdict=font1)
    # plt.xlabel("Heads count", fontdict=font2)
    # plt.ylabel("Drop persceintage %", fontdict=font2)
#
    # plt.plot(xpoints, ypoints)
    # plt.show()
#
    # plt.savefig(sys.stdout.buffer)
    # sys.stdout.flush()
#
#
# draw_gaussian_distribution_graph()
