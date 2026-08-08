import random
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


def flip_coin(trials: int = 10000, flips_per_trial: int = 10) -> dict:
    results = []

    for _ in range(trials):
        heads_count = sum(
            random.choice([0, 1])
            for _ in range(flips_per_trial)
        )
        results.append(heads_count)

    counts = Counter(results)
    percentages = {k: round(v / trials * 100, 2) for k, v in counts.items()}

    return percentages


def draw_gaussian_distribution_graph(statistic_data: dict) -> None:
    y_array = np.array([num for num in statistic_data.values()])
    x_array = np.array(list(statistic_data.keys()))

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.plot(x_array, y_array)
    plt.show()
