import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> None:
    my_dict = {}
    for _ in range(10000):
        count = 0
        for _ in range(10):
            res = random.randint(0, 1)
            if res == 0:
                count += 1
        if count not in my_dict:
            my_dict[count] = 1
        else:
            my_dict[count] += 1
    for key in my_dict.keys():
        my_dict[key] = my_dict[key] / 10000 * 100
    return my_dict


def draw_gaussian_distribution_graph(my_dict: dict) -> None:
    values = []
    keys_dict = []
    new_dict = dict(sorted(my_dict.items()))
    for key, value in new_dict.items():
        values.append(value)
        keys_dict.append(key)
    xpoints = np.array(keys_dict)
    ypoints = np.array(values)
    plt.plot(xpoints, ypoints)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.show()
