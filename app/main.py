import random

import matplotlib.pyplot as plt


def flip_coin() -> dict[int, float]:
    cases = 10000
    distribution = {heads: 0 for heads in range(11)}

    for _ in range(cases):
        heads_count = 0

        for _ in range(10):
            if random.choice([True, False]):
                heads_count += 1

        distribution[heads_count] += 1

    for heads_count in distribution:
        distribution[heads_count] = round(
            distribution[heads_count] / cases * 100,
            2,
        )

    return distribution


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()

    heads_counts = list(distribution.keys())
    drop_percentages = list(distribution.values())

    plt.plot(heads_counts, drop_percentages)
    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.xticks(range(11))
    plt.xlim(0, 10)
    plt.ylim(0, 100)

    plt.show()
