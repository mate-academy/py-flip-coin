import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    counts = {}
    for case in range(10000):
        heads = 0
        for attempt in range(10):
            if random.randint(0, 1) == 0:
                heads += 1
        counts[heads] = counts.get(heads, 0) + 1
    for count in counts:
        counts[count] = counts[count] / 10000 * 100
    counts = dict(sorted(counts.items()))
    return counts


results = flip_coin()


def draw_gaussian_distribution_graph(results: dict) -> None:
    x_axis = list(results.keys())
    y_axis = list(results.values())
    plt.plot(x_axis, y_axis)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.ylim(0, 100)
    plt.show()
