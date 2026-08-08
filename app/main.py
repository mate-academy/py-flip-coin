import random

import matplotlib.pyplot as plt
import numpy as np


def flip_coin(experiments: int = 10000) -> dict[int, float]:
    result = {i: 0.0 for i in range(11)}

    for _ in range(experiments):
        heads_quantity = 0

        for _ in range(10):
            if random.random() < 0.5:
                heads_quantity += 1

        result[heads_quantity] += 1

    for key in result:
        result[key] = round(
            (result[key] / experiments) * 100, 2
        )

    return result


def draw_gaussian_distribution_graph(
        distribution: dict[int, float]
) -> None:
    xpoints = np.array(list(distribution.keys()))
    ypoints = np.array(list(distribution.values()))

    plt.plot(
        xpoints,
        ypoints,
        color="magenta",
        linewidth=2.5,
        marker="o",
        markersize=6
    )

    plt.xlim(0, 10)
    plt.xticks(range(0, 11))

    plt.ylim(0, 100)
    plt.yticks(range(0, 110, 10))

    plt.xlabel("Heads count", fontsize=12)
    plt.ylabel("Drop percentage %", fontsize=12)
    plt.title("Gaussian distribution", fontsize=14)

    plt.grid(True, linestyle="--", alpha=0.6)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    draw_gaussian_distribution_graph(flip_coin())
