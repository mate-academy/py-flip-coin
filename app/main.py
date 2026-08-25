import random
from typing import Dict

import matplotlib.pyplot as plt

TRIALS = 10000
FLIPS_PER_TRIAL = 10


def flip_coin() -> Dict[int, float]:
    results_count = {i: 0 for i in range(FLIPS_PER_TRIAL + 1)}

    for _ in range(TRIALS):
        # random.choices повертає список із 10 випадкових 0 або 1
        heads_count = sum(random.choices([0, 1], k=FLIPS_PER_TRIAL))
        results_count[heads_count] += 1

    return {
        heads: round((count / TRIALS) * 100, 2)
        for heads, count in results_count.items()
    }


def draw_gaussian_distribution_graph() -> None:
    data = flip_coin()
    x_coords = list(data.keys())
    y_coords = list(data.values())

    plt.plot(x_coords, y_coords)
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.title("Gaussian distribution")
    plt.ylim(0, 100)
    plt.show()
