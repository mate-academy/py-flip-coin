import random
# import matplotlib.pyplot as plt
# import numpy as np


def flip_coin() -> dict:
    results = {i: 0 for i in range(11)}
    num_trials = 10000
    num_flips = 10

    for _ in range(num_trials):
        heads_count = sum(random.choice([0, 1]) for _ in range(num_flips))
        results[heads_count] += 1

    for key, value in results.items():
        results[key] = (value / num_trials) * 100

    return results


# def draw_gaussian_distribution_graph(data):
#     keys = list(data.keys())
#     values = list(data.values())
#
#     xpoints = np.array(keys)
#     ypoints = np.array(values)
#
#     plt.plot(xpoints, ypoints)
#     plt.title("Gaussian distribution")
#     plt.xlabel("Head count")
#     plt.ylabel("Drop percentage %")
#
#     plt.show()
