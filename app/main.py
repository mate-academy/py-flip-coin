import matplotlib.pyplot as plt
import random


def flip_coin() -> dict:
    heads_list = []

    for i in range(10000):
        heads = 0

        for _ in range(10):
            if random.choice(("heads", "tails")) == "heads":
                heads += 1
        heads_list.append(heads)

    return {i: round(heads_list.count(i) * 100 / 10000, 2)
            for i in range(11)
            }


def draw_gaussian_distribution_graph() -> None:
    plt.plot(flip_coin().keys(), flip_coin().values())
    plt.show()
