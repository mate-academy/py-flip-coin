from app.main import flip_coin

import matplotlib.pyplot as plt
import numpy as np


def draw_gaussian_distribution_graph() -> None:
    drop_coins = flip_coin()
    xpoints_array = []
    ypoints_array = []
    for key, value in drop_coins.items():
        xpoints_array.append(key)
        ypoints_array.append(value)

    xpoints = np.array(sorted(xpoints_array))
    ypoints = np.array(ypoints_array)

    plt.plot(xpoints, ypoints)

    plt.title("Gaussian distribution")
    plt.xlabel("Heads count")
    plt.ylabel("Drop percentage %")
    plt.axis([0, 10, 0, 100])

    plt.show()
