from typing import Callable


import numpy as np
import matplotlib.pyplot as plt
import random


def flip_coin() -> dict:
    coin = ["Heads", "Tails"]
    cases = [[random.choice(coin) for flip in range(10)]
             for case in range(10000)]

    zero = 0
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0
    ten = 0

    for case in cases:
        if coin[0] not in case:
            zero += 1
        elif case.count(coin[0]) == 1:
            one += 1
        elif case.count(coin[0]) == 2:
            two += 1
        elif case.count(coin[0]) == 3:
            three += 1
        elif case.count(coin[0]) == 4:
            four += 1
        elif case.count(coin[0]) == 5:
            five += 1
        elif case.count(coin[0]) == 6:
            six += 1
        elif case.count(coin[0]) == 7:
            seven += 1
        elif case.count(coin[0]) == 8:
            eight += 1
        elif case.count(coin[0]) == 9:
            nine += 1
        elif case.count(coin[0]) == 10:
            ten += 1

    heads_percentage = {
        0: round((zero / len(cases)) * 100, 2),
        1: round((one / len(cases)) * 100, 2),
        2: round((two / len(cases)) * 100, 2),
        3: round((three / len(cases)) * 100, 2),
        4: round((four / len(cases)) * 100, 2),
        5: round((five / len(cases)) * 100, 2),
        6: round((six / len(cases)) * 100, 2),
        7: round((seven / len(cases)) * 100, 2),
        8: round((eight / len(cases)) * 100, 2),
        9: round((nine / len(cases)) * 100, 2),
        10: round((ten / len(cases)) * 100, 2)
    }

    return heads_percentage


def draw_gaussian_distribution_graph(func: Callable) -> None:
    y_values = list(func().values())
    x_values = list(func().keys())

    x_axis = np.array(x_values)
    y_axis = np.array(y_values)

    plt.xlim(0, 10)
    plt.ylim(0, 100)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads Count")
    plt.ylabel("Drop percentage %")

    plt.plot(x_axis, y_axis)
    plt.show()


if __name__ == "__main__":
    print(flip_coin())
    draw_gaussian_distribution_graph(flip_coin)
