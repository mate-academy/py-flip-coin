import random


def flip_coin() -> dict[int: float]:
    heads_all_counts = {k: 0 for k in range(0, 11)}
    for _ in range(10000):
        heads_count = [random.randint(0, 1) for _ in range(0, 10)].count(1)
        heads_all_counts[heads_count] += 1
    for key, value in heads_all_counts.items():
        heads_all_counts[key] = value / 100
    return heads_all_counts


def draw_gaussian_distribution_graph() -> None:
    import matplotlib.pyplot as plt
    import numpy as np

    coins = flip_coin()
    xpoints = np.array(list(coins.keys()))
    ypoints = np.array([round(x, 2) for x in list(coins.values())])

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.ylim([0, 100])
    plt.xlim([0, 10])

    plt.plot(xpoints, ypoints)
    plt.xticks(range(11))
    plt.yticks(range(0, 101, 10))
    plt.show()
