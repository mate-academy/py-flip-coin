import random

import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    trials = 10000
    coins = 10
    results = {heads: 0 for heads in range(coins + 1)}

    for _ in range(trials):
        heads = 0
        for _ in range(coins):
            heads += random.randint(0, 1)
        results[heads] += 1

    return {
        heads: round((count / trials) * 100, 2)
        for heads, count in results.items()
    }


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    heads_count = list(data.keys())
    percentages = list(data.values())

    plt.plot(heads_count, percentages)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage, %")
    plt.show()