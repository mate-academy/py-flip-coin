import random
# import matplotlib.pyplot as plt
# import numpy as np


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


# def draw_gaussian_distribution_graph(results: dict) -> None:
#     heads = list(results.keys())
#     percentages = list(results.values())
#
#     plt.plot(heads, percentages, color="b")
#
#     plt.title("Gaussian distribution")
#     plt.xlabel("Heads count")
#     plt.ylabel("Drop percentage %")
#     plt.xticks(np.arange(0, 11, step=1))
#     plt.yticks(np.arange(0, 101, step=10))
#     plt.xlim(0, 10)
#     plt.ylim(0, 100)
#     plt.show()
