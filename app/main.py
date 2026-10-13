import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    tails = 0
    eagle = 1
    result_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0,
                   5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for _ in range(10000):
        flip_coin_10_times = [random.randint(tails, eagle)
                              for _ in range(10)]
        index = flip_coin_10_times.count(eagle)
        result_dict[index] += 1
    for key, value in result_dict.items():
        result_dict[key] = value / 100
    return result_dict


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()
    plt.xticks(range(0, 11))
    plt.yticks(range(0, 101, 10))
    plt.ylim(0, 100)

    plt.plot(list(distribution), list(distribution.values()))

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage")

    plt.show()
