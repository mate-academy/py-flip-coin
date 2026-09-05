import random

import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    cases = 10000
    heads_count = {heads: 0 for heads in range(11)}

    for _ in range(cases):
        heads = 0

        for _ in range(10):
            if random.choice([True, False]):
                heads += 1

        heads_count[heads] += 1

    return {
        heads: round(
            count / cases * 100,
            2,
        )
        for heads, count in heads_count.items()
    }


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()

    plt.bar(
        distribution.keys(),
        distribution.values(),
    )

    plt.xlabel("Number of heads")
    plt.ylabel("Percentage")
    plt.title("Coin Toss Distribution")

    plt.show()
