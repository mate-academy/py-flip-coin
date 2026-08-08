import random

from matplotlib import pyplot as plt


def flip_coin() -> dict:
    stats = {}
    results = []
    for _ in range(10000):
        heads = sum(random.randint(0, 1) for _ in range(10))
        results.append(heads)

    for i in range(11):
        stats[i] = round(results.count(i) / 100, 2)

    return stats


def draw_gaussian_distribution_graph() -> None:
    xdot = flip_coin().keys()
    ydot = flip_coin().values()

    plt.xlim(0, 10)
    plt.ylim(0, 100)

    plt.title("Gaussian Distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.xticks(range(11))
    plt.yticks(range(0, 101, 10))

    plt.plot(xdot, ydot)
    plt.show()
