import random

import matplotlib.pyplot as plt


def flip_coin(num: int = 10000) -> dict:
    head_counts = {i: 0 for i in range(10 + 1)}
    for _ in range(num):

        heads_in_this_case = 0

        for _ in range(10):

            if random.random() < 0.5:
                heads_in_this_case += 1

        head_counts[heads_in_this_case] += 1

    results_in_percentage = {}
    for count, frequency in head_counts.items():

        percentage = round((frequency / num) * 100, 2)
        results_in_percentage[count] = percentage

    return results_in_percentage


def draw_graph(results_in_percentage: dict) -> None:
    x_coord = sorted(results_in_percentage.keys())
    y_coord = [results_in_percentage[k] for k in x_coord]
    plt.bar(x_coord, y_coord)
    plt.xlabel("Number of heads")
    plt.title("Distribution of heads in 10 coin flips")
    plt.savefig("distribution.png")
    plt.show()


draw_graph(results_in_percentage=flip_coin(10000))
