import matplotlib.pyplot as plt
import random


def flip_coin() -> dict:
    dict_res = {}
    for _ in range(10000):
        count = 0
        for i in range(10):
            result = random.randint(0, 1)
            if result == 1:
                count += 1
        if count in dict_res:
            dict_res[count] += 1
        else:
            dict_res[count] = 1

    full = dict(sorted(dict_res.items()))

    for key, value in full.items():
        full[key] = (full[key] / 10000) * 100

    return full


def draw_gaussian_distribution_graph(full: dict) -> None:
    x_arr = []
    y_arr = []
    for key, value in full.items():
        y_arr.append(full[key])
        x_arr.append(key)
    plt.plot(x_arr, y_arr)
    plt.show()
