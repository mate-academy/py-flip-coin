import random
import numpy as np
import matplotlib.pyplot as plt


def flip_coin(num_cases: int = 10000, num_flips: int = 10) -> dict:
    results = {i: 0 for i in range(num_flips + 1)}

    for _ in range(num_cases):
        heads = sum(random.randint(0, 1) for _ in range(num_flips))
        results[heads] += 1

    percentages = {
        key: (value / num_cases) * 100
        for key, value in results.items()
    }

    return percentages


def draw_gaussian_distribution_graph() -> None:
    koord_x = np.array(list(flip_coin().keys()))
    koord_y = np.array(list(flip_coin().values()))

    plt.plot(koord_x, koord_y)

    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")

    plt.show()
