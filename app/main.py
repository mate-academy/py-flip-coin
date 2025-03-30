import random
# import matplotlib.pyplot as plt
# import numpy as np


def flip_coin(
        num_trials: int = 10000,
        num_flips: int = 10
) -> dict:
    results = {i: 0 for i in range(num_flips + 1)}

    for _ in range(num_trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(num_flips))
        results[heads_count] += 1

    for key, value in results.items():
        results[key] = (value / num_trials) * 100

    return results

# def draw_gaussian_distribution_graph() -> None:
#     result = flip_coin()
#     x_label = np.array(list(result.keys()))
#     y_label = np.array(list(result.values()))
#
#     plt.plot(10, 100)
#     plt.plot(x_label, y_label)
#
#     plt.title("Gaussian distribution")
#     plt.xlabel("Heads count")
#     plt.ylabel("Drop percentage %")
#
#     plt.show()
