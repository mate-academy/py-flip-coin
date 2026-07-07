import random

import matplotlib.pyplot as plt


def flip_coin(
              number_of_flips: int = 10, number_of_cases: int = 10000
        ) -> dict:
    results = {head_count: 0 for head_count in range(number_of_flips + 1)}

    for _ in range(number_of_cases):
        heads = sum(random.randint(0, 1) for _ in range(number_of_flips))
        results[heads] += 1

    return {
        head_count: count / number_of_cases * 100
        for head_count, count in results.items()
    }


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()

    plt.bar(list(distribution.keys()), list(distribution.values()))
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage of cases, %")
    plt.title("Gaussian distribution of coin flips")
    plt.show()


if __name__ == "__main__":
    draw_gaussian_distribution_graph()
