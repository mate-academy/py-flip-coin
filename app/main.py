import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    count_0 = 0
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    count_6 = 0
    count_7 = 0
    count_8 = 0
    count_9 = 0
    count_10 = 0
    dict_with_result = {0: 0,
                        1: 0,
                        2: 0,
                        3: 0,
                        4: 0,
                        5: 0,
                        6: 0,
                        7: 0,
                        8: 0,
                        9: 0}
    for _ in range(10000):
        count_of_times_heads = 0
        for i in range(10):
            if random.randint(0, 1) == 0:
                count_of_times_heads += 1
        if count_of_times_heads == 0:
            count_0 += 1
        if count_of_times_heads == 1:
            count_1 += 1
        if count_of_times_heads == 2:
            count_2 += 1
        if count_of_times_heads == 3:
            count_3 += 1
        if count_of_times_heads == 4:
            count_4 += 1
        if count_of_times_heads == 5:
            count_5 += 1
        if count_of_times_heads == 6:
            count_6 += 1
        if count_of_times_heads == 7:
            count_7 += 1
        if count_of_times_heads == 8:
            count_8 += 1
        if count_of_times_heads == 9:
            count_9 += 1
        if count_of_times_heads == 10:
            count_10 += 1

    dict_with_result[0] = count_0 / 10000 * 100
    dict_with_result[1] = count_1 / 10000 * 100
    dict_with_result[2] = count_2 / 10000 * 100
    dict_with_result[3] = count_3 / 10000 * 100
    dict_with_result[4] = count_4 / 10000 * 100
    dict_with_result[5] = count_5 / 10000 * 100
    dict_with_result[6] = count_6 / 10000 * 100
    dict_with_result[7] = count_7 / 10000 * 100
    dict_with_result[8] = count_8 / 10000 * 100
    dict_with_result[9] = count_9 / 10000 * 100
    dict_with_result[10] = count_10 / 10000 * 100
    return dict_with_result


def draw_gaussian_distribution_graph(dict_with: dict) -> None:
    xpoints = np.array(list(dict_with.keys()))
    ypoints = np.array(list(dict_with.values()))
    plt.plot(xpoints, ypoints)
    plt.show()
