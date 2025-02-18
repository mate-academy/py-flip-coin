import random
import matplotlib.pyplot as plt
import numpy as np


def flip_coin(num_flips: int = 10000, flip: int = 10) -> dict[int, float]:
    results = {i: 0 for i in range(flip + 1)}

    for _ in range(num_flips):
        heads_count = sum(random.choice([0, 1]) for _ in range(flip))
        results[heads_count] += 1
    for key in results:
        results[key] = round((results[key] / num_flips) * 100, 2)
    return results


def draw_gaussian_distribution_graph() -> None:
    flips = flip_coin()
    xpoints = np.array(list(flips.keys()))
    ypoints = np.array(list(flips.values()))
    plt.ylim(0, 100)
    plt.xlabel("flip_coin_head")
    plt.ylabel("chance %")
    plt.plot(xpoints, ypoints, marker="o", linestyle="-")
    return plt.show()


print(draw_gaussian_distribution_graph())
