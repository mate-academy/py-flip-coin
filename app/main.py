import random

import matplotlib.pyplot as plt


def flip_coin(num_of_flips: int = 10,
              num_of_cases: int = 10000) -> dict:
    heads_count = {number: 0 for number in range(num_of_flips + 1)}

    for _ in range(num_of_cases):
        heads = sum(random.randint(0, 1) for _ in range(num_of_flips))
        heads_count[heads] += 1

    return {
        heads: round(count / num_of_cases * 100, 2)
        for heads, count in heads_count.items()
    }


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()

    plt.plot(list(distribution.keys()), list(distribution.values()))
    plt.title("Gaussian Distribution of Coin Flips")
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage of cases, %")
    plt.show()
