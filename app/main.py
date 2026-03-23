import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin():
    n = 20_000
    possibilities = dict()

    for _ in range(n):
        flips = [random.choice([0, 1]) for _ in range(10)]
        if sum(flips) not in possibilities:
            possibilities[sum(flips)] = 1
        else:
            possibilities[sum(flips)] += 1

    return {k: round(v / n * 100, 2)  for k, v in possibilities.items()}


def draw_gaussian_distribution_graph():
    data = flip_coin()

    x = sorted(data.keys())
    y = [data[k] for k in x]

    plt.plot(x, y, color='blue')

    plt.title("Coin Flip Distribution")
    plt.xlabel("Number of Heads (out of 10)")
    plt.ylabel("Probability %")

    plt.xticks([x for x in range(1, 11)])

    plt.legend()
    plt.grid(True)

    plt.show()
