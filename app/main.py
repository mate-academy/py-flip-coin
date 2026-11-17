import random

import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    number_of_cases = 10_000
    results = {number_of_heads: 0 for number_of_heads in range(11)}

    for _ in range(number_of_cases):
        number_of_heads = sum(
            random.choice((0, 1)) for _ in range(10)
        )
        results[number_of_heads] += 1

    return {
        number_of_heads: count / number_of_cases * 100
        for number_of_heads, count in results.items()
    }


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()
    plt.plot(
        list(distribution.keys()),
        list(distribution.values()),
    )
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage of cases")
    plt.title("Distribution of heads in 10 coin flips")
    plt.show()
