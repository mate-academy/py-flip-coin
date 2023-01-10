import random
import matplotlib.pyplot as plt
import numpy as np


def flip_10_times() -> int:
    head_count = 0
    for _ in range(1, 11):
        if random.choice(["head", "back"]) == "head":
            head_count += 1
    return head_count


def flip_coin() -> dict:
    res = {i: 0 for i in range(11)}
    for _ in range(10001):
        if flip_10_times() not in res:
            res[flip_10_times()] = 1
        res[flip_10_times()] += 1

    for keys, values in res.items():
        res[keys] = (values / 10000) * 100
    return res


def draw_gaussian_distribution_graph() -> None:
    dict_coin = flip_coin()
    dict_keys = []
    dict_values = []
    for keys, values in dict_coin.items():
        dict_keys.append(keys)
        dict_values.append(values)
    xpoints = np.array(dict_keys)
    ypoints = np.array(dict_values)

    plt.plot(xpoints, ypoints)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.show()
