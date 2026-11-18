import random

import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    cases = 10_000
    heads_frequency = {heads: 0 for heads in range(11)}

    for _ in range(cases):
        heads = 0

        for _ in range(10):
            if random.choice(("heads", "tails")) == "heads":
                heads += 1

        heads_frequency[heads] += 1

    return {
        heads: count / cases * 100
        for heads, count in heads_frequency.items()
    }


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()

    heads_numbers = list(distribution.keys())
    percentages = list(distribution.values())

    plt.plot(heads_numbers, percentages, marker="o")
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage")
    plt.title("Coin Toss Distribution")
    plt.xticks(heads_numbers)
    plt.show()
