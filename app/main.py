import random
from collections import Counter

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


def flip_coin(flips: int = 10001) -> dict:

    flips = [[random.choice([1, 0]) for _ in range(10)] for _ in range(flips)]
    count_ten_flips = [Counter(item) for item in flips]
    total_counts = Counter(head_coin[1] for head_coin in count_ten_flips)
    percent_flips = {
        head: round(value * 0.01, 2) for head, value in total_counts.items()
    }
    return dict(sorted(percent_flips.items()))


def draw_gaussian_distribution_graph() -> None:
    points = np.array(list(flip_coin().values()))

    _, ax = plt.subplots()

    ax.set(title="Gaussian distribution",
           xlabel="Heads count",
           ylabel="Drop percentage %",
           ylim=(0, 100),
           xlim=(0, 10),
           xticks=range(11))

    ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))

    ax.plot(points)

    plt.show()


def main() -> None:
    draw_gaussian_distribution_graph()


if __name__ == "__main__":
    main()
