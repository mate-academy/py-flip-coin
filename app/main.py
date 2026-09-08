import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin() -> dict:
    probability_of_head = {}
    amount_of_head = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0
    }

    for i in range(10000):
        head_count = 0

        for toss in range(10):
            result_of_toss = random.randint(0, 1)
            if result_of_toss == 1:
                head_count += 1

        amount_of_head[head_count] += 1

    for result, amount in amount_of_head.items():
        probability_of_head[result] = amount / 10000 * 100

    return probability_of_head


def draw_gaussian_distribution_graph(heads: dict) -> None:

    xpoints = np.array(list(heads.keys()))
    ypoints = np.array(list(heads.values()))

    plt.plot(xpoints, ypoints)

    plt.title("Gaussian Distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
