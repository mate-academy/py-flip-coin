import random
from collections import Counter
import matplotlib.pyplot as plt

CASES_NUMBER = 10000
DROPS_IN_CASE = 10


def flip_coin() -> dict[int, float]:
    heads_count = Counter([
        len([True for _ in range(DROPS_IN_CASE) if random.random() > 0.5])
        for _ in range(CASES_NUMBER)
    ])

    heads_percentage = {
        head_drops: (happen_times / CASES_NUMBER) * 100
        for head_drops, happen_times in heads_count.items()
    }

    return heads_percentage


def draw_gaussian_distribution_graph() -> None:
    axis = plt.gca()
    axis.set_ylim(0, 100)
    axis.set_xlim(0, 10)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    heads_percentage = flip_coin()

    drops_percentage_points = [
        percentage for (_, percentage) in
        sorted(
            heads_percentage.items(),
            key=lambda heads_percentage_item: heads_percentage_item[0]
        )
    ]

    plt.plot(drops_percentage_points)
    plt.show()


if __name__ == "__main__":
    draw_gaussian_distribution_graph()
