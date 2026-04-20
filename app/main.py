import random
# import matplotlib.pyplot as plt
# import numpy as np


def flip_coin(trials: int = 10000, flips_per_trial: int = 10) -> dict:
    # here we initialize the dict with keys from 0 to 10 with all values
    # equal to 0, this considered as a initial state of the dict, and we
    # will add the values every single iteration up to 10000
    flip_dict = {i: 0 for i in range(flips_per_trial + 1)}

    # we make general loop with 10000 iterations and every iteration
    # we count how many heads we have if we flip our coin 10 times
    for _ in range(trials):
        # here we put
        heads_count = 0
        for i in range(flips_per_trial):
            heads_count += random.choice([0, 1])
            # here we add by the key we get in a single iteration one point

        flip_dict[heads_count] += 1

    flip_dict = {
        key: round(value / trials * 100, 2) for key, value in flip_dict.items()
    }
    return flip_dict


# def draw_gaussian_distribution_graph(flip_dict: dict) -> None:
#     xpoints = np.array(list(flip_dict.keys()))
#     ypoints = np.array(list(flip_dict.values()))
#
#     plt.plot(xpoints, ypoints)
#     plt.title("Gaussian distribution")
#     plt.xlabel("Heads count")
#     plt.ylabel("Drop percentage %")
#     plt.legend()
#     plt.show()
#
#
# result_dict = flip_coin()
# draw_gaussian_distribution_graph(result_dict)
