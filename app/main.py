import matplotlib.pyplot as plt
import numpy as np
import random as rnd


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}
    total_cases = 10000

    for i in range(total_cases):
        flips = []
        for j in range(0, 10):
            flips.append(rnd.choice([0, 1]))
        heads_count = sum(flips)
        results[heads_count] += 1

    for k in results:
        results[k] = round((results[k] / total_cases) * 100, 2)

    return results


def draw_gaussian_distribution_graph(results: dict) -> None:
    x = np.array(results.keys())
    y = np.array(results.values())
    plt.plot(x, y)

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage")

    plt.show()
