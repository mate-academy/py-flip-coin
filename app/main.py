import random

import matplotlib.pyplot as plt


def flip_coin() -> dict:
    total = 10000
    counts = {i: 0 for i in range(11)}

    for _ in range(total):
        heads = sum(random.randint(0, 1) for _ in range(10))
        counts[heads] += 1

    return {k: (v / total) * 100 for k, v in counts.items()}


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    plt.plot(list(data.keys()), list(data.values()))
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.show()
