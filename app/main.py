import random
import numpy as np
import matplotlib.pyplot as plt


no_of_rounds = 10000
no_of_flips = 10


def flip_coin() -> dict:
    # setup empty results dictionary
    results = {}

    # init results 0 to no_of_flips (inclusive) heads to 0
    for i in range(no_of_flips + 1):
        results[i] = 0

    # repeat tests no_of_rounds times
    for _ in range(no_of_rounds):
        # start round of no_of_flips flips
        # record number of heads, 0 = head, 1 = tail
        count_heads = 0
        for _ in range(no_of_flips):
            if random.randint(0, 1) == 0:
                count_heads += 1

        # update results
        results[count_heads] += 1

    # calculate results as percentages
    for i in range(no_of_flips + 1):
        results[i] = round(results[i] / 10000 * 100, 2)

    return results


def draw_gaussian_distribution_graph(heads_count: dict) -> None:
    x_values = heads_count.keys()
    y_values = heads_count.values()

    plt.plot(x_values, y_values)

    plt.xlabel("Heads count")
    plt.ylabel("Drop percetnage %")
    plt.title("Gaussian distribution")
    plt.ylim(0, 100)
    plt.yticks(np.arange(0, 101, 10))
    plt.xlim(0, no_of_flips)
    plt.xticks(np.arange(0, no_of_flips + 1, 1))

    plt.show()
