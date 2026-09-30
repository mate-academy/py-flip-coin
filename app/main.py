import random

import matplotlib.pyplot as plt


def flip_once() -> int:
    return random.randint(0, 1)


def count_flips() -> int:
    count = 0
    for _ in range(10):
        flip = flip_once()
        if flip == 1:
            count += 1
    return count


def flip_coin() -> dict[int, float]:
    flips = 10
    cases = 10000
    results = {i: 0 for i in range(flips + 1)}
    for _ in range(cases):
        heads = count_flips()
        results[heads] += 1
    for key in results:
        results[key] = round(results[key] / cases * 100, 2)
    return results


def draw_gaussian_distribution_graph() -> None:
    distribution = flip_coin()
    plt.title("Gaussian distribution")
    plt.plot((distribution.keys()), (distribution.values()))
    plt.xlabel("Number of heads")
    plt.ylabel("Percentage of cases")
    plt.show()


draw_gaussian_distribution_graph()
