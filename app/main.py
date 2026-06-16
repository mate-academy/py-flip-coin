import random
# from matplotlib import pyplot as plt
# import numpy as np


def flip_coin() -> dict:
    dict_coins_cases = {num: 0 for num in range(11)}
    for _ in range(10000):
        count = 0
        for _ in range(10):
            num_random = random.randint(0, 1)
            if num_random == 1:
                count += 1
        dict_coins_cases[count] += 1
    return {key: value / 100 for key, value in dict_coins_cases.items()}


# def draw_gaussian_distribution_graph(distribution: dict) -> None:
#     xpoints = np.array([x for x in range(11)])
#     ypoints = np.array([y for y in distribution.values()])
#     plt.title("Gaussian distribution")
#     plt.xlabel("Heads count")
#     plt.ylabel("Drop percentage, %")
#     plt.plot(xpoints, ypoints)
#     plt.show()
