import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin(n_flips: int = 10, n_cases: int = 100_000):
    list_zero = []
    for _ in range(n_cases):
        count = 0
        for count_up in range(n_flips):
            number = random.randint(0, 1)
            if number == 1:
                count += 1
        list_zero.append(count)

    dict_result = {}
    for counts in range(11):
        zero_one = list_zero.count(counts)
        interest = round((zero_one / n_cases) * 100, 2)
        dict_result[counts] = interest
    return dict_result


def draw_gaussian_distribution_graph(dict_result):
    x = np.array(list(dict_result.keys()))
    y = np.array(list(dict_result.values()))

    plt.plot(x, y, marker='o')

    plt.xlabel("Number of heads")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution of coin flips")
    plt.grid(True)
    plt.show()

