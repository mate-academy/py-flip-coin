from random import randint
# import matplotlib.pyplot as plt
# import numpy as np


def flip_coin() -> dict[int, float]:
    results = {i: 0 for i in range(11)}
    num_trials = 10000
    for _ in range(num_trials):
        heads_count = sum(randint(0, 1) for _ in range(10))
        results[heads_count] += 1
    results_percentage = {k: (v / num_trials) * 100
                          for k, v in results.items()}

    return results_percentage


# def draw_gaussian_distribution_graph(values: dict[int, float]) -> None:
#     x = np.array(list(values.keys()))
#     y = np.array(list(values.values()))
#     print(x)
#     print(y)
#     plt.xlim(0, 10)
#     plt.ylim(0, 100)
#     plt.xticks(np.arange(0, 11, 1))
#     plt.yticks(np.arange(0, 101, 10))
#     plt.plot(x, y)
#     plt.show()
