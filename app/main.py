# import numpy as np
# import matplotlib.pyplot as plt
from random import choice


def flip_10_times() -> int:
    count = 0
    for _ in range(10):
        if choice(["hand", "tail"]) == "hand":
            count += 1
    return count


def flip_coin() -> dict:
    dict_ = dict.fromkeys(range(11), 0)
    for _ in range(10000):
        dict_[flip_10_times()] += 1
    print(sum(dict_.values()))
    return {key: value / 100 for key, value in dict_.items()}


# def draw_gaussian_distribution_graph(flips: dict) -> None:
#     xpoints = np.array(list(flips.keys()))
#     ypoints = np.array(list(flips.values()))
#     plt.ylim([0, 100])
#     plt.xlim([0, 10])
#     plt.plot(xpoints, ypoints)
#     plt.title("Gaussian distribution")
#     plt.xlabel("Heads count")
#     plt.ylabel("Drop percentage %")
#     plt.show()
