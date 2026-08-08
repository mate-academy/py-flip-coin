# from matplotlib import pyplot as plt

import random


def flip_coin() -> dict:
    heads_chances = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0,
                     5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0
                     }
    for i in range(6000):
        heads = 0
        for coin in range(10):
            if random.randint(0, 1) == 1:
                heads += 1
        heads_chances[heads] += 1

    for key in heads_chances:
        heads_chances[key] = (heads_chances[key] / 6000) * 100
    return heads_chances


# def draw_gaussian_distribution_graph() -> None:
#     heads_chances = flip_coin()
#     xpoints = heads_chances.keys()
#     ypoints = heads_chances.values()
#     plt.plot(xpoints, ypoints)
#     plt.show()
