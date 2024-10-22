from __future__ import annotations
import random

import numpy as np
import matplotlib.pyplot as plt


def flip_coin() -> dict:
    list_res = []
    dict_of_res = {}
    for _ in range(10000):
        what_can_be = ["head", "not head"]
        one_of_circle = 0
        for _ in range(10):
            res_of_flip = random.choice(what_can_be)
            if res_of_flip == "head":
                one_of_circle += 1
        list_res.append(one_of_circle)

    for number in range(11):
        dict_of_res[number] = round((list_res.count(number) / 10000 * 100), 2)

    return dict_of_res


def draw_gaussian_distribution_graph(dict_for_grafik: dict) -> None:
    list_of_keys = [key for key in dict_for_grafik]
    list_of_meaning = [dict_for_grafik[key] for key in dict_for_grafik]

    x_points = np.array(list_of_keys)
    y_points = np.array(list_of_meaning)

    plt.plot(x_points, y_points)
    plt.xlabel("Count of heads")
    plt.ylabel("%")
    plt.show()
